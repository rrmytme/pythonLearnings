'''
A dataset:

is a collection of examples 
stores in database tables, csv, excel..
Rows ->  examples
Columns -> features and Lables (inputs and outputs)

Types of data:
A dataset could contain many kinds of datatypes, including but certainly not limited to:

numerical data - integers and float values with sign (1, 1.5, -100, 230.1212)
categorical data - a specific set of possible values (different species of animals in a national park)
human language, including individual words and sentences, all the way up to entire text documents
multimedia (such as images, videos, and audio files)
outputs from other ML systems
embedding vectors, which are covered in a later unit

Quantity of data:
Models trained on large datasets with few features generally outperform models trained on small 
datasets with a lot of features.

It's possible to get good results from a small dataset if you are adapting an existing model already 
trained on large quantities of data from the same schema.

Quality and reliability of data:
references: https://developers.google.com/machine-learning/crash-course/overfitting/data-characteristics#quality_and_reliability_of_data

A high-quality dataset helps your model accomplish its goal.

A high-quality dataset is usually also reliable. Reliability refers to the degree to which you can trust your data.

The following are common causes of unreliable data in datasets:

Omitted values. For example, a person forgot to enter a value for a house's age.
Duplicate examples. For example, a server mistakenly uploaded the same log entries twice.
Bad feature values. For example, someone typed an extra digit, or a thermometer was left out in the sun.
Bad labels. For example, a person mistakenly labeled a picture of an oak tree as a maple tree.
Bad sections of data. For example, a certain feature is very reliable, except for that one day when the network kept crashing.
We recommend using automation to flag unreliable data. For example, unit tests that define or rely on an external formal data schema can flag values that fall outside of a defined range.

Complete vs. incomplete examples:
complete: each example contains a value for each feature.
incomplete: meaning that at least one feature value is missing.
delete the incomplete or 
Imputation : fill the missed feature with well-reasoned data, good imputation can improve your model; bad imputation can hurt your model.

Direct versus proxy labels:
Direct labels: which are labels identical to the prediction your model is trying to make. 
For example, a column named bicycle owner would be a direct label for a binary classification model that predicts whether or not a person owns a bicycle.

Proxy labels, which are labels that are similar—but not identical—to the prediction your model is 
trying to make. For example, a person subscribing to Bicycle Bizarre magazine probably—but not definitely—owns a bicycle.

Direct labels are generally better than proxy labels.

Human-generated data: https://developers.google.com/machine-learning/crash-course/overfitting/labels#human-generated_data

Imbalanced datasets:
balanced datasets - All the examples are equally quantified (ex: 50% positive and 50% negative) 
Imbalanced datasets - All the examples are not equally quantified (ex: 10% positive and 90% negative)

mildly imbalanced and some moderately imbalanced datasets, imbalance isn't a problem. So, you should first try training on the original dataset. If the model works well, you're done.

One way to handle an imbalanced dataset is to downsample and upweight the majority class.

Downsampling and Upweighting:
Downsampling (in this context) means training on a subset of the majority class 
(ex: instead of 90% negative will go with 10% negative)
Upweighting means adding an example weight to the downsampled class equal to the factor by which you downsampled.
ex: example weight = oriinal example weight * Downsampling factor
    example weight = 1 * 10
The term weight doesn't refer to model parameters (like, w1 or w2). Here, weight refers to example weights, which increases the importance of an individual example during training.

Rebalance ratios:

 downsample and upweight depends on,

 The batch size
The imbalance ratio
The number of examples in the training set

Dividing the original dataset:
original dataset -> training set + validation set + test set
Note: When you transform a feature in your training set, you must make the same transformation in the validation set, test set, and real-world dataset.

In summary, a good test set or validation set meets all of the following criteria:

Large enough to yield statistically significant testing results.
Representative of the dataset as a whole. In other words, don't pick a test set with different characteristics than the training set.
Representative of the real-world data that the model will encounter as part of its business purpose.
Zero examples duplicated in the training set.

Transforming data:
Machine learning models can only train on floating-point values. However, many dataset features 
are not naturally floating-point values. Therefore, 

1. one important part of machine learning is transforming non-floating-point features to 
floating-point representations.
example: transform "street names" to a floating-point number.
2. converts floating-point numbers to a constrained range
example: normalize big numeric number 100002332 to 0.45 using  normalization methods

Overfitting: overfit model makes excellent predictions on the training set but poor predictions on new data
Underfitting: Underfit model doesn't even make good predictions on the training data.

causes of overfitting:
1. The training set doesn't adequately represent real life data (or the validation set or test set).
2. The model is too complex.

Detecting overfitting: The following curves help you detect overfitting,
loss curves:  plots a model's loss against the number of training iterations. 
generalization curves: A graph that shows two or more loss curves is called a generalization curve. 
example: loss curve1 - training data, loss curve1 - validation data

Generalization: is a process of identify and reduce overfitting.

Generalization conditions:
1. Examples must be independently and identically distributed, which is a fancy way of saying that your examples can't influence each other.
2. The dataset is stationary, meaning the dataset doesn't change significantly over time.
3. The dataset partitions have the same distribution. That is, the examples in the training set are statistically similar to the examples in the validation set, test set, and real-world data.

feedback loop: a situation in which a model's predictions influence the training data for the same 
model or another model. For example, a model that recommends movies will influence the movies that 
people see, which will then influence subsequent movie recommendation models.

simple vs complex model: The simple model generalizes better than the complex model on new data. That is, the simple model made better predictions on the test set than the complex model.

Regularization: is a process of reduce complexity

Fit data well.
Fit data as simply as possible.

-> minimize(loss + complexity)

Complexity: measured via  model's weights(L1 Regularization) or square of themodel's weights (L2 Regularization).

L2 regularization:

L2 regularization = (w1)2+(w2)2+...+(Wn)2

1. L2 regularization encourages weights towards 0, the overall complexity will probably drop.
2. L2 regularization never pushes weights all the way to zero.

Regularization rate (lambda):

minimize(loss + lambda * complexity)

A high regularization rate:

Strengthens the influence of regularization, thereby reducing the chances of overfitting.
Tends to produce a histogram of model weights having the following characteristics:
a normal distribution
a mean weight of 0.

A low regularization rate:

Lowers the influence of regularization, thereby increasing the chances of overfitting.
Tends to produce a histogram of model weights with a flat distribution.

Early stopping is a regularization method that doesn't involve a calculation of complexity. 
Instead, early stopping simply means ending training before the model fully converges. 
For example, you end training when the loss curve for the validation set starts to increase 
(slope becomes positive).

Our goal is to find the equilibrium between learning rate and regularization rate.

Interpreting loss curves:
1. Ideal loss curve (please refer the attached Ideal loss curve image)
2. Oscillating loss curve: it happens because of,
    bad examples - Check your data against a data schema to detect bad examples, and then remove the bad examples from the training set.
    high learning rate - reducing learning rate is often a good idea when debugging a training problem.
    untrustworthy examples: Although this technique sounds artificial, it is actually a good idea. Assuming that the model converges on the small set of trustworthy examples, you can then gradually add more examples, perhaps discovering which examples cause the loss curve to oscillate.
  (please refer the attached Oscillating loss curve image)  
3. Loss curve with a sharp jump: it happens because of, 
    The input data contains a burst of outliers.
    The input data contains one or more NaNs—for example, a value caused by a division by zero.
    (please refer the attached Loss curve with a sharp jump image) 
4. Test loss diverges from training loss: it happens because of, The model is overfitting the training set.
   Possible solutions:
    Make the model simpler, possibly by reducing the number of features.
    Increase the regularization rate.
    Ensure that the training set and test set are statistically equivalent.
    (please refer the attached Test loss diverges from training loss image) 
5. Loss curve gets stuck: it happens because of,     
    The training set contains repetitive sequences of examples. we need to Ensure that we are 
    shuffling examples sufficiently.
    (please refer the attached Loss curve gets stuck image)

'''