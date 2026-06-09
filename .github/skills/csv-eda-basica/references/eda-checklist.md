# EDA Quality Checklist

Use this checklist at every step of an exploratory data analysis.

## 1. Loading
- [ ] File loads without encoding errors (try `utf-8`, `latin-1` if needed).
- [ ] Shape is as expected (rows × columns).
- [ ] Column names are clean (no leading/trailing spaces, no special characters).

## 2. Data Types
- [ ] Numeric columns are `float64` or `int64`, not `object`.
- [ ] Date columns are parsed as `datetime`, not `object`.
- [ ] Categorical columns are `category` or `object` with a known cardinality.

## 3. Missing Values
- [ ] No column has >50% missing values without a documented reason.
- [ ] Missing patterns are random (MAR) vs systematic (MNAR) — check with a heatmap.
- [ ] A strategy for handling missing values is defined (drop / impute / flag).

## 4. Distributions
- [ ] Numeric features: checked for skewness and outliers (IQR or z-score).
- [ ] Categorical features: checked for rare categories (<1% frequency).
- [ ] Target variable (if present): class balance documented.

## 5. Relationships
- [ ] Correlation matrix computed for numeric features.
- [ ] High-correlation pairs (>0.9) flagged for potential collinearity.
- [ ] At least one scatter or box plot per feature vs target.

## 6. Documentation
- [ ] Every plot has a title, labelled axes, and an interpretation cell.
- [ ] Dataset origin is noted (where was this file obtained?).
- [ ] Known limitations or biases are recorded.
