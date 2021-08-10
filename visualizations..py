#!/usr/bin/env python
# coding: utf-8

# ### Import pandas & matplotlib



import pandas as pd
import matplotlib.pyplot as plt


# ### Import the data in the CSV file
# You can find the data [here](https://raw.githubusercontent.com/plotly/datasets/master/data.csv). Should have a shape of (150000,11). Use this [resource](https://github.com/plotly/datasets/blob/master/data_dictionary.csv) for context.



df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/data.csv")


# ### Quickly inspect the head



df.head()


# ### Inspect the tail



df.tail()


# ### What is the shape of the DataFrame? Does it correspond to what we expected? 



df.shape # Yes, it corresponds to what we expected.


# ### Do you need to change the index?



# No, we I don't need to change the index.


# ### Missing values?
# You don't need to fill in these missing values, but don't forget that they're there!



df[df.isnull().any(axis=1)]


# ### Out of the 11 features, which are discrete and which are continuous?
# 
# 
# ---
# 
# 

# **Discrete:** SeriousDlqin2yrs, age, NumberOfTime30-59DaysPastDueNotWorse, MonthlyIncome, NumberOfOpenCreditLinesAndLoans, NumberOfTimes90DaysLate, NumberRealEstateLoansOrLines, NumberOfTime60-89DaysPastDueNotWorse and NumberOfDependents. DebtRatio (Can also be discrete).
# 
# **Continuos:** RevolvingUtilizationOfUnsecuredLines, DebtRatio.

# ### Plot each feature with the appropriate visualization

# #### Histograms



df['age'].hist(bins=40);


# #### Bar charts



df['NumberOfDependents'].value_counts().plot(kind='bar');


# #### Scatterplots



df.plot.scatter(x='age', y='NumberOfOpenCreditLinesAndLoans');


# Relationship? 
# 
# ---
# 
# 

# Age of borrower in years compared with Number of Open loans (installment like car loan or mortgage) and Lines of credit (e.g. credit cards).
# People in between 20 to 80 years tend to have more credit lines and open loans.

# #### Boxplots



df.boxplot(column='age', by='NumberOfOpenCreditLinesAndLoans');


# Any outliers?
# 
# 
# ---
# 
# 

# Yes.
