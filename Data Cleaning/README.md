## Data Cleaning
Here stores the _files, python scripts and online data sources_ for developing the __data cleaning feature__ of the project.   
The CSV data files used for testing the codes are downloaded from Kaggle: https://www.kaggle.com/datasets/kaushiksuresh147/customer-segmentation for education purposes. The 'train.csv' file is used to test the codes on missing values.

# Current proposed Features
0: pick the csv file you want to read from explorer  
1: read csv file as a dataframe  
2. pick up the numeric columns and non-numeric columns  
3. whether the numeric columns is normally distributed  
3. if normally distributed, fill with mean; if not, fill with median  
4. search the conditional to fill categorical columns with mode or "not available".  
5. re-check the count of missing values == 0  
6. transfer categorical columns into numeric columns  ; if dictionary file exists, use dictionary  
7. Export cleaned and transformed file as "name_Recoded.csv"  
8. Export the dictionary used for transforming Categorical-to-Numerical values, and save locally as [filename]__category_dict.json  

_________________
# BDAI-Automation

This is a project started by the Big Data and Artificial Intelligence Club at the St. Lawrence College (Kingston Campus) in May 2022.

The project aims to create a _python script_ for automation purposes in **cleaning, formating, and transforming** the __CSV or Excel files__ to be used directly and efficiently in __data visualization softwares__ like PowerBi.

# Project Team Members:
*Lead*: Xiuhao Shuai  
*Team*:  
Donovan Bangs  
Hennadii Korolevych  
Yali Liu  
Isabel Grau  

# Thx for joining us!
BDAI Club linked-in page: https://www.linkedin.com/company/bdaic/  
Location:  
St Lawrence College
100 Portsmouth Avenue, Kingston, Ontario K7L5A6, CA

Time: May 25th, 2022
