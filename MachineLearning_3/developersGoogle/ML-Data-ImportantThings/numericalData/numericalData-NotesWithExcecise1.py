'''
Step1: Visualize your data in plots or graphs. (scatter or histograms)

Step2: Evaluate potential features and labels mathematically.

Get basic statistics:

count - is the number of populated elements in this column. Ideally, every column contains the same value for count, but that's not always the case.
mean - is the traditional average of values in that column. We recommend comparing the mean to the median for each column. The median is the 50% row of the table.
std - is the standard deviation of the values in this column.
min, 25%, 50%, 75%, and max - indicate values in the 0, 25, 50, 75, and 100th percentiles.

Step3: Find outliers in the dataset.

'''
import pandas as pd

# The following lines adjust the granularity of reporting.
pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.1f}".format

# Import the dataset
training_df = pd.read_csv(filepath_or_buffer="https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv")

# Get basic statistics:
training_df.describe()

# Identify possible outliers
'''
print("""The following columns might contain outliers:

  * total_rooms
  * total_bedrooms
  * population
  * households
  * possibly, median_income

In all of those columns:

  * the standard deviation is almost as high as the mean
  * the delta between 75% and max is much higher than the
      delta between min and 25%.""")
'''