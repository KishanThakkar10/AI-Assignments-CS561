import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the target distribution function P(x)
def target_distribution(x):
    return np.exp(-x**4) * (2 + np.sin(5*x) + np.sin(-2*x**2))

# Define the proposal distribution
def proposal_distribution(x, sigma):
    return norm.rvs(loc=x, scale=sigma)

# Metropolis-Hastings algorithm
def metropolis_hastings(iterations, initial_state, sigma):
    samples = [initial_state]
    current_state = initial_state

    for _ in range(iterations):
        # Generate a candidate from the proposal distribution
        candidate_state = proposal_distribution(current_state, sigma)

        # Calculate acceptance ratio
        acceptance_ratio = min(1, target_distribution(candidate_state) / target_distribution(current_state))

        # Accept or reject the candidate
        if np.random.uniform(0, 1) < acceptance_ratio:
            current_state = candidate_state
        samples.append(current_state)

    return samples

# Parameters
initial_state = -1
iterations = 1500
sigmas = [0.05, 1, 50]

# Generate and save plots for each sigma value
for sigma in sigmas:
    samples = metropolis_hastings(iterations, initial_state, sigma)

    # Plot histogram of generated samples and Markov chain
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Plot histogram of generated samples
    axs[0].hist(samples, bins=50, density=True, alpha=0.5, color='blue')
    x_values = np.linspace(-2, 2, 1000)
    axs[0].plot(x_values, target_distribution(x_values), color='red', label='Actual Distribution')
    axs[0].set_title(f'Histogram with Sigma={sigma}')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Density')
    axs[0].legend()

    # Plot generated sample versus iteration
    axs[1].plot(samples)
    axs[1].set_title(f'Markov Chain with Sigma={sigma}')
    axs[1].set_xlabel('Iteration')
    axs[1].set_ylabel('Generated Sample')

    # Adjust layout
    plt.tight_layout()

    # Save the plot as a PNG image
    plt.savefig(f'MH_plots_sigma_{sigma}.png')

    # Show the plot
    plt.show()
