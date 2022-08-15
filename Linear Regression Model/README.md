
# What is Linear Regression

In Advanced Statistical Mathematics, Linear Regression is a technique employed for determining the relationship (or function) 
between (one or more) independent variables (denoted by x) and the corresponding dependent variable (denoted by y).

The function derived from the Linear Regression approach is called the *hypothesis*. To take a simple example in one variable:

h(x) = θ0 + θ1 x

Here, h(x) is the hypothesis, and θ0 and θ1 are called parameters. Cases where a single independent variable is used are termed 
as simple linear regression, and conversely, multiple variable models are called multivariate linear regression.

The Linear Regression technique is aimed at determining the values of θ0 and θ1 such that the value of the corresponding h(x) 
is closest to the value of y (it should be noted at this point that we say closest and not equal to). This is done by using a 
specialized formula known as the Cost function denoted by J(θ).

The Cost function is a function of θ0 and θ1 (in multivariate cases or cases of higher degree dependencies, we may have more 
parameters θ2, θ3, etc.) using the Mean Square Error (MSE) technique. This is given by:

