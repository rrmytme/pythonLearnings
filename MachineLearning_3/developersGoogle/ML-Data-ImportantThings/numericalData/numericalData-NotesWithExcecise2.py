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
from matplotlib import pyplot as plt
import io
from plottingFunctions import plot_the_dataset, plot_a_contiguous_portion_of_dataset 

# The following lines adjust the granularity of reporting.
pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.1f}".format

dataset = ''' 
calories,test_score
254,71
153,69
167,73
162,70
39,61
295,84
12,52
262,73
351,80
253,73
381,97
2,47
55,62
45,54
54,48
92,64
183,72
226,81
265,85
313,86
383,89
215,80
31,49
178,60
238,68
173,68'''

# Import the dataset
training_df = pd.read_csv(io.StringIO(dataset), on_bad_lines='warn')

# Get basic statistics:
training_df.describe()

# Identify possible outliers
print("""The basic statistics do not suggest a lot of outliers.
The standard deviations are substantially less than the
means. Furthermore, the quartile boundaries are approximately
evenly spaced.""")


# Visualize the dataset
plot_the_dataset("calories", "test_score", number_of_points_to_plot=50)

print("""Visualizing 50 data points doesn't imply any outliers.
However, as you increase the number of random data points to plot, a
clump of outliers appears. Notice the points with high test scores but less
than 200 calories.""")

#Step4: get statistics with random weekly data:
# Get statistics on Week 0
training_df[0:349].describe()
# Get statistics on Week 1
training_df[350:699].describe()
# Get statistics on Week 2
training_df[700:1049].describe()
# Get statistics on Week 3
training_df[1050:1399].describe()

print("""The basic statistics for each week are pretty similar, so weekly
differences aren't a likely explanation for the outliers.""")

#Step4: get statistics with random daily data:
for i in range(0,7):
  start = i * 50
  end = start + 49
  print("\nDay %d" % i)
  plot_a_contiguous_portion_of_dataset("calories", "test_score", start, end)

  print("""Wait a second--the calories value for Day 4 spans 0 to 200, while the
calories value for all the other Days spans 0 to 400. Something is wrong
with Day 4, at least on the first week.""")
  
#Step5: Use statistics to confirm your suspicions
# You could use a variety of metrics to fully compare Thursday to the other
# six days, but this answer simply focuses on the mean.

running_total_of_thursday_calories = 0
running_total_of_non_thursday_calories = 0
count = 0
for week in range(0,4):
  for day in range(0,7):
    for subject in range(0,50):
      position = (week * 350) + (day * 50) + subject
      if (day == 4):  # Thursday
        running_total_of_thursday_calories += training_df['calories'][position]
      else:  # Any day except Thursday
        count += 1
        running_total_of_non_thursday_calories += training_df['calories'][position]

mean_of_thursday_calories = running_total_of_thursday_calories / 200
mean_of_non_thursday_calories = running_total_of_non_thursday_calories / 1200

print("The mean of Thursday calories is %.0f" % (mean_of_thursday_calories))
print("The mean of calories on days other than Thursday is %.0f" % (mean_of_non_thursday_calories))  

'''
Output is, Thursday data is outlier
The mean of Thursday calories is 93
The mean of calories on days other than Thursday is 201
'''
