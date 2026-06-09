# EDA Notebook Template

Use this structure when generating a new EDA notebook with the `csv-eda-basica` skill.

---

```markdown
# EDA: <Dataset Name>

Brief description of the dataset: origin, purpose, and what questions we are trying to answer.
```

```python
# Cell 1 — Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
```

```markdown
## 1. Load and Inspect
We load the dataset and check its basic structure.
```

```python
# Cell 2 — Load
df = pd.read_csv(Path("<path_to_csv>"))
print(f"Shape: {df.shape}")
df.head()
```

```markdown
## 2. Missing Values
We check for null entries and assess data completeness.
```

```python
# Cell 3 — Missing values
df.isnull().sum().sort_values(ascending=False)
```

```markdown
## 3. Descriptive Statistics
Summary statistics for numeric and categorical columns.
```

```python
# Cell 4 — Statistics
df.describe(include="all")
```

```markdown
## 4. Distributions
Visual distribution for each numeric feature.
```

```python
# Cell 5 — Histograms
df.hist(figsize=(12, 8), bins=20)
plt.tight_layout()
plt.show()
```

```markdown
**Interpretation:** <fill in after running>
```

```markdown
## 5. Initial Questions
Based on the EDA, the following questions are worth investigating further:
1. ...
2. ...
3. ...
```

---
