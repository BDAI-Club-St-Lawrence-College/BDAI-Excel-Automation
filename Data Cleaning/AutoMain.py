import pandas as pd
import numpy as np
from scipy.stats import shapiro
import json
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#Settings
replaceType = 'median' # use 'mean' or 'median' to replace missing values
alpha = 0.05 # variables for statistical Shapiro-Wilk test for normality, as 

###############################################################################
# We don't want the GUI window of tkinter to be appearing on our screen
Tk().withdraw()
  
# Dialog box for selecting the data file
filepath = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print("File path: ", filepath,"\n")

# Import Data - read file and save as dataframe
df = pd.read_csv(filepath)

# save file name wih extension into variable
filename = os.path.basename(filepath)
# remove extension from filename
filename = os.path.splitext(filename)[0]
print("File name: ", filename,"\n")

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

# if number of missing values is less than 5%, replace with mode, otherwise replace with NA
for i in catcols:
    if df[i].isnull().sum()/df.shape[0] < 0.05:
        df[i].fillna(df[i].mode()[0], inplace=True)
        print(i, "has missing values filled with mode")
    else:
        # replace missing values with NA
        df[i].fillna('not_available', inplace=True)
        print(i, "has missing values more than 5%, replaced with 'not_available'")




## 7. Transfer Categorical Columns to Numeric

# pd.get_dummies()

# https://stats.stackexchange.com/questions/411336/how-many-dummy-variables-should-we-include-in-our-multiple-linear-regression-ana

# Rule of Thumb: We should have at least 15 subjects per parameter.
# If using dummies we should detect whether the number of dummies would exceed
# a reasonable number and choose some other method.
# 
# Following code to propose a method of recoding categorical values to numeric 
# values with pd.factorize()


# Using pd.factorize reassign all categorical values to a numeric
# Keep the key-value pairs in a dictionary
# Use the dictionary to replace the categorical values with the numeric values

# Using pd.factorize reassign all categorical values to a numeric
# Keep the key-value pairs in a dictionary

# Instantiate a dictionary to record the recoded values
category_dict = {}

# Loop through columns and apply pd.factorize to each
for i in catcols:
    # Get the unique values in the column and save into dictionary
    category_dict[i] = dict(enumerate(df[i].unique()))
    # Recode the values in the column
    # With sort=True, the uniques will be sorted, and codes will be shuffled so that the relationship is the maintained.
    df[i] = pd.factorize(df[i], sort=True)[0]

## Find a way to assign missing values to '0' ?
## then map all categorical to numeric not '0' ?

# Review the recoded dataframe
print("\nRecoded DataFrame:\n", df.head())

# Print the dictionary of categories
print("\nThe dictionary of categories: \n")
print(json.dumps(category_dict, indent=1))

## Next Step: How to look up dictionary of recoded values, after analysis ?
## Is it possible to add 1 to all factors AND the dictionary, to avoid 0s ?
##      - would adding +1 be necessary or relevant?

# Save the recoded dataframe to a csv file with the name + "Recoded" as the original file
df.to_csv(filename + "_Recoded.csv", index=False)
print("\nRecoded dataframe saved to", filename + "_Recoded.csv", "\n")