"""
Create blind A/B test pairs from TSS-MoVe evaluation data.

For each question (after inner-joining the CSV with all three run folders),
all C(5,2)=10 pairs of the 5 answer variants are generated with randomised
A/B assignment.

Output files (written to data/):
  ab_test_blind.csv  – for evaluators: pair_id, Fragestellung, Antwort_A, Antwort_B, Bewertung
  ab_test_key.csv    – for reconstruction: pair_id, Fragestellung, Variante_A, Variante_B
"""

import json
import random
from itertools import combinations
from pathlib import Path

import pandas as pd

RANDOM_SEED = 42
DATA_DIR = Path("data")

# Maps variant name → DataFrame column that holds its answer text
VARIANT_COLS = {
    "original":      "Antwort",
    "chatgpt_bezug": "ChatGPT Antwort (Bezug zu Dokument)",
    "run_v2":        "ans_v2",
    "run_v3":        "ans_v3",
    "run_fid":       "ans_fid",
}

# Maps target column name → run folder (same load pattern as evaluate_testdata.py)
RUN_DIRS = {
    "ans_v2":  "Eval_Dataset_Results_v2",
    "ans_v3":  "Eval_Dataset_Results_v3",
    "ans_fid": "FIDMove_Results_v2",
}


def load_run(run_dir: Path) -> pd.DataFrame:
    rows = []
    for fpath in run_dir.glob("*.json"):
        with open(fpath, encoding="utf-8") as f:
            data = json.load(f)
        rows.append({
            "Fragestellung": data["metadata"]["query"],
            "answer":        data["final_output"]["answer"],
        })
    return pd.DataFrame(rows)


def main():
    random.seed(RANDOM_SEED)

    df = pd.read_csv(DATA_DIR / "TSS-MoVe_Testdaten_Fragestellungen.csv")

    # Drop duplicate questions before merging (keep first occurrence).
    # The CSV has 2 rows for some questions answered against different source docs;
    # since the run folders only have one answer per question, keeping duplicates
    # would produce double pairs for those questions.
    df = df.drop_duplicates(subset="Fragestellung", keep="first").reset_index(drop=True)

    # Inner-join with each run folder (drops questions not present in all runs)
    for col_name, folder_name in RUN_DIRS.items():
        run_df = load_run(DATA_DIR / folder_name).rename(columns={"answer": col_name})
        df = pd.merge(df, run_df, on="Fragestellung", how="inner")

    variants = list(VARIANT_COLS.keys())
    blind_rows = []
    key_rows = []
    skipped = 0
    pair_id = 0
    for _, row in df.iterrows():
        question = row["Fragestellung"]
        for var_a, var_b in combinations(variants, 2):
            ans_a = row[VARIANT_COLS[var_a]]
            ans_b = row[VARIANT_COLS[var_b]]

            # Skip pairs where either answer is missing or empty
            if not isinstance(ans_a, str) or not ans_a.strip():
                print(f"  WARNING: skipping pair ({var_a}, {var_b}) for '{question[:60]}' — {var_a} answer is empty")
                skipped += 1
                continue
            if not isinstance(ans_b, str) or not ans_b.strip():
                print(f"  WARNING: skipping pair ({var_a}, {var_b}) for '{question[:60]}' — {var_b} answer is empty")
                skipped += 1
                continue

            # Randomly decide which answer goes to column A
            if random.random() < 0.5:
                var_a, var_b = var_b, var_a
                ans_a, ans_b = ans_b, ans_a

            blind_rows.append({
                "pair_id":       pair_id,
                "Fragestellung": question,
                "Antwort_A":     ans_a,
                "Antwort_B":     ans_b,
                "Bewertung":     "",
                "Variante_A":   var_a,
                "Variante_B":   var_b,
            })

            pair_id += 1

    blind_df = pd.DataFrame(blind_rows)
    # Shuffle all rows
    df_shuffled = blind_df.sample(frac=1, random_state=RANDOM_SEED)

    blind_path = DATA_DIR / "ab_test_blind.csv"
    key_path   = DATA_DIR / "ab_test_key.csv"

    df_shuffled.drop(columns=["Bewertung", "Antwort_A", "Antwort_B"]).to_csv(key_path, index=False)
    df_shuffled.drop(columns=["Variante_A", "Variante_B"]).to_csv(blind_path, index=False)

    print(f"Questions after merge : {len(df)}")
    print(f"Pairs per question    : {len(list(combinations(variants, 2)))}")
    print(f"Pairs skipped (empty) : {skipped}")
    print(f"Total pairs written   : {len(blind_df)}")
    print(f"Written: {blind_path}")
    print(f"Written: {key_path}")


if __name__ == "__main__":
    main()
