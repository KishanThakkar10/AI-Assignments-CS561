# Hidden Markov Model (HMM) Localization

This repository contains Python code for implementing a solution for the robot localization problem using Hidden Markov Model. The HMM is applied to a grid world scenario where a robot needs to localize itself based on sensor readings in an environment with obstacles.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Overview

The implementation consists of several key components:

1. **Grid World**: The environment in which the robot operates is represented as a grid. Obstacles are denoted by '0', while empty spaces are denoted by '1'.

2. **Transition Model**: The transition model defines the probabilities of moving from one grid cell to another. It is calculated based on the neighboring empty cells.

3. **Sensor Model**: The sensor model computes the likelihood of observing a sensor reading given the true position of the robot. It considers the possibility of sensor errors.

4. **Filtering**: The filtering step calculates the posterior distribution over the robot's position given a sequence of sensor readings. It is implemented using the forward algorithm.

5. **Viterbi Algorithm**: The Viterbi algorithm is used to find the most likely path taken by the robot given a sequence of sensor readings.

6. **Hidden Markov Model (HMM)**: The main function integrates all the components to implement the HMM for localization. It iterates over different sensor error rates and evaluates the localization performance in terms of localization error and path accuracy.

## Usage

To run the HMM localization algorithm:

```bash
python robot_localization.py

