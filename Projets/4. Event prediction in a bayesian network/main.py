# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import random as random

fluFile = open('C:\\Users\\User\\PycharmProjects\\[EARIN] Exercice 5 BARBE Victor DEBEAUVAIS Guillaume\\jsonfiles\\burglary', 'r') # opens file read mode
fluData = fluFile.read() # reads data of flu file

network = json.loads(fluData)

relationList = network['relations'] # creates a list containing all relations
nodesList = network['nodes'] # creates a list containing all nodes


def markov_blanket(node):
    markovBlanketParents = []
    markovBlanketChildren = []
    markovBlanketParentsOfChildren = []
    markovblanket = [] #creating markov blanket

    for i in range (len(relationList[node]['parents'])):
        markovBlanketParents.append(relationList[node]['parents'][i]) #adding the parents

    for i in range(len(relationList)):
        for j in range(len(relationList[nodesList[i]]['parents'])):  #adding the children
            if relationList[nodesList[i]]['parents'][j] == node:  # adding the children
                markovBlanketChildren.append(nodesList[i])  # adding the children

                for x in range (len(relationList[nodesList[i]]['parents'])):  #adding parents of the children
                    if relationList[nodesList[i]]['parents'][x] != node:
                        markovBlanketParentsOfChildren.append(relationList[nodesList[i]]['parents'][x])

    markovblanket.append(markovBlanketParents)
    markovblanket.append(markovBlanketChildren)
    markovblanket.append(markovBlanketParentsOfChildren)

    return markovblanket




def mcmc(evidence,evidenceList,query):
    answer = []
    calculus = []
    passage = 0
    markovBlanket = markov_blanket(query)

    for i in range (len(network['nodes'])): #setting the value of observed variable according to evidence
        calculus.append('F')
        for j in range (len(evidenceList)):
            if network['nodes'][i] == evidenceList[j]:
                calculus[i] = evidence[evidenceList[j]]
                passage = 1
        if passage == 0 :
            a = random.randint(0, 1)  #randomly setting non observed values
            if a == 0:
                calculus[i] = 'F'
            elif a == 1:
                calculus[i] = 'T'
            
        passage = 0


    queryIndex = 0                              #getting position of query in the network
    for i in range(len(network['nodes'])):
        if network['nodes'][i] == query:
            queryIndex = i

    listeParents = []
    statusListeParent = []      #getting the list of parents of the query and if they are true or false
    for i in range(len(relationList[nodesList[queryIndex]]['parents'])):
        listeParents.append(relationList[nodesList[queryIndex]]['parents'][i]) #liste de parents du query
    for i in range(len(network['nodes'])):
        for j in range(len(listeParents)):
            if network['nodes'][i] == listeParents[j]:
                statusListeParent.append(calculus[i])  #getting if the parents are true or false

    print("please enter in caps seperated by a comma the value found by the algorithm which are")
    for i in range(len(statusListeParent)):
        print(statusListeParent[i])
    print("T")
    p = input()
    probabilityQueryKnowingParents = relationList[nodesList[queryIndex]]['probabilities'][p] #the probability of the query knowing parents

    alpha = 1 # alpha = 1/proba evidence  are true
    '''''
    for i in range(len(network['nodes'])):
        for j in range(len(listeParents)):
            if network['nodes'][i] == listeParents[j]:
                alpha = alpha * relationList[nodesList[i]]['probabilities']['T']
    '''
    probabilityChildrenKnowingParents = []
    childrenList = []

    for i in range(len(markovBlanket[1])):
        childrenList.append(markovBlanket[1][i])
    parentsOfChildrenList = []
    statusParentsOfChildrenList = []
    #parentsOfChildrenList.append(markovBlanket[2])


    for i in range(len(childrenList)):
        print("children index")
        print(i)
        print("name of the children")
        print(childrenList[i])
        childrenIndex = 0  # getting position of children in the network
        for j in range(len(network['nodes'])):
            if network['nodes'][j] == childrenList[i]:
                childrenIndex = j


        for x in range(len(relationList[nodesList[childrenIndex]]['parents'])):
            parentsOfChildrenList.append(relationList[nodesList[childrenIndex]]['parents'][x])  # liste de parents du children
        for x in range(len(network['nodes'])):
            for j in range(len(parentsOfChildrenList)):
                if network['nodes'][x] == parentsOfChildrenList[j]:
                    statusParentsOfChildrenList.append(calculus[x])  # getting if the parents are true or false


        print(parentsOfChildrenList)
        print("please enter in caps seperated by a comma the value found by the algorithm for the children which are")
        for x in range(len(statusParentsOfChildrenList)):  #pritting the proba that has to be used
            print("here status of parents")
            print(statusParentsOfChildrenList[x])
            print(parentsOfChildrenList[x])
        print("here status of the child")
        print(childrenList[i])
        print(calculus[childrenIndex])
        d = input()
        probabilityChildrenKnowingParents.append(relationList[nodesList[childrenIndex]]['probabilities'][d])

        parentsOfChildrenList.clear() #clearing for next iteration
        statusParentsOfChildrenList.clear()

    productOfChildren = 1
    for i in range(len(probabilityChildrenKnowingParents)):
        productOfChildren = productOfChildren * probabilityChildrenKnowingParents[i]






    finalProba = probabilityQueryKnowingParents * productOfChildren * alpha

    return calculus,listeParents,statusListeParent,probabilityQueryKnowingParents,probabilityChildrenKnowingParents,finalProba




evidence={"John_calls":"T", "Marry_calls": "T"}
evidenceList = ["John_calls", "Marry_calls"]
query='alarm'


a = mcmc(evidence,evidenceList,query)

print(a)


