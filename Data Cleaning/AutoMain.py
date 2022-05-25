import pandas as pd
import numpy as np
from scipy.stats import shapiro

# read Excel file
df = pd.read_csv (r"CustSeg.Train.csv")
df.head()

# Define Variables
alpha = 0.05  # for statistical Shapiro-Wilk test for normality

##########
# Create a list of Numerical columns (int and float (and boolean?))
numcols = []
for i in df.columns:
    if df[i].dtype != "object":
        numcols.append(i)
numcols

## the function to Determine Shapiro-Wilk p-value < alpha with a function:

def shapiro_check(x, alpha):
    p = shapiro(x).pvalue
    if p > alpha:
        return(False)
    else:
        return(True)

# Run Shapiro test to each column
for col in numcols


#########
# Create a list of Categorical columns
catcols = []
for i in df.columns:
    if df[i].dtype == "object":
        catcols.append(i)
catcols

# Replace NA in categorical columns to mode
for i in catcols:
    df[i].fillna(df[i].mode, inplace = True)