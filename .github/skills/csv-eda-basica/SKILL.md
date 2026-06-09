---
name: csv-eda-basica
description: "Use when starting exploratory data analysis on a CSV file. Detects columns, types, missing values, and distributions. Proposes initial questions and produces a structured EDA notebook. Invoke with: /csv-eda-basica, eda, explore dataset, analyze csv, check data quality."
argument-hint: "Path to the CSV file to analyse (e.g. data/sample.csv)"
user-invocable: true
---

# Skill: csv-eda-basica

Perform a structured Exploratory Data Analysis (EDA) on a CSV file.

## Steps

### 1. Load and Inspect
- Read the CSV at the path provided in the argument.
- Report: shape, column names, data types, first 5 rows.

### 2. Data Quality Check
- Count missing values per column (absolute and percentage).
- Identify columns with >20% missing values and flag them as high-risk.
- Check for duplicated rows.
- Refer to the checklist in [`references/eda-checklist.md`](./references/eda-checklist.md).

### 3. Distributions
- For numeric columns: mean, std, min, max, quartiles.
- For categorical columns: value counts and top-5 categories.
- Note any columns with suspiciously low variance (potential constants).

### 4. Propose Initial Questions
- Based on the structure and distributions found, list 3–5 analytical questions worth investigating.
- Example: "Is there a correlation between feature X and the target variable?"

### 5. Generate Notebook
- Use the notebook template at [`assets/notebook-template.md`](./assets/notebook-template.md) as the structure.
- Create a new `.ipynb` file at `notebooks/eda_<dataset_name>.ipynb` with cells matching each step above.
- Follow conventions in `.github/instructions/notebooks.instructions.md`.

## Output

A populated EDA notebook ready to run, plus a brief summary in the chat of key findings.
