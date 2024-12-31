'''
Binning (also called bucketing):
 is a feature engineering technique that groups different numerical subranges into bins or buckets. In many cases, binning turns numerical data into categorical data. For example, consider a feature named X whose lowest value is 15 and highest value is 425. Using binning, you could represent X with the following five bins:

Bin number	Range	Feature vector
1	15-34	[1.0, 0.0, 0.0, 0.0, 0.0]
2	35-117	[0.0, 1.0, 0.0, 0.0, 0.0]
3	118-279	[0.0, 0.0, 1.0, 0.0, 0.0]
4	280-392	[0.0, 0.0, 0.0, 1.0, 0.0]
5	393-425	[0.0, 0.0, 0.0, 0.0, 1.0]

Binning is a good alternative to scaling or clipping when either of the following conditions is met:

1. The overall linear relationship between the feature and the label is weak or nonexistent.
2. When the feature values are clustered.

Quantile bucketing:
 creates bucketing boundaries such that the number of examples in each bucket is exactly or nearly equal. Quantile bucketing mostly hides the outliers

Example: consider the equally spaced buckets, where each of the ten buckets represents a span of 
exactly 10,000 dollars. Notice that the bucket from 0 to 10,000 contains dozens of examples but the 
bucket from 50,000 to 60,000 contains only 5 examples. Consequently, the model has enough examples 
to train on the 0 to 10,000 bucket but not enough examples to train on for the 50,000 to 60,000 bucket.

to address it, we uses quantile bucketing to divide car prices into bins with approximately the same 
number of examples in each bucket. Notice that some of the bins encompass a narrow price span while 
others encompass a very wide price span. 
'''