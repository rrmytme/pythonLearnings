
'''
logistic regression that is designed to predict the probability of a given outcome.

ex: "Will it rain today?" or "Is this email spam?"

the results would be 0 to 1 and converted to yes(1 or near to 1) or no(0 or near to 0) 

step1: find the linear equation output 

z = b + wx 

or 

z = b + w1x1 + .... + WnXn  

Step2: Transform linear output using the sigmoid function

substiture z into sigmoid function below,

y = 1/1+e-z (e power z)

Step3: find Log Loss and regularization

-------------------

Logistic regression models are trained using the same process as linear regression models, with two key distinctions:

Logistic regression models use Log Loss as the loss function instead of squared loss.
Applying regularization is critical to prevent overfitting.

'''

import numpy as np

def probabilityCalc(z):
    return (1/(1 + np.exp(-z)))

def logloss(y_true,y_pred):
    log_loss = (-((y_true * np.log10(y_pred)) + (1-y_true) * np.log10(1-y_pred)).mean())
    return log_loss

print(probabilityCalc(1))