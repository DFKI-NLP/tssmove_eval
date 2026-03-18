# tssmove eval

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Evaluate TSS Move Test docs

## Quickstart

### Setup

This project requires [uv](https://docs.astral.sh/uv/). If it is not already installed. please see the [installation guide](https://docs.astral.sh/uv/getting-started/installation/).

```bash
# clone project
git clone https://github.com/DFKI-NLP/tssmove_eval
cd tssmove_eval

# create a Python environment and install dependencies
uv sync

# (optional) copy the .env.example file to .env and adjust environment variables as needed
cp .env.example .env
```

## Usage

```bash
uv run -m tssmove_eval.evaluate_testdata
```

## Results

- Faithfulness - Answer vs retrieved contexts (claims supported by context)
- Answer Relevancy - Answer vs Query (generate 3 pseudo-questions from the answer, average sim(query,pseudo-question))
- Factual correctness - Answer vs reference answer, F1 at the claim level (claims in answer supported by reference)
- Answer correctness - Weighted mix of (simplified) factual correctness + embedding similarity of answer to reference

So there should be no major differences for Faithfulness and Answer relevancy between the two runs, only for 
the other 2 metrics

### ## With the ChatGPT answer (created with respect to the input document) as the reference

Running experiment: Antwort_vs_ChatGPTBezug ...
Running experiment: 100%|██████████| 24/24 [16:32<00:00. 41.35s/it]
Evaluation complete.

── Aggregate Scores ─────────────────────────────────────────

| Metric              | Score  |
|---------------------|--------|
| faithfulness        | 0.9488 |
| answer_relevancy    | 0.6368 |
| factual_correctness | 0.5121 |
| answer_correctness  | 0.6297 |

── Per-row Scores ───────────────────────────────────────────

| faithfulness  | answer_relevancy  | factual_correctness    | answer_correctness  | 
| ----------- | ----------- | ----------- | ----------- |
 | 0.800  | 0.661  | 0.180  | 0.473 | 
 | 1.000  | 0.864  | 0.410  | 0.617 | 
 | 1.000  | 0.889  | 0.360  | 0.585 | 
 | 1.000  | 0.446  | 0.490  | 0.581 | 
 | 0.840  | 0.456  | 0.300  | 0.444 | 
 | 0.944  | 0.552  | 0.390  | 0.612 | 
 | 1.000  | 0.521  | 0.680  | 0.822 | 
 | 0.882  | 0.491  | 0.480  | 0.700 | 
 | 1.000  | 0.839  | 0.520  | 0.569 | 
 | 1.000  | 0.455  | 0.450  | 0.568 | 
 | 0.793  | 0.663  | 0.620  | 0.760 | 
 | 0.931  | 0.815  | 0.880  | 0.830 | 
 | 1.000  | 0.366  | 0.730  | 0.687 | 
 | 0.920  | 0.662  | 0.660  | 0.738 | 
 | 0.818  | 0.719  | 0.610  | 0.755 | 
 | 1.000  | 0.785  | 0.690  | 0.616 | 
 | 1.000  | 0.512  | 0.330  | 0.500 | 
 | 0.867  | 0.469  | 0.310  | 0.498 | 
 | 1.000  | 0.750  | 0.300  | 0.546 | 

## With the generic ChatGPT answer as the reference

Running experiment: Antwort_vs_ChatGPTGeneric ...
Running experiment: 100%|██████████| 24/24 [15:51<00:00, 39.63s/it]
Evaluation complete.

── Aggregate Scores ─────────────────────────────────────────

| Metric              | Score  |
|---------------------|--------|
  |  faithfulness        |        0.9533 | 
  | answer_relevancy       |     0.6284 | 
  |  factual_correctness   |      0.3042 | 
  |  answer_correctness    |      0.4484  | 

── Per-row Scores ───────────────────────────────────────────

 | faithfulness  | answer_relevancy  | factual_correctness  | answer_correctness  |  
 | ----------- | ----------- | ----------- | ----------- |
 | 0.833  | 0.661  | 0.150  | 0.332  |  
 | 1.000  | 0.778  | 0.380  | 0.487  |  
 | 1.000  | 0.448  | 0.130  | 0.342  |  
 | 0.760  | 0.728  | 0.240  | 0.447  |  
 | 1.000  | 0.744  | 0.320  | 0.523  |  
 | 1.000  | 0.895  | 0.460  | 0.513  |  
 | 0.917  | 0.524  | 0.300  | 0.642  |  
 | 0.909  | 0.482  | 0.120  | 0.301  |  
 | 1.000  | 0.503  | 0.190  | 0.374  |  
 | 0.833  | 0.517  | 0.430  | 0.460  |  
 | 0.957  | 0.490  | 0.050  | 0.203  |  
 | 1.000  | 0.536  | 0.190  | 0.487  |  
 | 0.810  | 0.530  | 0.320  | 0.645  |  
 | 1.000  | 0.646  | 0.130  | 0.316  |  
 | 1.000  | 0.540  | 0.130  | 0.359  |  
 | 0.960  | 0.806  | 0.660  | 0.780  |  
 | 0.926  | 0.706  | 0.200  | 0.344  |  
 | 1.000  | 0.665  | 0.050  | 0.233  |  
 | 1.000  | 0.376  | 0.660  | 0.775  |  
 | 1.000  | 0.753  | 0.680  | 0.518  |  
 | 975.000  | 0.878  | 0.840  | 0.455  |  
 | 1.000  | 0.734  | 0.480  | 0.667  |  
 | 1.000  | 0.660  | 0.120  | 0.396  |  
 | 1.000  | 0.480  | 0.070  | 0.164  |  