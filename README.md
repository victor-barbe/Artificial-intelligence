# Artificial-intelligence

This repository will contain various artificial intelligence projects

## Description

These artificial intelligence project were created for my engineering classes, or either by personnal interest.

## 1. `Newton's gradient `

The goal of this project it to take a function of the form ax^2 + bx + c with a a matrix, b a vector and c a number, all defined in the real numbers. Then we have to find the lowest part of the function using newton's gradient method.

## 2. `Genetic algorithm `

The goal of this project it to take a function of the form ax^2 + bx + c with a a matrix, b a vector and c a number, all defined in the real numbers. The genetic algorithm will have to find the lowest point of the function.$

## 3. `Chess game `

The goal of this project is to create a complete chess game, with an artificial intelligence based on the min max algorithm

## 4. `Event prediction in a bayesian network`

This project should base its work on a JSON file defining different events, their probability and the links between events. Then here are its functionalities:

1. It should print out the nodes forming a Markov blanket for the selected variable

2. accepts evidence – which sets the observed variables of specific nodes

3. Be able to answer simple queries – i.e. it returns the probability distribution of the
   selected query variables

4. To perform these, it should use MCMC algorithm with GIBBS sampling

## 5. `Classification`

1. This program distinguishes cancer versus normal patterns from mass-spectrometric data based on the dataset:
   https://archive.ics.uci.edu/ml/datasets/Arcene

2. We use at least two separate methods (Random Forrest and Gradient Boosting) and compare them to each other, the solution is resolved as a classifier. We compare accuracy on the training set and on the test set.

## 6. `Artificial neuronal network`

This program implemens a two-layer perceptron. Make it learn to represent a function `f : [-10,10] → R` of the form `sin(x + sqrt(6)) + cos(x + sqrt(5))`.
The neural network learns with the stochastic gradient descent, based on successive draws from the plot of the f function.

## 7. `Q-Learning algorithm and the Taxi problem`

The goal of this program is to solve the Taxi problem (find the least expensive path to a point).

The prepared solution should consist of 3 parts:

1. Training program. It should accept algorithm parameters, display some quality metric (e.g. episode reward) during training, and save the trained model.

2. Visualisation program. It should be able to load the model saved by the training program and display the environment state while the loaded mo- del controls the actions of the agent.

3. Trained model. For the demonstration, a model should be trained in ad- vance. Do not include the model in the sent files.
