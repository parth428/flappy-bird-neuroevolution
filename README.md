# Python Project: Flappy Bird with NEAT AI

This project is an implementation of the Flappy Bird game, enhanced with NEAT (NeuroEvolution of Augmenting Topologies) AI to create an intelligent agent that learns to play the game autonomously.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Running the Project](#running-the-project)
- [Results](#results)
- [Future Improvements](#future-improvements)

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

## How It Works

The NEAT AI algorithm enables the creation of an evolving neural network that learns to play Flappy Bird through fitness scores. Here’s a breakdown of how NEAT works in this project:

- Initialization of Population: NEAT starts by creating a population of simple neural networks (agents) with minimal structure. These agents will play the Flappy Bird game, with each network controlling a simulated bird.
  
- Evaluating Fitness: Each neural network (or agent) is evaluated based on a fitness score, which, in this case, is determined by how long the bird survives and how far it travels. Higher fitness scores are awarded to networks that allow the bird to navigate more obstacles.
  
- Selection and Reproduction: After each generation, the networks with the highest fitness scores are selected to form the basis for the next generation. NEAT introduces crossover and mutation in these networks, creating a new generation of agents with slightly modified characteristics, ideally improving performance over time.
  - Crossover: Combines genes from two parent networks to form a new network, inheriting traits from both.
  - Mutation: Randomly changes certain attributes, such as network weights or node connections, introducing variety into the population.

- Complexifying the Network: One of NEAT’s core strengths is its ability to complexify networks by adding nodes and connections only as needed. Starting with simple networks, NEAT progressively adds complexity, leading to an optimized network capable of higher performance without excessive structural overhead.
  
- Iterating Generations: This process of selection, crossover, mutation, and complexification continues for several generations. Over time, networks evolve to exhibit improved gameplay, adapting their strategies based on fitness criteria.
  
The config-feedforward.txt file sets key NEAT parameters, including:
  - Population Size: Defines the number of agents in each generation.
  - Fitness Criterion: Specifies how fitness is measured.
  - Mutation and Crossover Rates: Determines how frequently changes occur in the network’s structure.
    
This evolutionary approach allows the agent to autonomously improve its ability to navigate the Flappy Bird game through successive generations, adapting its neural network structure to achieve higher scores.

## Running The Project
```bash
  python flappy_bird.py
  ```
The program will initiate the Flappy Bird game. NEAT will begin to train a neural network agent to play the game by evaluating its performance in successive generations.

## Results
As the generations progress, the birds begin to improve significantly, learning when to flap to avoid hitting pipes. With each new generation, the networks evolve better strategies for survival.

After running the NEAT algorithm for a sufficient number of generations, you'll observe:
    - Birds surviving longer
    - Increasing fitness scores
    - Better overall performance in navigating through the pipes
  
Example Results:
    - Generation 1: The birds will likely crash quickly as they have not yet learned to navigate the pipes.
    - Generation 10: After several generations, the birds should be able to pass through multiple pipes without hitting them.

## Future Improvements

Potential future enhancements to this project include:
  - Implementing a graphical user interface for easier parameter tuning.
  - Adjusting NEAT parameters for faster training.
  - Adding a feature to visualize the neural network’s structure.

