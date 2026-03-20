# Fuzzy-Credit-Risk-System
A fuzzy inference system for credit risk analysis, implemented from scratch in pure Python (no external libraries)

This project implements a complete fuzzy logic system to evaluate credit risk based on a client's credit score.

Instead of using rigid thresholds (e.g., `score > 600`), the system applies fuzzy logic to model uncertainty and gradual transitions between risk levels.

## Model Description

### Input
- Credit Score (0 – 800)

### Fuzzy Sets
- High Risk
- Medium Risk
- Low Risk

### Output
- Credit Approval Level (0 – 100%)
- Converted to Risk Percentage

## Mathematical Concepts

The system is based on fuzzy set theory and follows a complete fuzzy inference pipeline:

### 1. Fuzzification
The crisp input (credit score) is mapped into fuzzy values using membership functions:

- Triangular function:
μ(x) =
0 if x ≤ a or x ≥ c
(x - a)/(b - a) if a < x < b
(c - x)/(c - b) if b ≤ x < c


- Trapezoidal function:
μ(x) =
0 if x ≤ a or x ≥ d
(x - a)/(b - a) if a < x < b
1 if b ≤ x ≤ c
(d - x)/(d - c) if c < x < d


---

### 2. Rule Evaluation (Mamdani Inference)

Fuzzy rules are applied to map input sets to output sets:

- High Risk → Low Credit Approval  
- Medium Risk → Medium Credit Approval  
- Low Risk → High Credit Approval  

The degree of activation of each rule is computed using:

- AND operator → `min`

---

### 3. Aggregation

The outputs of all rules are combined into a single fuzzy set using:

- OR operator → `max`

---

### 4. Defuzzification (Centroid Method)

The aggregated fuzzy output is converted into a crisp value using the centroid formula:
y* = Σ(x · μ(x)) / Σ(μ(x))


This represents the "center of mass" of the resulting fuzzy distribution.

---

### 5. Final Risk Calculation

The final credit risk is obtained by inverting the approval level:
Risk (%) = 100 - Approval (%)
