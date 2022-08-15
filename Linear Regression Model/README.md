
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

![Screenshot 2022-08-15 at 11 37 56 AM](https://user-images.githubusercontent.com/92638241/184585233-332b4b2e-668b-4da7-96d9-5fc6b0c32003.png)

Our objective is to minimize the value of the Cost Function. We do this by the Gradient Descent Algorithm. 

![Screenshot 2022-08-15 at 12 21 41 PM](https://user-images.githubusercontent.com/92638241/184589461-136848ca-b848-4ea1-9649-a1d365766415.png)

Gradient Descent is an iterative optimization algorithm used to determine the zero gradient minima of a given function.
