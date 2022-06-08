import pandas as pd
import numpy as np
from scipy.stats import shapiro
import json

#Settings
replaceType = 'median' # use 'mean' or 'median' to replace missing values
alpha = 0.05 # variables for statistical Shapiro-Wilk test for normality

###############################################################################
# Import Data - read file
df = pd.read_csv (r"CustSeg.Train.csv")

# print info of data
print(df.info())
print(df.head())
# print number of missing values
print("Number of missing values:")
print(df.isnull().sum(), "\n")

# Create a list of Numerical columns (int and float (and boolean?))
numcols = []
for i in df.columns:
    if df[i].dtype != "object":
        numcols.append(i)

# check if data volume <5000 or not
if df.shape[0] > 5000:
    print("Data volume is too large, missing values will be replaced with mean or median automically:" , replaceType, "\n")
    # replace missing values with mean or median
    if replaceType == 'mean':
        for i in numcols:
                df[i].fillna(df[i].mean(), inplace=True)
    elif replaceType == 'median':
        for i in numcols:
                df[i].fillna(df[i].median(), inplace=True)
else:
    print("Data volume is", df.shape[0],", missing values will be replaced with mean or median based on statistical Shapiro-Wilk test for normality", "\n")

    ## the function to Determine Shapiro-Wilk p-value < alpha with a function:
    def shapiro_check(x, alpha):
        p = shapiro(x).pvalue
        if p > alpha:
            return(False)
        else:
            return(True)

    # if the numerical column is normally distributed, replace missing values with mean, otherwise with median  
    for i in numcols:
        if shapiro_check(df[i], alpha) == False:
            print(i, "is not normally distributed, filled with median")
            df[i].fillna(df[i].median(), inplace=True)
        else:
            print(i, "is normally distributed, filled with mean")
            df[i].fillna(df[i].mean(), inplace=True)


#########
# Create a list of Categorical columns
catcols = []
for i in df.columns:
    if df[i].dtype == "object":
        catcols.append(i)

# if column contains only one unique value, drop it
for i in catcols:
    if len(df[i].unique()) == 1:
        df.drop(i, axis=1, inplace=True)
        print(i, "is dropped because it contains only one unique value")

# if number of missing values is less than 5%, replace with mode, otherwise do nothing
for i in catcols:
    if df[i].isnull().sum()/df.shape[0] < 0.05:
        df[i].fillna(df[i].mode()[0], inplace=True)
        print(i, "has missing values filled with mode")
    else:
        print(i, "has missing values more than 5%, do nothing")


## Using pd.factorize reassign all categorical values to a numeric
## Keep the key-value pairs in a dictionary
## Use the dictionary to replace the categorical values with the numeric values

## Subset Just Categorical Columns - DataFrame
#categoricals = df[catcols]
#categoricals.head()

## Using pd.factorize reassign all categorical values to a numeric
## Keep the key-value pairs in a dictionary

# Instantiate a dictionary to record the recoded values
category_dict = {}

# Loop through columns and apply pd.factorize to each
for column in df[catcols]:
    df[column] = dict(enumerate(df[column].unique()))
    df[column] = pd.factorize(df[column],axis=1)[0]

## Find a way to assign missing values to '0' ?
## then map all categorical to numeric not '0' ?

# Review the recoded dataframe
print("\nRecoded DataFrame:\n", df.head())

# Print the dictionary of categories
print("\nThe dictionary of categories: \n")
print(json.dumps(category_dict, indent=4, sort_keys=True))

## Next Step: How to look up dictionary of recoded values, after analysis ?
## Is it possible to add 1 to all factors AND the dictionary, to avoid 0s ?
##      - would adding +1 be necessary or relevant?

print(df[catcols][ 0:10])
