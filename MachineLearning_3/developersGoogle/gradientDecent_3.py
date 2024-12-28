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

Please refer the gradientDecentCode.py  
'''