#!/usr/bin/env python
# coding: utf-8

# ## Part 1: Functions
# 

# ### Built-in functions
# 
# 
# ---
# 
# 
# Make sure to run the cell below before beginning your assignment.



x = ["a", "b", "c", "d", "e", "f"]


# ### 1.1 For the list of values provided:
# 
# 
# *   Max?
# *   Min?
# *   Number of elements in the list?
# *   Sort the list in _descending_ order.
# 
# 



max(x)




min(x)




len(x)




sorted(x, reverse = True)


# ### Methods
# 
# 
# ---
# 
# 

# ### 1.2 Using the same list:
# 
# *  Remove the second to last element. 
# *  Add the letter "z" to the list.
# *  Empty out the list.
# 



def solution(list_x):
  for i, val in enumerate(x[1:]):
    x.remove(val)
  print(x, "<- Removed the second to last element.")
  x.append("z")
  print(x, "<- Added the letter 'z' to the list.")
  for i, val in enumerate(x[0:]):
    x.remove(val)
  print(x, "<- List emptied out.")

solution(x)


# ### 1.3 For the string provided:
# 
# * Capitalize the entire string.
# * Split the string at every empty space.



y = "to thine own self be true, and it must follow, as the night the day, thou canst not then be false to any man."
cap = y.upper()
split = cap.split()
print(split)


# ### Custom Functions
# 
# 
# ---
# 
# 

# ### 1.4 Create a function that returns the sum of two numbers.



def the_sum(first_number, second_number):
  total = first_number + second_number
  return total

the_sum(2, 3)


# ### 1.5 Create a function that, given a list of numbers, returns their average.



data = [52,44,33,70,61,53,71,84,92,21,55,32,19]

def mean(number_list):
  total = 0
  for numbers in number_list:
    total += numbers
    avarage = round(total / len(number_list),2)
  return avarage

mean(data)


# ### 1.6 Create a function that, given a string, returns that string capitalized and reversed. 



def frase(frase_data):
  frase_CAP = frase_data.upper()
  reversing = frase_CAP[::-1]
  print(reversing)
  
frase("I like programming")


# ### 1.7 Create a function that, given a list of strings, concatenates them together with proper spacing.



def frase(frase_data):
  joining = ' '.join(frase_data)
  return joining

str_list = ["Have", "a", "great", "day"]
frase(str_list)


# ## Part 2: Packages

# ### 2.1 Import the Random library and use it to create a list of ten random numbers from 0-50.
# There are several ways to do this. Google around and find one that you can replicate here. 



import random
my_randoms = [random.randrange(0, 51, 1) for nums in range(10)]
print(my_randoms)


# ### 2.2 Import the Numpy library and assign it an alias "np". Then change the list of random numbers you generated into a Numpy array.



import numpy as np

np.array(my_randoms)


# ### 2.3 Calculate the mean of the Numpy array. (Hint: Numpy has a method for this.)
# 



np.mean(my_randoms)


# ### Easter Egg: 
# In the cell below, run the following command and see what happens :)  
# `import this`  
# 



import this
