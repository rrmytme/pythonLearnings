'''
References: https://developers.google.com/machine-learning/crash-course/categorical-data
Categorical data has a specific set of possible values. 
For example: The different species of animals in a national park

WE should represent features that contain integer values as categorical data instead of numerical data

Encoding: means converting categorical or other data to numerical vectors that a model can train on. This conversion is necessary because models can only train on floating-point values; models can't train on strings such as "dog" or "maple".

Categorical data: Vocabulary and one-hot encoding

The term dimension is a synonym for the number of elements in a feature vector. Some categorical features are low dimensional. For example:

Feature name	# of categories	Sample categories
snowed_today	2	True, False
skill_level	3	Beginner, Practitioner, Expert

Vocabulary: When a categorical feature has a low number of possible categories, you can encode it as a vocabulary. With a vocabulary encoding, the model treats each possible categorical value as a separate feature. During training, the model learns different weights for each category.
For example, suppose you are creating a model to predict a car's price based, in part, on a categorical feature named car_color. 
car_color -> 0 - Red, 1 - green, 2 - Blue  (0,1,2 are indexes to identify a feature category)

One-hot encoding: Machine learning models can only manipulate floating-point numbers. 
Therefore, we must convert each string -> unique index number -> One-hot encoding(feature vector)

Example: 
Feature	    Red	Orange	Blue	Yellow	Green	Black	Purple	Brown
"Red"	    1	0	    0	    0	    0	    0	    0	    0
"Orange"	0	1	    0	    0	    0	    0	    0	    0
"Blue"	    0	0	    1	    0	    0	    0	    0	    0

 Sparse representation: means storing the position of the 1.0 in a sparse vector. 
 For example, 
 1. the one-hot vector for "Blue" is: [0	0  1  0  0  0	0  0] -> 2
 2. The sparse representation of a multi-hot encoding stores the positions of all the nonzero elements. 
 For example, the sparse representation of a car that is both "Blue" and "Orange" is 2, 1.

 Outliers in categorical data: Like numerical data, categorical data also contains outliers. Suppose car_color contains not only the popular colors, but also some rarely used outlier colors, such as "Mauve" or "Avocado". Rather than giving each of these outlier colors a separate category, you can lump them into a single "catch-all" category called out-of-vocabulary (OOV). In other words, all the outlier colors are binned into a single outlier bucket. The system learns a single weight for that outlier bucket.

 Encoding high-dimensional categorical features: use Embeddings.

 Categorical data: Common issues:
 1. Human raters - gold labels, relatively better data quality than machine-labeled data
    possible issues: Human errors, bias, and malice, labeled without standard agreement( inter-rater agreement.)
 2. Machine raters - silver labels, vary widely in quality
    example:  model mislabels a photo of a cookie as a biscuit
 3. High dimensionality - Categorical data tends to produce high-dimensional feature vectors; that is,
   feature vectors having a large number of elements. High dimensionality increases training costs 
   and makes training more difficult. For these reasons, ML experts often seek ways to reduce the 
   number of dimensions prior to training. Possible soln is reducing dimensionality is to 
   convert feature vectors to embedding vectors.

Categorical data: Feature crosses:
Feature crosses are created by crossing (taking the Cartesian product of) two or more categorical or bucketed features of the dataset. Like polynomial transforms, feature crosses allow linear models to handle nonlinearities. 
Feature crosses also encode interactions between features.

For example, consider a leaf dataset with the categorical features:

edges, containing values smooth, toothed, and lobed
arrangement, containing values opposite and alternate

Feature crosses  -> edges * arrangement -> {(1, 0, 0), (1, 0)}

Domain knowledge can suggest a useful combination of features to cross. Without that domain knowledge, it can be difficult to determine effective feature crosses or polynomial transforms by hand. It's often possible, if computationally expensive, to use neural networks to automatically find and apply useful feature combinations during training.

Be careful—crossing two sparse features produces an even sparser new feature than the two original features. For example, if feature A is a 100-element sparse feature and feature B is a 200-element sparse feature, a feature cross of A and B yields a 20,000-element sparse feature.


'''
