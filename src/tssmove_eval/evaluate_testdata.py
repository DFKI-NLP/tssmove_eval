"""
RAGAS 0.4.3 Evaluation Script — Faithfulness, AnswerRelevancy, FactualCorrectness, AnswerCorrectness

In v0.4, @experiment() replaces evaluate(). It requires a file-backed
ragas.Dataset (local/csv), not an in-memory EvaluationDataset.

The experiment function is async, processes one row at a time, calls
metric.ascore() per metric, and returns a dict with scores merged in.
Results are auto-saved to ./experiments/<timestamp>-<name>.csv

Required DataFrame columns:
  - user_input          : The user query
  - response            : The LLM-generated answer
  - retrieved_contexts  : JSON-encoded list of strings (for CSV compatibility)
  - reference           : Ground-truth answer (required by ContextPrecision)

Usage:
    pip install ragas openai pandas
    python evaluate_faithfulness.py
"""

import os
import json
import asyncio
import pandas as pd
from openai import AsyncOpenAI
from ragas import Dataset, experiment
from ragas.llms import llm_factory
from ragas.embeddings.base import embedding_factory
from ragas.metrics.collections import Faithfulness, AnswerRelevancy, AnswerCorrectness, FactualCorrectness
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# ── 1. Configuration ──────────────────────────────────────────────────────────

# Set your LLM provider API key (RAGAS uses OpenAI by default)
api_key = os.environ.get("OPENAI_API_KEY")

# Optional: use a different LLM / embeddings model
client = AsyncOpenAI(api_key=api_key)
llm        = llm_factory("gpt-5-mini", client=client, max_tokens=64000)
embeddings = embedding_factory("openai", model="text-embedding-3-small", client=client, interface="modern")

faithfulness_metric = Faithfulness(llm=llm)
answer_relevancy_metric = AnswerRelevancy(llm=llm, embeddings=embeddings)
answer_correctness_metric = AnswerCorrectness(llm=llm, embeddings=embeddings)
factual_correctness_metric = FactualCorrectness(llm=llm, mode="f1", atomicity="high", coverage="high")


DATASET_DIR = "./tmp_ragas"  # directory where ragas saves the dataset CSV
TESTDOC_DIR = "data/source_docs"

configs = [
  #{
  #  "experiment_name": "Antwort_vs_ChatGPTBezug",
  #  "col_dict": {"user_input": "Fragestellung", "response": "Antwort", "reference": "ChatGPT Antwort (Bezug zu Dokument)"},
  #},
  #{
  #  "experiment_name": "Antwort_vs_ChatGPTGeneric",
  #  "col_dict": {"user_input": "Fragestellung", "response": "Antwort",
  #               "reference": "ChatGPT Antwort Generisch (ohne Bezug auf Dokument)"},
  #},
    {
        "experiment_name": "tssmove_vs_refantwort_eval2",
        "run_dir": "data/Eval_Dataset_Results_v2",
        "col_dict": {"user_input": "Fragestellung", "response": "tss_move_antwort",
                    "reference": "Antwort"},
    },
    {
        "experiment_name": "tssmove_vs_refantwort_eval3",
        "run_dir": "data/Eval_Dataset_Results_v3",
        "col_dict": {"user_input": "Fragestellung", "response": "tss_move_antwort",
                     "reference": "Antwort"},
    },
    {
        "experiment_name": "tssmove_vs_refantwort_fidmove_v2",
        "run_dir": "data/FIDMove_Results_V2",
        "col_dict": {"user_input": "Fragestellung", "response": "tss_move_antwort",
                     "reference": "Antwort"},
    }
]

# ── 2. Sample DataFrame ───────────────────────────────────────────────────────



def load_text(filename):
    try:
        with open(filename, "r") as f:
            return [f.read()]
    except FileNotFoundError:
        print(f"File {filename} not found")
        return [" "]



# ── 3. Validation ─────────────────────────────────────────────────────────────

def validate_df(df: pd.DataFrame):
    required_cols = {"user_input", "response", "retrieved_contexts", "reference"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"DataFrame is missing required columns: {missing}")

    if df["retrieved_contexts"].apply(lambda x: isinstance(x, str)).any():
        raise TypeError(
            "The 'retrieved_contexts' column must contain lists of strings. "
            "If loaded from CSV, parse with: df['retrieved_contexts'].apply(json.loads)"
        )





