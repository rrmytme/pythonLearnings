#Linear regression: 

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
w = the rate of x changes (car pounds mean)
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

In linear regression, there are four main types of loss, which are outlined in the following table.

1. L1 loss:	The sum of the absolute values of the difference between the predicted values and 
the actual values = sum (actual value - predicted value)

2. Mean absolute error (MAE)	The average of L1 losses across a set of examples.	
= sum (actual value - predicted value)/n (no.of examples)

3. L2 loss	The sum of the squared difference between the predicted values and the actual values.
Sum of Squares Error or Sum of Squares Residual Error SSE = sum of all((actual value - predicted value)2)

4. Mean squared error (MSE)	The average of L2 losses across a set of examples.	
Mean Squares Error MSE = sum of all((actual value - predicted value)2)/n 

Deciding whether to use MAE or MSE can depend on the dataset and the way you want to handle certain predictions.

MSE: The model is closer to the outliers but further away from most of the other data points.

MAE: The model is further away from the outliers but closer to most of the other data points.

----------------
Gradient descent - please refer pythonLearnings\MachineLearning_3\developersGoogle\gradientDecent\gradientDecent_3.py
----------------

Hyperparameters: are variables that control different aspects of training. 
hyperparameters are values that you control

types:
1. Learning rate - is a floating point number you set that influences how quickly the model converges. 
If the learning rate is too low, the model can take a long time to converge. However, 
if the learning rate is too high, the model never converges, but instead bounces around the weights 
and bias that minimize the loss.
Doubling the learning rate can result in a learning rate that is too large, and therefore cause the 
weights to "bounce around," increasing the amount of time needed to converge. As always, the best 
hyperparameters depend on your dataset and available compute resources.

2. Batch size - is the number of examples the model processes before updating its weights and bias.
Two common techniques to get the right gradient on average without needing to look at every example 
in the dataset before updating the weights and bias are,
    2.1. stochastic gradient descent - a batch size of one per iteration. stochastic gradient descent 
    can produce noise throughout the entire loss curve, not just near convergence

    2.2 mini-batch stochastic gradient descent - is a compromise between full-batch and SGD. For 
    number of data points, the batch size can be any number greater than 1 and less than N
.   The model chooses the examples included in each batch at random, averages their gradients, 
    and then updates the weights and bias once per iteration.

3. Epochs - means that the model has processed every example in the training set once.
    For example, given a training set with 1,000 examples and a mini-batch size of 100 examples, 
    it will take the model 10 iterations to complete one epoch.

    Batch type	                                When weights and bias updates occur
    Full batch	                                After the model looks at all the examples in the dataset. For instance, if a dataset contains 1,000 examples and the model trains for 20 epochs, the model updates the weights and bias 20 times, once per epoch.
    Stochastic gradient descent	                After the model looks at a single example from the dataset. For instance, if a dataset contains 1,000 examples and trains for 20 epochs, the model updates the weights and bias 20,000 times.
    Mini-batch stochastic gradient descent	    After the model looks at the examples in each batch. For instance, if a dataset contains 1,000 examples, and the batch size is 100, and the model trains for 20 epochs, the model updates the weights and bias 200 times.
'''