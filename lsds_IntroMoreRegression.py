#!/usr/bin/env python
# coding: utf-8

# ## Assignment
# 
# ### 1. Experiment with Nearest Neighbor parameter
# 
# Using the same 10 training data points from the lesson, train a `KNeighborsRegressor` model with `n_neighbors=1`.
# 
# Use both `carat` and `cut` features.
# 
# Calculate the mean absolute error on the training data and on the test data.



get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

columns = ['carat', 'cut', 'price']

train = pd.DataFrame(columns=columns, 
        data=[[0.3, 'Ideal', 422],
        [0.31, 'Ideal', 489],
        [0.42, 'Premium', 737],
        [0.5, 'Ideal', 1415],
        [0.51, 'Premium', 1177],
        [0.7, 'Fair', 1865],
        [0.73, 'Fair', 2351],
        [1.01, 'Good', 3768],
        [1.18, 'Very Good', 3965],
        [1.18, 'Ideal', 4838]])

test  = pd.DataFrame(columns=columns, 
        data=[[0.3, 'Ideal', 432],
        [0.34, 'Ideal', 687],
        [0.37, 'Premium', 1124],
        [0.4, 'Good', 720],
        [0.51, 'Ideal', 1397],
        [0.51, 'Very Good', 1284],
        [0.59, 'Ideal', 1437],
        [0.7, 'Ideal', 3419],
        [0.9, 'Premium', 3484],
        [0.9, 'Fair', 2964]])

cut_ranks = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
train.cut = train.cut.map(cut_ranks)
test.cut = test.cut.map(cut_ranks)







# How does the train error and test error compare to the previous `KNeighborsRegressor` model from the lesson? (The previous model used `n_neighbors=2` and only the `carat` feature.)
# 
# Is this new model overfitting or underfitting? Why do you think this is happening here? 
# 
# 

# ### 2. More data, two features, linear regression
# 
# Use the following code to load data for diamonds under $5,000, and split the data into train and test sets. The training data has almost 30,000 rows, and the test data has almost 10,000 rows.



import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = sns.load_dataset('diamonds')
df = df[df.price < 5000]
train, test = train_test_split(df.copy(), random_state=0)
train.shape, test.shape


# Then, train a Linear Regression model with the `carat` and `cut` features. Calculate the mean absolute error on the training data and on the test data.






# Use this model to predict the price of a half carat diamond with "very good" cut






# ### 3. More data, more features, any model

# You choose what features and model type to use! Try to get a better mean absolute error on the test set than your model from the last question.

# Refer to [this documentation](https://ggplot2.tidyverse.org/reference/diamonds.html) for more explanation of the features.
# 
# Besides `cut`, there are two more ordinal features, which you'd need to encode as numbers if you want to use in your model:



train.describe(include=['object'])




clarity_rank = {"IF":0,"VVS1":1, "VVS2":2,"VS1":3, "VS2":4,"SI1":5, "SI2":6, "I1":7}
train.clarity = train.clarity.map(clarity_rank)  

color_rank = {"J":7, "I":6, "H":5, "G":4, "F":3, "E":2, "D":1 }
train.color = train.color.map(color_rank)

features = ['color','clarity']
target = ['price']
model = LinearRegression()
model.fit(train[features],train[target])
mean_abs_error()
model.coef_,model.intercept_
