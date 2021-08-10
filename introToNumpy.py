#!/usr/bin/env python
# coding: utf-8

# ### Import Numpy as Np



import numpy as np


# ### Generate random numbers
# Create a (5,3) Numpy array of random integer values between 0 and 100.



random_list = np.random.randint(101, size=(5, 3))
random_list


# ### Array practice
# Run each of these in their own code cell and comment it accordingly:
# 
# *  Return the first row
# *  Return the last column
# *  Return the third column values from the 4th and 5th rows
# *  Multiply every value in the array by 2
# *  Divide every value by 3
# *  Increase the values in the first row by 12
# * Calculate the mean of the first column
# * Calculate the median of the array _after_ removing the 2 smallest values in the array
# * Calculate the standard deviation of the first 3 rows
# * Return values in the second column greater than 25
# * Return values in the array under 40



# Return the first row:
random_list[0]




# Return the last column:
random_list[:,-1]




# Return the third column values from the 4th and 5th rows:
random_list[3:5,2]




# Multiply every value in the array by 2:
random_list[:,] * 2




# Divide every value by 3:
random_list[:,] / 3




# Increase the values in the first row by 12:
random_list[0,] + 12




# Calculate the mean of the first column:
np.mean(random_list[:,0])




# Calculate the median of the array after removing the 2 smallest values in the array:
first = random_list
first = np.delete(first, first.argmin())
second = np.delete(first, first.argmin())
median = np.median(second)
print(median)




# Calculate the standard deviation of the first 3 rows:
np.std(random_list[0:3,])




# Return values in the second column greater than 25:
values = random_list[:,1] > 25
random_list[:,1][values]




# Return values in the array under 40:
values = random_list[:,] < 40
random_list[values]
