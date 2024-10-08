# Metropolis-Hastings Sampling Implementation

This repository contains Python code implementing the Metropolis-Hastings algorithm for sampling from a complex probability distribution. The objective is to generate samples from the target distribution \( P(x) = \exp(-x^4) \cdot (2 + \sin(5x) + \sin(-2x^2)) \) using a normal distribution as the proposal distribution.

## Files Included

- `metropolis_hastings.py`: Python script containing the implementation of the Metropolis-Hastings algorithm.
- `README.md`: This README file providing an overview of the implementation.
- `MH_plots_sigma_*.png`: Images containing plots generated by the code, where '*' denotes the sigma value used in the plot.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- SciPy

## Usage

1. Run the Python script:

python metropolis_hastings.py

2. The script will generate histograms of the generated samples and plots of the Markov chain for three different values of sigma.Images of the plots will be saved in the same directory.

## Parameters

- `initial_state`: Initial value for the Markov chain.
- `iterations`: Number of iterations for the Metropolis-Hastings algorithm.
- `sigmas`: List of sigma values for the proposal distribution.

## Acknowledgments

The implementation is inspired by the assignment problem of CS561: Artificial Intelligence at IITG.


