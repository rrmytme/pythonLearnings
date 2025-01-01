#GradientDecent: 

'''
References: https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent

the impacting factors of a model's efficiency is the parameters used in a model oter than the feature and label

For ex: on Linear regression model the bias and weight are impacts directly of the models efficiency hence we need to 
adjust them to have low level loss so that the model will be converged.

Gradient descent: is a mathematical technique that iteratively finds the weights and bias that produce the model with the lowest loss. Gradient descent finds the best weight and bias by repeating the following process for a number of user-defined iterations.

The model begins training with randomized weights and biases near zero, and then repeats the following steps:

1. Calculate the loss with the current weight and bias.

2. Determine the direction to move the weights and bias that reduce loss.

3. Move the weight and bias values a small amount in the direction that reduces loss.

4. Return to step one and repeat the process until the model can't reduce the loss any further.

Step1: set the weight and bias to zero

Example:
Pounds in 1000s (feature)	Miles per gallon (label)
3.5	                            18
3.69	                        15
3.44	                        18
3.43	                        16
4.34	                        15
4.42	                        14
2.37	                        24

here y' = b + w1x1 => 0 + 0(x1)

Step2: Calculate MSE loss with the current model parameters
Loss = sum ((actual value - predicted value)2)/n 
     = ((18-0)2+(15-0)2+(18-0)2+(16-0)2+(15-0)2+(14-0)2+(24-0)2)7
     = 303.71

Step3: find derived weight
derived weight md = -(2/n)*sum(x*(y-y_predicted))   
                      = -(2/7)* 419.02
                      = -119.7

Step3: find derived bias
derived bias bd = -(2/n)*sum(y-y_predicted)   
                      = -(2/7)* 120
                      = -34.3

Step4: Move a small amount in the direction of the negative slope to get the next weight and bias. 
For now, we'll arbitrarily define the "small amount" as 0.01:  

new weight = old weight - (small amount * derived weight)
           = 0 - (0.01 * -119.7) 
           = 1.2

new bias = old bias - (small amount * derived bias)
           = 0 - (0.01 * -34.3) 
           = 0.34

Step5: repeat the steps until the loss is very low or model is converge.             

Please refer the gradientDecentCode.py  
'''