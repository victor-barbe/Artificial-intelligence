# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:39:32 2021

@author: User
"""

import numpy as np
import random as random
import time

print("first, you have to enter the differents values to create your function")

def defDimension():
    print("\nplease enter the dimension of the space of the fonction ")
    dimension = int(input())
    return(dimension)

global dimension
dimension = defDimension()

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

#user can here give the coordinates of the first point Xo
def valeurFirstPoint():
    
    #creating the first point X
    column = 1
    vector_X = []

    print("\nplease enter the coordinate of the first point X0 ")

    for i in range(dimension):        
        x =[]  
        for j in range(column):      
            x.append(int(input()))  
        vector_X.append(x)  
 
 
    for i in range(dimension):  
        for j in range(column):  
            print(vector_X[i][j], end = " ")  
        print()  

    return(vector_X)

#global values used in different functions
global matrix_A 
matrix_A = valeurMatrice()
global vector_B
vector_B = valeurVector()
global c 
c = valeurConstant()


#calculates the gradient using the users values 
def calculateGradient(curentPoint):
    
    #matrix_A = valeurMatrice()
    vector_X = curentPoint
    #vector_B = valeurVector()
    
    a=np.array(matrix_A)
    matrix_C = a.T + a
     
    c = np.array(matrix_C)    
    d = np.array(vector_X)
 
    matrix_product = []
    p = np.array(matrix_product)
    p = np.dot(c,d)

    matrix_gradient = []
    matrix_gradient = vector_B + p

    return(matrix_gradient)



#user defines a domain and then the first coordinates are chosen randomly
def randomFirstPoint():
    
    print("\nplease choose a domain where the first point will be generated, enter the two integer boundaries")
    begin_domain = int(input())
    end_domain = int(input())
    vector_X = []
    
    column = 1
    for i in range(dimension):        
        x =[]  
        for j in range(column):      
            x.append(random.randint(begin_domain, end_domain))  
        vector_X.append(x) 
    return(vector_X)

#gradient descent method
def gradientDescentMethod(iterationMax,firstPoint,step):
    total_time = 0
    compteur = 0
    curentPoint = firstPoint
    while compteur < iterationMax and total_time<1:      #calculation will stop on number of iteration or computing time
        time_start = time.time()
        compteur = compteur + 1
        gradient = calculateGradient(curentPoint)
        curentPoint -= step * gradient
        print("\nthis is the curent point x ")
        print(curentPoint)
        print("\nthis is the value of J(x)")
        j = calculateValueFonction(curentPoint)
        print(j)
        print ("\nend of the iteration number %d" %compteur)
        time_elapsed = time.time()-time_start
        total_time += time_elapsed
    
#calculate the value of J(x) on the current point
def calculateValueFonction(curentPoint):
    vector_X = curentPoint
    x=np.array(vector_X)
    vector_X_Transposate = x.T
    b=np.array(vector_B)
    vector_B_Transposate = b.T
    a=np.array(matrix_A)
    j = c + vector_B_Transposate.dot(x) + vector_X_Transposate.dot(a.dot(x))
    return(j)

#newton's gradient method    
def newtonGradientMethod(iterationMax,firstPoint):
    compteur = 0
    curentPoint = firstPoint
    total_time = 0
    while compteur < iterationMax and total_time<1:          #calculation will stop on number of iteration or computing time
        time_start = time.time()
        compteur = compteur + 1
        gradient = calculateGradient(curentPoint)
        a = np.array(matrix_A)
        hessianQuadratic = a + a.T
        
        curentPoint -= np.linalg.pinv(hessianQuadratic).dot(gradient)
        print("\nthis is the current point x ")
        print(curentPoint)
        print("\nthis is the value of J(x)")
        j = calculateValueFonction(curentPoint)
        print(j)
        print ("\nend of the iteration number %d" %compteur)
        time_elapsed = time.time()-time_start
        total_time += time_elapsed

#batch mode for newton's method
def batchModeNewton(numberRestarts,iterationMax):
    
    print("\nplease choose a domain where the first point will be generated, enter the two integer boundaries")
    begin = int(input())
    end = int(input())
    
    firstPoint = randomForBatchMode(begin, end)
    vectorSum = []
    for i in range(numberRestarts):
        compteur = 0
        curentPoint = firstPoint
        while compteur < iterationMax:
            compteur += 1
            gradient = calculateGradient(curentPoint)
            a = np.array(matrix_A)
            hessianQuadratic = a + a.T
        
            curentPoint -= np.linalg.pinv(hessianQuadratic).dot(gradient)
            j = calculateValueFonction(curentPoint)
        vectorSum.append(j)
        firstPoint = randomForBatchMode(begin, end)
    
    sum = np.array(vectorSum)
    mean = sum.mean()
    standardDeviation = np.std(sum,0)
    print("\nthis is the mean of the j over the iterations")
    print(mean)
    print("\nthis is the standard Deviation over the iterations")
    print(standardDeviation)
    
 
#batch mode for the simple gradient method
def batchModeDescentGradient(numberRestarts,iterationMax,step):
    print("\nplease choose a domain where the first point will be generated, enter the two integer boundaries")
    begin = int(input())
    end = int(input())  
    firstPoint = randomForBatchMode(begin, end)
    vectorSum = []
    
    for i in range (numberRestarts):
        compteur = 0
        curentPoint = firstPoint
        while compteur < iterationMax:
            compteur = compteur + 1
            gradient = calculateGradient(curentPoint)
            curentPoint -= step * gradient
            j = calculateValueFonction(curentPoint)
        vectorSum.append(j)
        firstPoint = randomForBatchMode(begin, end)
    
    sum = np.array(vectorSum)
    mean = sum.mean()
    standardDeviation = np.std(sum,0)
    print("\nthis is the mean of the j over the iterations")
    print(mean)
    print("\nthis is the standard Deviation over the iterations")
    print(standardDeviation)
        

#function to choose random coordinates for batch mode
def randomForBatchMode(begin,end):
    vector_X = []
    column = 1
    for i in range(dimension):        
        x =[]  
        for j in range(column):      
            x.append(random.randint(begin, end))  
        vector_X.append(x) 
    return(vector_X)
    
    


#user can choose here the way the program will calculate in a menu


print("\nEnter 0 to chose Newton's method, 1 for the simple gradient method, 2 for the batch mode with newton method and 3 for the batch mode with the simple gradient method")
gradientMethod = int(input())

if gradientMethod == 2:
    print("\nchoose the number of restarts for the newton batch mode")
    n = int(input())
    batchModeNewton(n, 50)
elif gradientMethod == 3:
    print("\nchoose the number of restarts for the newton batch mode")
    n = int(input())
    batchModeDescentGradient(n, 100, 0.01)
    

if gradientMethod < 2:
    
    print("\ndo you want to chose the first point, or make it random. Enter 0 to chose it, 1 to make it random")
    firstPointMethod = int(input())
    
    if firstPointMethod == 0:
        vector_X = valeurFirstPoint()
    else:
        vector_X = randomFirstPoint()


    if gradientMethod == 0:
        newtonGradientMethod(10, vector_X)
    elif gradientMethod == 1:
        gradientDescentMethod(100, vector_X, 0.01)


