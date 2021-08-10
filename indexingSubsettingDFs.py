#!/usr/bin/env python
# coding: utf-8
 

# ### Import pandas



import pandas as pd


# ### Read in your data
# Your dataset can be found [here.](https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv)
# Import it and return the first 5 rows:



df = pd.read_csv('https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv')
df.head(5)


# ### What is the shape of the DataFrame?



df.shape


# ### Get specific values



# What is the gender of the server in the 41st entry?
df.iloc[41][3]




# Was the 22nd entry seated in a smoking section?
df.loc[22]['smoker']


# ### Get a range of values



# Return the last 20 entries.
df.tail(20)




# Return entries 25 through 50.
df.iloc[25:51,:]


# ### Filtering and subsetting:



# Return all the entries where the size is greater than 2.
condition = df.loc[0:]['size'] > 2
df[condition]




# Create a DataFrame consisting only of data for Fridays. 
# Hint: You should have 19 values.
data = df.loc[0:]['day'] == 'Fri'
df[data]
