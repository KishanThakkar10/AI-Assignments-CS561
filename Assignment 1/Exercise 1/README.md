# Fraud Detection Bayesian Network Implementation

## Overview

This project implements a Bayesian Network for fraud detection using Python and the `pomegranate` library. The Bayesian Network models the relationships between various factors such as travel history, device ownership, online purchases, foreign purchases, and fraud occurrence. It allows for probabilistic inference to estimate the likelihood of fraud given observed evidence.

## Dependencies

- Python 3.x
- Required Libraries:
  - `matplotlib`: For plotting the Bayesian Network.
  - `itertools`: For creating combinations.
  - `pomegranate`: For defining probability distributions and constructing the Bayesian Network.
  - `networkx`: For network visualization.

## Files

1. `bayesian_network.py`: Main Python script containing the implementation of the Bayesian Network, conditional probability tables, and inference methods.
2. `README.md`: Markdown file containing project overview, dependencies, and usage instructions.
3. `output.png`: Image file containing the plotted Bayesian Network.

## Implementation Details

1. **Bayesian Network Construction:**
   - The Bayesian Network is constructed using the `pomegranate` library.
   - Nodes represent variables such as travel, device ownership, online purchases, foreign purchases, and fraud.
   - Dependencies between variables are defined based on domain knowledge and assumptions.

2. **Conditional Probability Tables (CPTs):**
   - Conditional probability tables are defined for each variable based on its parent variables in the network.
   - Probabilities are assigned based on the problem statement and assumptions.

## Usage

1. Ensure that Python and the required libraries are installed.
2. Run the `bayesian_network.py` script to execute the Bayesian Network implementation.
3. The script will generate the plotted Bayesian Network and provide probabilities of fraud occurrence under different evidences.

## Conclusion

This implementation provides a structured approach to model and understand the factors influencing fraud detection using Bayesian Network. It offers insights into the dependencies between variables and allows probabilistic inference to estimate fraud probabilities based on observed evidence. Further improvements could involve refining the model assumptions and incorporating real-world data for more accurate predictions.

