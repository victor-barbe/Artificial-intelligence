import numpy as np
import gym
import random

# we create the environment for taxi
taxiEnvironnement = gym.make("Taxi-v3")

#creating q tables for the algo
numberActions = taxiEnvironnement.action_space.n     #to get number of possible actions
numberStates = taxiEnvironnement.observation_space.n  #to get number of possible states
qTable = np.zeros((numberStates, numberActions))  #filling the q table with zeros to initialise

# we define number of episode and steps
numberEpisode = 30000
numberTestEpisode = 150
maxStep = 200

# we define gamma and learning rate
learningRate = 0.7
gamma = 0.6

# we define variable to balance exploration and explotation
explorationRate = 1.0
#to paste reward over an episode
globalReward = []


for i in range(numberEpisode):
    state = taxiEnvironnement.reset()
    step = 0
    done = False

    for step in range(maxStep):
        explorationExplotation = random.uniform(0, 1) #to chose between exploration or exploitation
        if explorationExplotation > explorationRate:    #in this case exploitation we take bigger number
            action = np.argmax(qTable[state, :])
        else:
            action = taxiEnvironnement.action_space.sample()  #otherwise exploration, we take a random action

        new_state, reward, done, info = taxiEnvironnement.step(action) #we take an action and see outcome state and reward
        #we udpate the table following the formula
        qTable[state, action] = qTable[state, action] + learningRate * (reward + gamma * np.max(qTable[new_state, :]) - qTable[state, action])
        state = new_state #actualise the state

        if done == True: #to finish the episode
            break

    explorationRate = explorationRate - 0.01  #we reduce the value of exploration rate to get more explotation with time
    if explorationRate < 0.01: #to keep exploration rate above 0
        explorationRate = 0.01

taxiEnvironnement.reset()

for i in range(numberTestEpisode):
    state = taxiEnvironnement.reset()
    step = 0
    done = False
    totalReward = 0
    print("Episode number :")
    print(i)

    for step in range(maxStep):
        taxiEnvironnement.render()
        # take best action in a state to maximize reward
        action = np.argmax(qTable[state, :])
        newState, reward, done, info = taxiEnvironnement.step(action)
        totalReward += reward

        if done:
            globalReward.append(totalReward)
            print ("Score :")
            print(totalReward)
            break
        state = newState
taxiEnvironnement.close()

averageScore = sum(globalReward) / numberTestEpisode
print("averageScore :", averageScore)