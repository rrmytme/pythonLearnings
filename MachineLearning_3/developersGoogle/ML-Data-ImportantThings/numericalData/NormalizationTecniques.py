'''
The goal of normalization is to transform features to be on a similar scale. For example, consider the following two features:

Feature X spans the range 154 to 24,917,482.
Feature Y spans the range 5 to 22.
These two features span very different ranges. Normalization might manipulate X and Y so that they span a similar range, perhaps 0 to 1.

Normalization provides the following benefits:

Helps models converge more quickly during training. When different features have different ranges, gradient descent can "bounce" and slow convergence. That said, more advanced optimizers like Adagrad and Adam protect against this problem by changing the effective learning rate over time.
Helps models infer better predictions. When different features have different ranges, the resulting model might make somewhat less useful predictions.
Helps avoid the "NaN trap" when feature values are very high. NaN is an abbreviation for not a number. When a value in a model exceeds the floating-point precision limit, the system sets the value to NaN instead of a number. When one number in the model becomes a NaN, other numbers in the model also eventually become a NaN.
Helps the model learn appropriate weights for each feature. Without feature scaling, the model pays too much attention to features with wide ranges and not enough attention to features with narrow ranges.

Normalization techniques: scaling and Clipping

1. Linear scaling:
scaled value x' = x - x min/x max - x min
When to use: When the feature is uniformly distributed across a fixed range.
example: Age feature boundaries are 0-100 mostly

2. Z-score scaling:
z-score = x-mean/standard deviation
When to use: When the feature distribution does not contain extreme outliers.
example: height feature does not contain extreme outliers.

3. Log scaling:
x' = log(x) 
When to use: When the feature conforms to the power law.
example: 
Low values of X have very high values of Y.
As the values of X increase, the values of Y quickly decrease. Consequently, high values of X have very low values of Y.

A few movies have lots of user ratings. (Low values of X have high values of Y.)
Most movies have very few user ratings. (High values of X have low values of Y.)

4. Clipping:
is a technique to minimize the influence of extreme outliers. In brief, clipping usually caps (reduces) the value of outliers to a specific maximum value.

if x > max, set x' = max
if x < min, set x' = min

When to use: When the feature contains extreme outliers.
example: temperature min = -10, max = 45 outliers = 70, -20 will be set to 45, -10

'''