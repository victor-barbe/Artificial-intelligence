import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPRegressor
import random

f = lambda x: [[x] for x in x] #change the data to then fit to the network
X_train= np.arange(-10, 10, 0.2) #create X values
y_train = np.sin(X_train * np.sqrt(6)) + np.cos(X_train * np.sqrt(5)) #create Y values
#print(X)
#print(Y)
#print(f(X))
X_test = []
y_test = []
training_samples = 20
for i in range(training_samples): #create random samples
    X_test.append(random.uniform(-10, 10))
    y_test.append(random.uniform(-2, 2))

def neuronal_network(f,X_train,y_train,X_test,y_test):    #neuronal network
    N = 100
    print(tuple([N]*10))
    neuronalNetwork = MLPRegressor(hidden_layer_sizes = tuple([100]*10))
    neuronalNetwork.fit(f(X_train),y_train)
    neuronalNetwork.score(f(X_test),f(y_test))
    predicted_sin = neuronalNetwork.predict(f(X_train))
    return(predicted_sin)

def display(X_train,y_train,predicted_sin):  #to display the real and approximated function
    plt.plot(X_train,y_train)
    plt.plot(X_train, predicted_sin)
    plt.legend(["Real function", "Network approximated function"])
    plt.xlim(-10, 10)
    plt.ylim(-2, 2)
    plt.show()

#def training():


neuronalNetwork = neuronal_network(f,X_train,y_train,X_test,y_test)
display(X_train,y_train,neuronalNetwork)





