#Linear Algebra: 

'''
Refence Page: https://developers.google.com/machine-learning/crash-course/linear-regression
youtube for ML: https://www.youtube.com/@Dr.NancyJane 

formulae: 
y = ax+b or y = b+wx (for one input or indepandant var) or y= b+w1x1+w2x2....+WnXn (n is number of input or indepandant vars)  

y - predicted value or dependant var
b - bias or y intercept  
w - weight or the rate x changes
x - input or indepandant var

example:

Pounds in 1000s (feature)	Miles per gallon (label)
3.5	                        18
3.69	                    15
3.44	                    18
3.43	                    16
4.34	                    15
4.42	                    14
2.37	                    24

Predict the Miles per gallon for 4 pounds(4000)?

Step1: find the dependant and Independant var
Independant var = Pounds
Dependant var = Miles per gallon

Step2: Understand the linear relationship 
Here if car weight increases then the Miles per gallon is get reduced hence its negative linear relationship (Will understand better via scatter plots)

Step3: find weight or W
w = the rate x changes (car pounds)
    = 3.5 + 3.69 + 3.44 + 3.43 + 4.34 + 4.42 + 2.37 / 7 (no.of inputs) = 3.6

Step4: Add the weight with the linear relationship -3.6 (in this example its negative)

Step5: find the  bias or y intercept or slope
y = b+wx 
b = y - wx
substitute all the known values in the equation and get the average 
example: take the first input and output values with the weight
Pounds in 1000s (feature)	Miles per gallon (label)
3.5	                        18

b = 18 - (-3.6)(3.5) = 30.60

like tis find b value for all te provided input and output values with the weight and get the average
for tis example b is 30 

Step6: substitute all the known/calculated values in the equation and get the prediction

y = b + wx
y = 30 + (-3.6)(4) = 15.6 
te predicted Miles per gallon value for a 4000 Pounds car is 15.6


//Anoter way to find bias or y intercept or slope and weight 

step1:  find sum(x),  sum(y), sum(x2), sum(x*y) and n - no.of entries 

Step2: find weight w = n * sum(x*y) - (sum(x) * sum(y))/ n * sum(x2) - (sum(x))2 - power

Step3: find slope b = sum(y) - w * sum(x)/n

------

Evaluate the model: Find loss (difference between actual vs predicted value) 

via 
1. Sum of Squares Error or Sum of Squares Residual Error SSE = sum of all((actual value - predicted value)2)

2. Mean Squares Error MSE = sum of all((actual value - predicted value)2)/n 

Fit and train the model:
After find the errors refit the line and train the model further.  

'''