# ── 4. Build a file-backed ragas.Dataset from the DataFrame ──────────────────
# @experiment() requires ragas.Dataset (not EvaluationDataset).
# retrieved_contexts is JSON-encoded as a string for CSV storage.

def build_ragas_dataset(df: pd.DataFrame, name: str, root_dir: str, col_dict: dict[str,str]) -> Dataset:
    dataset = Dataset(name=name, backend="local/csv", root_dir=root_dir)
    for _, row in df.iterrows():
        dataset.append({
            "user_input": row[col_dict["user_input"]],
            "response": row[col_dict["response"]],
            # JSON-encode the list so it survives CSV round-trip
            "retrieved_contexts": json.dumps(row["retrieved_contexts"]),
            "reference": row[col_dict["reference"]],
        })
    dataset.save()
    return dataset


# ── 5. Experiment function ────────────────────────────────────────────────────
# @experiment() takes no arguments.
# The function is async, receives one row at a time as a dict-like object,
# scores each metric, and returns a dict with the original row + scores.
# Results are auto-saved to ./experiments/<timestamp>-<name>.csv

@experiment()
async def run_evaluation(row):
    # Decode retrieved_contexts from JSON string (CSV storage format)
    contexts = json.loads(row["retrieved_contexts"])

    faith = await faithfulness_metric.ascore(
        user_input=row["user_input"],
        response=row["response"],
        retrieved_contexts=contexts,
    )
    relevancy = await answer_relevancy_metric.ascore(
        user_input=row["user_input"],
        response=row["response"],
    )
    factual_correct = await factual_correctness_metric.ascore(
        response=row["response"],
        reference=row["reference"]
    )
    answer_correct = await answer_correctness_metric.ascore(
        user_input=row["user_input"],
        response=row["response"],
        reference=row["reference"]
    )

    return {
        **row,
        "faithfulness": faith.value,
        "answer_relevancy": relevancy.value,
        "factual_correctness": factual_correct.value,
        "answer_correctness": answer_correct.value
    }


# ── 6. Run ────────────────────────────────────────────────────────────────────

async def main():
    #print("Input DataFrame:")
    #print(df[["user_input", "response"]].to_string(index=False))
    #print()
    df = pd.read_csv('data/TSS-MoVe_Testdaten_Fragestellungen.csv')

    df["retrieved_contexts"] = df["Quelle_lokal"].apply(lambda x: load_text(f"{TESTDOC_DIR}/{x}"))

    for config in configs:
    #validate_df(df)
        if "run_dir" in config:
            queries =  []
            generated_answers = []
            for file in Path(config["run_dir"]).glob("*.json"):
                with open(file, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    queries.append(file_data["metadata"]["query"])
                    generated_answers.append(file_data["final_output"]["summary"])

            new_df = pd.DataFrame({
                config["col_dict"]["user_input"]: queries,
                config["col_dict"]["response"]: generated_answers
            })

            result = pd.merge(df, new_df, on=config["col_dict"]["user_input"], how='inner')
            df = result

        dataset = build_ragas_dataset(df, name=f"rag_eval_dataset_{config['experiment_name']}",
                                      root_dir=DATASET_DIR, col_dict=config["col_dict"])

        print(f"Running experiment: {config['experiment_name']} ...")
        # name= passed to .arun() sets the experiment label in the saved CSV filename
        results = await run_evaluation.arun(dataset, name=config['experiment_name'])
        print("Evaluation complete.\n")

        # ── 7. Results ────────────────────────────────────────────────────────────
        metric_names = ["faithfulness", "answer_relevancy", "factual_correctness", "answer_correctness"]
        results_df = results.to_pandas()

        print("── Aggregate Scores ─────────────────────────────────────────")
        for metric in metric_names:
            print(f"  {metric:<25} {results_df[metric].mean():.4f}")
        print()

        output_df = df[[config["col_dict"]["user_input"], config["col_dict"]["response"], config["col_dict"]["reference"]]].copy()
        for metric in metric_names:
            output_df[metric] = results_df[metric]

        print("── Per-row Scores ───────────────────────────────────────────")
        print(output_df.to_string(index=False))
        print()

        # Results are also auto-saved by ragas to: ./experiments/<timestamp>-rag_eval_v1.csv
        output_path = f"experiments/ragas_results_{config['experiment_name']}.csv"
        output_df.to_csv(output_path, index=False)
        print(f"Results saved to '{output_path}'")
        print(f"Experiment also auto-saved to ./experiments/{config['experiment_name']}.csv")


if __name__ == "__main__":
    asyncio.run(main())