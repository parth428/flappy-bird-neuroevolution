# Python Project: Flappy Bird with NEAT AI

This project is an implementation of the Flappy Bird game, enhanced with NEAT (NeuroEvolution of Augmenting Topologies) AI to create an intelligent agent that learns to play the game autonomously.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Running the Project](#running-the-project)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)

## Introduction
This project combines the popular Flappy Bird game mechanics with NEAT AI to simulate evolutionary behavior in a neural network. Using NEAT, the AI agent trains through several generations to improve its performance in navigating through obstacles in the game.

### What is NEAT?
NEAT, or **NeuroEvolution of Augmenting Topologies**, is a genetic algorithm designed to evolve artificial neural networks. NEAT optimizes both the topology (structure) and weights of a neural network simultaneously, allowing networks to evolve over time by mimicking natural selection. This method is beneficial for tasks that require continuous adaptation, as it grows neural networks incrementally, adding complexity only as needed.

For more information, you can check out the [NEAT-Python Documentation](https://neat-python.readthedocs.io/en/latest/).

## Installation
To get started with this project, you’ll need Python and a few dependencies. Install them with the following command:

  ```bash
  pip install pygame neat-python
  ```
  [Pygame Documentation](https://www.pygame.org/docs/)
  
  [NEAT-Python Documentation](https://neat-python.readthedocs.io/en/latest/)

Please then download the files: `flappy_bird.py`, `config-feedforward.txt`, and the `imgs` folder, and save them all in the same directory on your machine.

### How It Works

