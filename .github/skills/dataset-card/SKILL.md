---
name: dataset-card
description: "Use when documenting a dataset for a project. Creates a structured dataset card covering origin, variables, known biases, licence, and limitations. Invoke with: /dataset-card, document dataset, create dataset card, dataset documentation, data card."
argument-hint: "Path to the dataset file or folder (e.g. data/sample.csv)"
user-invocable: true
---

# Skill: dataset-card

Create a standardised dataset card for a data file used in this project.

## Steps

### 1. Inspect the Dataset
- Read the file at the provided path (CSV or folder of CSVs).
- Extract: number of rows, columns, data types, sample values, missing value counts.

### 2. Fill the Template
Use the template at [`assets/dataset-card-template.md`](./assets/dataset-card-template.md).

Populate each section with what you can infer from the file. For sections that require human input (origin, licence, known biases), leave a clear `<!-- TODO: fill in -->` placeholder.

### 3. Save the Card
- Write the completed card to `doc/dataset-card_<filename>.md`.
- Do not overwrite an existing card — append a version note instead.

## Output

A Markdown dataset card file saved to `doc/`, plus a chat summary of the key metadata found.
