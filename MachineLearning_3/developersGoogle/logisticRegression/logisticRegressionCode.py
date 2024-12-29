

df = pd.read_csv("D:/myProjects/pythonLearnings/MachineLearning_3/developersGoogle/logisticRegression/insurance_data.csv")
df.head()

plt.scatter(df.age,df.bought_insurance,marker='+',color='red')