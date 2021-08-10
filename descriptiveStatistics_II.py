#!/usr/bin/env python
# coding: utf-8

# ### Import Numpy, pandas, and matplotlib



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### Import the data in the CSV file
# Today you'll be working with the tips dataset from the lecture. You can find the data [here](https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv). 



df = pd.read_csv("https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv", index_col=0)


# ### Print out the first 10 rows



df.head(10)


# ### Print out the last 10 rows



df.tail(10)


# ### Examine total bill and tip to identify any correlation. Calculate the correlation coefficient, AND plot both features as a scatterplot.



# The relationship is positive and somewhat strong. The relationship have a strong variability.
total_bill_vs_tip = df.plot.scatter(x='total_bill', y='tip') and df['total_bill'].corr(df['tip'])
print(total_bill_vs_tip)


# ### Examine size and total bill to identify any correlation. Calculate the correlation coefficient, AND plot both features as a scatterplot.



# The relationship is positive and somewhat strong. It's not a linear relationship.
size_vs_total_bill = df.plot.scatter(x='size', y='total_bill') and df['size'].corr(df['total_bill'])
print(size_vs_total_bill)


# ### Examine size and tip to identify any correlation. Calculate the correlation coefficient, AND plot both features as a scatterplot.



# The relationship is positive and not so strong. It's not a linear relationship.
size_vs_tip = df.plot.scatter(x='size', y='tip') and df['size'].corr(df['tip'])
print(size_vs_tip)


# ### Explain *correlation* in your own words. Please limit your response to three sentences.
# 
# 
# ---
# 
# 

# Correlation explains how two variables relates to one another. This relationship doesn't mean that some correlation is absolute, it could be influence of some other external factor or just a coincidence.
