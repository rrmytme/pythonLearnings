'''
Classification is the task of predicting which of a set of classes 

for example, predicting whether a given email is "spam" or "not spam"?

binary classification 
multi-class classification

Thresholds: based on tis will classify te predictions
for example  Thresholds is 0.5 means any predictions < 0.5 is not a spam and predictions >= 0.5 is spam

confusion matrix: comes with
- Actual positive, Actual negative
- Predicted positive, Predicted negative

Datasets: 
Separated - where positive examples and negative examples are generally well differentiated, with most positive examples having higher scores than negative examples.
Unseparated - where many positive examples have lower scores than negative examples, and many negative examples have higher scores than positive examples.
Imbalanced - containing only a few examples of the positive class.

Accuracy: 
is the proportion of all classifications that were correct, whether positive or negative.

= correct classification/total classification
= true positive + true negative / true positive + true negative + false positive + false negative

Use as a rough indicator of model training progress/convergence for balanced datasets.

For model performance, use only in combination with other metrics.

Avoid for imbalanced datasets. Consider using another metric.

Recall (True positive rate):
is the proportion of all actual positives that were classified correctly as positives

= correctly classified Actual positive/true positive + false negative

Use when false negatives are more expensive than false positives.
example: get all the business mails important then let the spam into inbox


False positive rate (false alarm):
is the proportion of all actual negatives that were classified incorrectly as positives

= false positive/false positive + true negative

Use when false positives are more expensive than false negatives.
example: block all the spams are important then let the business mails into spam

Precision:
is the proportion of all the model's positive classifications that are actually positive.

= true positive/true positive + false positive

Use when it's very important for positive predictions to be accurate.
example: block all the spams are important 

Receiver-operating characteristic curve (ROC):
 is a visual representation of model performance across all thresholds.

 The ROC curve is drawn by calculating the true positive rate (TPR) and false positive rate (FPR) at every possible threshold (in practice, at selected intervals), then graphing TPR over FPR. A perfect model, which at some threshold has a TPR of 1.0 and a FPR of 0.0, can be represented by either a point at (0, 1)

Area under the curve (AUC): 
represents the probability that the model, if given a randomly chosen positive and negative example, will rank the positive higher than the negative.

The perfect model above, containing a square with sides of length 1, has an area under the curve (AUC) of 1.0. This means there is a 100% probability that the model will correctly rank a randomly chosen positive example higher than a randomly chosen negative example.

Prediction bias:
 calculating prediction bias is a quick check that can flag issues with the model or training data early on.

Prediction bias is the difference between the mean of a model's predictions and the mean of ground-truth labels in the data.

Prediction bias can be caused by:

Biases or noise in the data, including biased sampling for the training set
Too-strong regularization, meaning that the model was oversimplified and lost some necessary complexity
Bugs in the model training pipeline
The set of features provided to the model being insufficient for the task

'''