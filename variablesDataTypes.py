#!/usr/bin/env python
# coding: utf-8

# ## Part 1: Variables
# 

# ### 1.1 Create three numerical variables (ints and/or floats) and add them together. At least one of your variables must hold a negative value.



a = 5.0
b = 6
c = -1

a + b + c


# ### 1.2 Write a sentence in five parts, assign each part to a variable, then concatenate them all together. Account for spacing!



a = 'There are more things '
b = 'in heaven and earth, '
c = 'Horatio, '
d = 'than are dreamt of in '
e = 'your philosophy.'

a + b + c + d + e


# ### 1.3 We need to calculate Joey's body mass index. Here's the formula for BMI:  
# 
# >$\frac{Weight(kg)}{Height(m)^2} = BMI$  
# 
# Joey is 1.82 meters tall and weighs 78 kg. Create a variable for his height, weight, and BMI by combining the first two. 
# 



weight = 78
height = 1.82
BMI = weight / (height ** 2)

print(BMI)


# ### 1.4 Now calculate Susie's BMI.
# Susie is 1.63 meters tall and weighs 59 kg. Calculate her BMI by changing the values of the variables you created for Joey. It's easier than creating all new variables, right?



weight = 59
height = 1.63
BMI = weight / (height ** 2)

print(BMI)


# ## Part 2: Data Types

# ### 2.1 What is the data type of the following variables?



a = -91
b = 12.0222
c = True
d = "Loosey goosey"

type(a), type(b), type(c), type(d)


# ### 2.2 How do strings behave differently than integers or floats?

# *Write your answer below this line*: 
# 
# ---
# Strings concatenate. Integers or floats sums toguether.
# 

# ### 2.3 Create one variable holding a string and another variable holding a float. Concatenate the two together. 



a = 'π is approximately equal to '
b = 3.14159

a + str(b)
