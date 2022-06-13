import pandas as pd
import numpy as np
from scipy.stats import shapiro
import json
import os

#Settings
replaceType = 'median' # use 'mean' or 'median' to replace missing values
alpha = 0.05 # variables for statistical Shapiro-Wilk test for normality, as 

###############################################################################
# Copy paste the filepath of the data file into the following line:
filepath = r"C:\Users\shuai\OneDrive - St. Lawrence College\SLC_Class\BDAI\Data Cleaning\CustSeg.Test.csv"

# Import Data - read csv file and save as dataframe
# if the files is csv format, use pd.read_csv()
if filepath.endswith('.csv'):
    df = pd.read_csv(filepath)
    # check if the files is excel format, use pd.read_excel() to read the first tab of the excel file
elif filepath.endswith('.xlsx'):
    df = pd.read_excel(filepath, sheet_name=0)


# save file name wih extension into variable
filename = os.path.basename(filepath)
# remove extension from filename
filename = os.path.splitext(filename)[0]


#### Create a list of boolean columns
boolcols = []
for i in df.columns:
    if df[i].dtype == "bool":
        boolcols.append(i)

# create a list of boolean columns with missing values
boolcols_missing = []
for i in boolcols:
    if df[i].isnull().sum() > 0:
        boolcols_missing.append(i)

# if number of missing values is less than 5%, replace with mode, otherwise replace with not_available
for i in boolcols_missing:
    if df[i].isnull().sum()/df.shape[0] < 0.05:
        df[i].fillna(df[i].mode()[0], inplace=True)
    else:
        # replace missing values with NA
        df[i].fillna('not_available', inplace=True)


#### Create a list of Numerical columns (int and float (and boolean?))
numcols = []
for i in df.columns:
    if df[i].dtype != "object":
        numcols.append(i)

# create a list of numerical columns with missing values
numcols_missing = []
for i in numcols:
    if df[i].isnull().sum() > 0:
        numcols_missing.append(i)

# check if data volume <5000 or not
if df.shape[0] > 5000:
    # replace missing values with mean or median
    if replaceType == 'mean':
        for i in numcols_missing:
                df[i].fillna(df[i].mean(), inplace=True)
    elif replaceType == 'median':
        for i in numcols_missing:
                df[i].fillna(df[i].median(), inplace=True)
else:
    ## the function to Determine Shapiro-Wilk p-value < alpha with a function:
    def shapiro_check(x, alpha):
        p = shapiro(x).pvalue
        if p > alpha:
            return(False)
        else:
            return(True)

    # if the numerical column is normally distributed, replace missing values with mean, otherwise with median  
    for i in numcols_missing:
        if shapiro_check(df[i], alpha) == False:
            df[i].fillna(df[i].median(), inplace=True)
        else:
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

# create a list of categorical columns with missing values
catcols_missing = []
for i in catcols:
    if df[i].isnull().sum() > 0:
        catcols_missing.append(i)

# if number of missing values is less than 5%, replace with mode, otherwise replace with not_available
for i in catcols_missing:
    if df[i].isnull().sum()/df.shape[0] < 0.05:
        df[i].fillna(df[i].mode()[0], inplace=True)
    else:
        # replace missing values with NA
        df[i].fillna('not_available', inplace=True)