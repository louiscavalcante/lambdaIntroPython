#!/usr/bin/env python
# coding: utf-8

# ### Import Numpy, pandas, and matplotlib



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### Import the data in the CSV file
# Today you'll be working with the tips dataset from the lecture. You can find the data [here](https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv). Be careful not to import an extra index column! See the lecture notebook for a workaround.



df = pd.read_csv("https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv", index_col=0)


# ### Print out the first 10 rows



df.head(10)


# ### Print out the last 10 rows



df.tail(10)


# ### What is the shape of the DataFrame?



df.shape


# ### What is the data type of each column/feature?



df.dtypes


# ### Are there any missing values?



df[df.isnull().any(axis=1)] # There are no missing values.


# ### What is the average total bill? Calculate the mean, median, and mode. 



df['total_bill'].mean()




df['total_bill'].median()




df['total_bill'].mode()


# ### Which of the three do you think best represents the data? Why?
# 
# 
# ---
# 
# 

# The mean, because it's the best avarage of a continuous data in a total bill list.

# ### Visualize the distribution of tips. Describe it (skew, kurtosis, etc.).



df['tip'].plot.density(); # Positive Skew.


# ### What is the range of tips? 



df['tip'].describe()




np.var(df['tip'], ddof=1)


# The range of the tips is 1.91 from the min of 1 and the max of 10.

# ### Create a boxplot for tips. See module 6 of the Intro to Pandas lesson for hints. 



df.boxplot(column='tip', by='size');


# ### What was the most common day?



# The most common day is Saturday.
df['day'].value_counts().plot(kind='bar');


# ### What was the most common gender?



# The most common gender is Male.
df['sex'].value_counts().plot(kind='barh');


# ### What is the standard deviation of "tips"?



np.std(df['tip'], ddof=1)


# ### What is the variance of total bill?



np.var(df['total_bill'], ddof=1)


# ### Submit your assignment notebook! (Make sure you've changed the name to FIRSTNAME_LASTNAME_1_2): 
# 
# 1.  Click the Share button in the upper-right hand corner of the notebook.
# 2.  Get the shareable link.
# 3.  Set condition to: "Anyone with the link can comment."
# 4.  TBD 
# 
# 
# ---
# 
# The question below is _optional_. Only tackle it after you've completed the rest of the assignment!

# ### STRETCH: Visualize all the numeric features and describe their distributions.



# Small tips are the most common.
df['tip'].hist();




# Groups of 2 are the most common.
df['size'].hist();




# Small bills are the most common.
df['total_bill'].hist(bins=10);
