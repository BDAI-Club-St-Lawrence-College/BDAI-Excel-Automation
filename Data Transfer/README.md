## Data Transfer
Here stores the excel files, python scripts for developing the project's data merge/verify/transfer feature.   
The CSV data files used for testing the codes were created by Xiuhao Shuai for club practice purposes.

# Current proposed features
1. Merge the excel file "Attendance" with "Contract"  
   -- based on the same Name + Contract Type  
2. Filter out the rows with mistaken inputs  
 -- working "Date" in "Attendance.xlsx" should be within the range between "StartDate" and "EndDate" in "Contract.xlsx"  
3. Calculate how much the company should pay for each month (based on the correct records)  
_________________
Question want to solve:  
Create a consolidated excel record of how much the company should pay to who on what day. Also, extract any rows of inputs with errors/mistakes.  

# Data Structure  
"Attendance.xlsx"   
an excel file that records employee's attendance on their workday  
ID - unique transaction ID  
Name- Employee name  
ContractType - 3 different types of contract: A, B, C  
Date - the date when the employee was working  
StartTime - working start time  
EndTime - working end time  

"Contract.xlsx"  
an excel file that records each employee's contract and hourly pay for that specific contract type  
Name - Employee name  
Type - 3 different types of contract: A, B, C  
StartDate - Contract start date  
EndDate - Contract end date  
HourlyPay - hourly pay to the employee  
_________________
# BDAI-Automation

This project was started by the Big Data and Artificial Intelligence Club at St. Lawrence College (Kingston Campus) in May 2022.

The project aims to create a _python script_ for automation purposes in **cleaning, formatting and transforming** the __CSV or Excel files__ to be used directly and efficiently in __data visualization softwares__ like PowerBi.

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
