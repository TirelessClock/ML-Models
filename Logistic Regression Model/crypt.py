# This project will be based on a few assumptions:

# The input data will contain only a single variable on which the outcome depends - i.e. only one independent variable.
# The input data will be in the form of a CSV file

# Steps to doing this:

# Importing relevant libraries
from sympy import *
from math import e
import numpy as np 
from matplotlib import pyplot as plt


# 1. Input data as x list and y list - Here we take those as inputs in the final function

# 2. Define hypothesis function
def hypothesis(t0, t1, x_arr):
    hyp_arr = []
    for i in range(len(x_arr)):
        g = 1/(1+e**(-(t0+t1*x_arr[i])))
        hyp_arr.append(g)
    return hyp_arr


# 3. Define Cost function 
def cost(hyp_arr, y_arr):
    j = 0
    for i in range(len(y_arr)):
        a = -(y_arr[i]*ln(hyp_arr[i]))
        b = -(1-y_arr[i])*(ln(1-hyp_arr[i]))
        j += a+b
    j /= len(y_arr)
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
        print(x,y, q,s)
        x -= a*q
        y -= a*s


        p = expr0.subs(t0, x)
        q = p.subs(t1, y)

        r = expr1.subs(t0, x)
        s = r.subs(t1, y)

    return x,y


# 5. Putting it all together to find the values of t0 and t1
def logisticRegression(x_arr, y_arr):
    x_arr = x_arr.tolist()
    y_arr = y_arr.tolist()
    t0, t1 = symbols("t0 t1")
    hyp_arr = hypothesis(t0, t1, x_arr)
    j = cost(hyp_arr, y_arr)
    t0, t1 = gradDesc(t0, t1, j, 1, 0.1)
    print("t0 = ", t0)
    print("t1 = ", t1)


# 6. Graphing
    x = np.linspace(min(x_arr)-10,max(x_arr)+10 ,100)
    y = t1*x + t0
    plt.plot(x,y, '-r')
    plt.scatter(x_arr, y_arr)
    plt.savefig("plot.png")
