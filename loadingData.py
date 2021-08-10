#!/usr/bin/env python
# coding: utf-8

# ### Import pandas with the "pd" alias.



import pandas as pd


# ### Import the data in the CSV file.
# Today you'll be working with some GDP data. You can find the data [here](https://raw.githubusercontent.com/axrd/datasets/master/gdp.csv).



df = pd.read_csv("https://raw.githubusercontent.com/axrd/datasets/master/gdp.csv")


# ### Print out the first 7 rows.



df.head(7)


# ### Print out the last 3 rows.



df.tail(3)


# ### What is the shape of the DataFrame?



df.shape


# ### What is the data type of each column/feature?
# Hint: We didn't cover this, Google it!  
# 
# Hint 2: Columns and features are interchangeable when talking about DataFrames or tabular data in general. 



df.dtypes


# ### Rename the column "Counry" to "Country".



df = df.rename(columns={'COUNRY':'COUNTRY'})


# ### Verify the change persisted!



df.columns


# ### Submit your assignment notebook! (Make sure you've changed the name to FIRSTNAME_LASTNAME_1_2): 
# 
# 1.  Click the Share button in the upper-right hand corner of the notebook.
# 2.  Get the shareable link.
# 3.  Set condition to: "Anyone with the link can comment."
# 4.  TBD 
# 
# 
# 
# ---
# 
# The question below is _optional_. Only tackle it after you've completed the rest of the assignment!

# ### STRETCH: Tying it back to Lesson 01...
# 
# *  What is the max GDP?
# *  Min GDP?
# *  Median GDP?
# *  Standard Deviation of GDP?



# Max GDP:
df.loc[df['GDP (BILLIONS)'].idxmax()]




# Min GDP:
df.loc[df['GDP (BILLIONS)'].idxmin()]




# Median GDP:
print([df['GDP (BILLIONS)'].median()])




# Standard Deviation of GDP:
print([df['GDP (BILLIONS)'].std()])
