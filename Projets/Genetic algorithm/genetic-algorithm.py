# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:01:27 2021

@author: User
"""

import numpy as np
import random as random

from operator import itemgetter


def defDimension():
    print("\nplease enter the dimension of the space of the fonction ")
    dimension = int(input())
    return(dimension)


#user chooses the value of the constent
def valeurConstant():
    print("\nenter the value of the constent C please" )
    c = float(input())
    return(c)

#user chooses the value of the matrix 
def valeurMatrice():
   
    matrix_A = []  
    print("\nEnter the entries row wise for the matrix:")  
 
 
    for i in range(dimension):        
        a =[]  
        for j in range(dimension):      
            a.append(int(input()))  
        matrix_A.append(a)  
 
 
    for i in range(dimension):  
        for j in range(dimension):  
            print(matrix_A[i][j], end = " ")  
        print()  

    return(matrix_A)

    
#user chooses the value of the vector
def valeurVector():
    column = 1     
    vector_B = []  
    print("\nEnter the entries row wise for the vector:")   
    for i in range(dimension):        
        b =[]  
        for j in range(column):      
            b.append(int(input()))  
        vector_B.append(b)  
  
    for i in range(dimension):  
       for j in range(column):  
           print(vector_B[i][j], end = " ")  
       print()  

    print("\nfin de l'entrée du vecteur ")

    return(vector_B)


dimension = defDimension()
matrix_A = valeurMatrice()
vector_B = valeurVector()
c = valeurConstant()
populationSize = 50
d = 3
crossoverProbability = 0.9
mutationProbability = 0.1

#matrix_A = [[-2, 1, 0], [1, -2, 1], [0, 1, -2]]
#vector_B = [-14, 14, -2]
#c = -23.5

def generateRandomMatrix(row,collum):
    matrix_X = []
    
    for i in range(row):        
        x =[]  
        for j in range(collum):      
            x.append(random.randint(0,1))  
        matrix_X.append(x)  
 
    X = np.array(matrix_X)       
    return X

      
def binaryToScalar (B):
    C = np.matrix([int(''.join(str(x) for x in column),2) for column in B]).reshape((B.shape[0],1))
    return C


def calculateFitness(curentPoint):
    vector_X = curentPoint
    x=np.array(vector_X)
    vector_X_Transposate = x.T
    b=np.array(vector_B)
    vector_B_Transposate = b.T
    a=np.array(matrix_A)
    j = c + vector_B_Transposate.dot(x) + vector_X_Transposate.dot(a.dot(x))
    return(j)


def createPopulation():
    
    populationArray = []
    
    for i in range(populationSize):
        a = generateRandomMatrix(dimension, d)
        b = binaryToScalar(a)
        c = calculateFitness(b)
        individual = [a,b,c,]
        populationArray.append(individual)
    
    populationFinal = sorted(populationArray,key=itemgetter(2))
    #populationFinal = populationArray
    
    for i in range(populationSize):
        print("\n")
        for j in range(3):
            print(populationFinal[i][j])
            
    print("\n")
                    
    return populationFinal


def probaList(populationFinal):
    probaList = []
    fitnessSum = 0
    scaler = abs(populationFinal[0][2])
    
    for i in range(populationSize):
        fitnessSum += populationFinal[i][2] + scaler
    
    for i in range(populationSize):
        probaList.append((populationFinal[i][2] + scaler ) / fitnessSum)
       

    return probaList

def singlePointCrossover(matrix_1, matrix_2,crossoverProbability):
    
    vector_1 = matrix_1.reshape(-1)
    vector_2 = matrix_2.reshape(-1)
    
    crossoverPoint = random.randint(0,len(vector_1))
    
    for i in range(crossoverPoint):
        o = vector_1[i]
        p = vector_2[i]
        vector_1[i] = o
        vector_2[i] = p
        
        

    
    return vector_1.reshape(matrix_1.shape), vector_2.reshape(matrix_2.shape)
            
def rouletteWheelSelection(probaList,populationFinal):
    parents = []
  
    roulette = random.uniform(0,0.95)
    
    curent = 0
    compteur=0
    for i in range (populationSize):
        curent += probaList[i]
        if (curent > roulette and compteur<2):
                parents.append(populationFinal[i][0])
                compteur+=1        
         
             
             
      
          
            
   
       
           
   
    return (parents)
 
def mutation(matrice):
    mutation = random.random()
    numberToMutate = random.randint(0, d-1)
    for i in range(dimension):
        if (mutationProbability > mutation):
            if(matrice[i][numberToMutate] == 0):
                matrice[i][numberToMutate] = 1
            elif(matrice[i][numberToMutate] == 1):
                matrice[i][numberToMutate] = 0
    return (matrice)

#binaryToScalar(generateRandomMatrix(dimension, d))

a = createPopulation()
it=300


for j in range(it):
 for i in range(populationSize-1):
  b = probaList(a)
  pair=rouletteWheelSelection(b, a)
  p1=np.array(pair[0])
  p2=np.array(pair[1])
  cross=np.array(singlePointCrossover(p1, p2, crossoverProbability))
 
  a[i][0]=cross[0]
  a[i+1][0]= cross[1]
  a[i][1]=binaryToScalar(a[i][0])
  #a[i][2]=calculateFitness(a[i][1])
  a[i+1][1]=binaryToScalar( a[i+1][0])
  #a[i+1][2]=calculateFitness(a[i+1][1])
  x=random.randint(0, populationSize-1)
  a[x][0]=mutation(a[x][0])
  a[x][1]=binaryToScalar(a[x][0])
 print("POPULATION")
 print(a)
