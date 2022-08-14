# This project will be based on a few assumptions:

# The Linear Regression model being built will be strictly linear - that is, we will only be dealing with one independent variable and two parameters
# The input data will be in the form of a CSV file

# Steps to doing this:

# Importing relevant libraries
from sympy import *
import numpy as np 
from matplotlib import pyplot as plt


# 1. Input data as x list and y list - Here we take those as inputs in the final function

# 2. Define hypothesis function
def hypothesis(t0, t1, x_arr):
    hyp_arr = []
    for i in range(len(x_arr)):
        hyp_arr.append(t0+t1*x_arr[i])
    return hyp_arr

# 3. Define Cost function 
def cost(hyp_arr, y_arr):
    j = 0
    for i in range(len(y_arr)):
        print(i, end=" ")
        j += (hyp_arr[i]-y_arr[i])**2
    j /= 2*len(y_arr)
    return j

# 4. Define Gradient Descent
def gradDesc(t0, t1, j, a, threshold):

    x=0
    y=0

    expr0 = diff(j,t0)
    expr1 = diff(j,t1)

    p = expr0.subs(t0, x)
    q = p.subs(t1, y)

    r = expr1.subs(t0, x)
    s = r.subs(t1, y)

    while abs(q)>threshold or abs(s)>threshold:
    # for i in range(10):
        print(x,y, q,s)
        x -= a*q
        y -= a*s


        p = expr0.subs(t0, x)
        q = p.subs(t1, y)

        r = expr1.subs(t0, x)
        s = r.subs(t1, y)

    return x,y


# 5. Putting it all together to find the values of t0 and t1
def linearRegression(x_arr, y_arr):
    x_arr = x_arr.tolist()
    y_arr = y_arr.tolist()
    t0, t1 = symbols("t0 t1")
    hyp_arr = hypothesis(t0, t1, x_arr)
    j = cost(hyp_arr, y_arr)
    t0, t1 = gradDesc(t0, t1, j, 0.0001, 1)


# 6. Graphing
    x = np.linspace(min(x_arr)-10,max(x_arr)+10 ,100)
    y = t1*x + t0
    plt.plot(x,y, '-r')
    plt.scatter(x_arr, y_arr)
    plt.savefig("plot.png")