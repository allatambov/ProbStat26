import pandas as pd
import seaborn as sns
from scipy import stats

### PART 01 ###

x = [4, 3, 7, 10, 20, 10, 80]
y = [14, 9, 28, 40, 50, 23, 5]

data = pd.DataFrame({"x" : x, "y" : y})
data

data.plot.scatter(x = "x", y = "y");

print(stats.pearsonr(data["x"], data["y"]))
print(stats.spearmanr(data["x"], data["y"]))

data.iloc[0:5].plot.scatter(x = "x", y = "y");

print(stats.pearsonr(data["x"][0:5], data["y"][0:5]))
print(stats.spearmanr(data["x"][0:5], data["y"][0:5]))

### PART 02 ###

df = pd.read_csv("cities.csv")
df

df.describe()
df.describe(include = "object")

numeric = df.select_dtypes([int, float])
numeric.corr()

sns.heatmap(numeric.corr(), 
            annot = True, 
            cmap = "coolwarm")

pd.plotting.scatter_matrix(numeric, 
                           figsize = (16, 16), 
                           color = "forestgreen",
                           alpha = 1, 
                           hist_kwds = {"edgecolor": "white", 
                                       "color" : "limegreen"});
print(stats.pearsonr(df["Decibel_Level"], 
                     df["Happiness_Score"]))

print(stats.spearmanr(df["Green_Space_Area"], 
                      df["Healthcare_Index"]))

tab = pd.crosstab(df["Region"], df["Traffic_Density"])
tab

print(stats.chi2_contingency(tab))
