# -*- coding: utf-8 -*-
"""Lab_02_Linear_Regression_2024 for students.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d8zXekWxMTV13CGNcpjVf1OzUPqQ2zut

#**<font color='blue'><b>Lab-02 Linear Regression With One Variable**

> Indented block

In the first part of the exercise, we're tasked with implementing linear regression with one variable to predict profits for a food truck. Suppose you are the CEO of a restaurant franchise and are considering different cities for opening a new outlet. The chain already has trucks in various cities and you have data for profits and populations from the cities.

**Let's start by importing some libraries and examining the data.**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

from google.colab import files
files.upload()

data = pd.read_csv('ex1data1.csv')
data.head

data.head()

data.tail()

data.shape

def computeCost(X, y, theta):
  m = len(y)
  predictions = X.dot(theta)
  square_err = (predictions - y)**2
  cost = 1/(2*m) * np.sum(square_err)
  return cost

def gradientDescent(X, y, theta, alpha, iters):
  m = len(y)
  Cost = np.zeros(iters)

  for i in range(iters):
    predictions = X.dot(theta)
    errors = predictions - y
    theta = theta - (alpha/m) * X.transpose().dot(errors)
    Cost[i] = computeCost(X, y, theta)
  return theta , Cost

alpha = 0.01
iters = 1500

X = data.iloc[:, 0].values # Feature (population)
y = data.iloc[:, 1].values # Target (profit)

    # Add a column of ones to X for the intercept term
X = np.c_[np.ones(X.shape[0]), X]
theta = np.zeros(2) # Initialize theta to zeros

Theta, C = gradientDescent(X, y, theta, alpha, iters)

computeCost(X, y, Theta)

"""**Lab-01(b) Linear Regression with multiple Variables**"""