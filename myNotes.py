#!/usr/bin/env python
# coding: utf-8

### **Math Operators:**
"""

# Exponentiation Operator:
 ## Multiplies the first number by itself x times.
 x = 4

 2 ** x

# Square Root Operator:
## Raises to the 1/2 power.
16 ** .5

# Modulus Operator:
## Is the remainder after division.
3 % 2

# Integer Division Operator:
## Answer should be (1.5), but it will round down to the nearest whole number.
3 // 2

# Equals Plus Operator:
nums_list = [2,3,5,10,20] # Equals = 40
total = 0
for nums in nums_list:
  total += nums # Equals Plus Operator works inside for Loops | Same as total = total + nums
print(total)

"""### **Comparison Operators:**"""

# The Equality Comparison Operator:
2 == 2

# The Inequality Comparison Operator:
5 != 2

# The Greater-Than Operator:
4 > 2

# The Less-Than Operator:
1 < 4

# The Greater-Than or Equal-To Operator:
6 >= 3

# The Less-Than or Equal-To Operator:
5 <= 5

"""### **Logical Operators:**

In some cases we might want to include multiple conditions in our if statement and only have an if statement's block execute if both conditions are true or if either of the conditions are true. We can use the two following "Logical Operators" in these kinds of scenarios

`and` - Evaluates to True if expressions to its left ***and*** to its right are true. (Preferably on Top of "or"). 

**and** statements hold the most strick conditions on a function.

`or` - Evalues to True if either expressions to its left ***or*** right are true.
"""

# You can fiddle with these parameters to see how the if statement below will react.
wants_to_learn_data_science = True
will_work_hard = True
age = 20

if age >= 18 and wants_to_learn_data_science and will_work_hard:
  print("Go to Lambda School!")
elif wants_to_learn_data_science or will_work_hard or age >= 18:
  print("Your future is bright!")
else:
  print("Find something that's a good fit for you.")

"""### **if Statements - elif - else Conditions:**"""

money_in_wallet = 5.00
movie_ticket_price = 8.99

if money_in_wallet >= movie_ticket_price:
  print("Go to the movies!")
else:
  print("Stay home and watch Netflix.")

# In addition to the if and else keywords we can use the elif keyword
# to include multiple if statements together in a group.
visitor = "Mike"

if visitor == "Bryce":
  print("Hi Bryce!")
elif visitor == "Jacob":
  print("Hi Jacob!")
elif visitor == "Mike":
  print("Hi Mike!")
else:
  print("Pleased to meet you!")

# Expressions using the in keyword will evaluate to True if an item is
# found in a list, but will evaluate to False if an item is not found in a list.
friends = ["Bryce", "Jacob", "Mike", "Ben", "Young"]

visitor = "Mike"

if visitor in friends:
  print("Hi " + visitor + "!")
else:
  print("Pleased to meet you!")

"""### **Functions:**"""

first_number = []
second_number = []

def the_sum(first_number, second_number):
  total = first_number + second_number
  return total

the_sum(2, 3)

"""### String Methods"""

# String 
my_string = "this is a string"

my_string.upper()

"this is a string".upper()

"""Methods are functions that are specific to a certain object -a certain data type. Above we have shown the `.upper()` method that can be called on strings. You'll notice that we can call it on either a variable that holds a string value or on the string value directly. 

Whenever we call a method we do so by using what is called "Dot Notation" This simply means that we call the function by putting a dot `.` between the method call and the variable name. This indicates to python that we want to call the method on that specific object/variable. 
"""

my_string.capitalize()

my_string.split()

"""Additional [string methods](https://www.programiz.com/python-programming/methods/string)

### Lists Methods

We have already used a few list methods when working with lists. We have used methods like `.append()`, `.pop()`, `.remove()`, and `.insert()`, 

Additional [list methods](https://www.programiz.com/python-programming/methods/list)
"""

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday"]

# Find the index position of an element in a list:
weekdays.index("Wednesday")

# Don't work across the board:
weekdays.remove("Tuesday")
weekdays

# Some methods can change their objects. For example, we forgot to include the 
# last weekday in our weekday list:
weekdays.append("Friday")
weekdays

"""**Remember:**


*   In Python, _everything_ is an object.
*   Different objects have different methods, depending on their data types.
*   Some methods change the object they're called on. So be careful!

### **for Loops:** Running blocks of code repeatedly (iteration)
"""

for item in [1,2,3,4,5]:
  print("Hello!")

for value in [1,2,3,4,5]:
  print(value)

# The declaration of any for loop ends with a colon : this tells the Python
# interpreter that I'm done with that statement and that the code block
# that I want to repeat is coming next.
animal_list = ['cat', 'dog', 'fish']

for animal in animal_list:
  # Indent to put things inside the For Loop
  print('-------------------')
  print("*****", animal, "*****")
  print('-------------------\n')

# Unindent to put code outside of the for loop
print("Are some of my favorite animals.")

# The range() Iterable:
## The number you want it to start at (inclusive).
## The number you want it to end at (exclusive).
for item in range(1, 6):
  print(item)

# create a new list that holds the squared values by creating an empty list
# and appending these new values to the empty list.
numbers_to_square = [1,2,3,4]

squared_numbers = []
for number in numbers_to_square:
  squared_numbers.append(number**2)

print(numbers_to_square)
print(squared_numbers)

# I can also keep track of the number of iterations that the for loop is on by
# using the enumerate() function. When I use the enumerate function I can add
# a second variable to the beginning of the for loop. The first variable will
# represent the specific iteration of the for loop, and the second variable
# will change to represent the each item in the list.
for i, number in enumerate(numbers_to_square):
  print("index:", i, "- item in original list:", number, "- list squared:", number**2)

# Now not only can I use this i variable in combination with the enumerate()
# function to track the iteration that my loop is on, I can use it to overwrite
# values in the original list as well.
for i, number in enumerate(numbers_to_square):
  numbers_to_square[i] = number**2

print(numbers_to_square)

# I can now use this "index" value not only to access items in the original
# list but to modify the previous list as I am looping over it. Lets write
# a loop that subtracts one from each item in the list that we are iterating over.
my_list = [5,6,7,8,9,10]

for i, num in enumerate(my_list):
  my_list[i] = my_list[i]-1

print(my_list)

# Three lists combined into a new list where each element is
# a person's name, weight, and height. Called "person_data".
## Using for i, val in enumerate():
heights = [184, 177, 190, 188]
weights = [84.5, 81.8, 86.1, 92.2]
names = ['John', 'Ryan', 'Bobby', 'Pete']

person_data = []
for i, val in enumerate(names):
  element = [names[i], weights[i], heights[i]]
  person_data.append(element)
print(person_data)

# Another example of three lists combined:
## Using range and len
person_data = []
length = (len(names))
for i in range (length):
  element = [names[i], weights[i], heights[i]]
  person_data.append (element)
print (person_data)

# Calculate BMI to all elements inside a list:
## Solution 1 Using enumerate and print loop
for i, val in enumerate(person_data):                                           # ENUMERATE USING LIST TOTAL RANGE (NOT SPECIFIED ON ARGUMENT [0:1])
  BMI = (person_data[i][1]) / ((person_data[i][2] / 100) **2)
  print(person_data[i][0] + "'s", "BMI is", round(BMI, 1))

# Another way to Calculate BMI to all elements inside a list:
## Solution 2 using range and len
BMI = []
for i in range(len(person_data)):                                               # RANGE USING LEN (LENTH) OF "person_data"
  BMI_RESULT = round(person_data[i][1] / ((person_data[i][2] / 100) ** 2), 1)   # CALCULATION (RETREAVES INFO PER ITERATION AND PUT IT ON A TEMP LIST)
  BMI_RETRIEVE = [person_data[i][0], BMI_RESULT]                                # RETRIEVING ELEMENTS ("BMI_RESULT" DOESNT NEED index BECAUSE IT RETRIEVES INFO PER ITERATION)
  BMI.append(BMI_RETRIEVE)                                                      # PLACING RETRIEVED ELEMENTS ON A LIST CALLED "BMI"
print(BMI)

# Another way to Calculate BMI to all elements inside a list:
## Solution 3 Using enumerate and new list
BMI = []
for i, val in enumerate(person_data[0:]):                                       # ENUMERATE USING RANGE [0:]
  BMI_RESULT = round(person_data[i][1] / ((person_data[i][2] / 100) ** 2), 1)   # CALCULATION (RETREAVES INFO PER ITERATION AND PUT IT ON A TEMP LIST)
  BMI_RETRIEVE = [person_data[i][0], BMI_RESULT]                                # RETRIEVING ELEMENTS ("BMI_RESULT" DOESNT NEED index BECAUSE IT RETRIEVES INFO PER ITERATION)
  BMI.append(BMI_RETRIEVE)                                                      # PLACING RETRIEVED ELEMENTS ON A LIST CALLED "BMI"
print(BMI)

# List Comprehention:
BMI_list_comp = [[person_data[i][0], round((person_data[i][1]) / ((person_data[i][2] / 100) **2), 1)] for i in range(len(person_data))]
print(BMI_list_comp)

"""### **Lists:**"""

# One dimensional list:
## You can create a list simply by using brackets [ ] and separating elements with a comma.
ages = [24, 23, True, 23, 'Cat', 46, 19, 34]
ages

# Three dimensional lists:
three_dimensional_list = ['cat', ['fish', 'shark', ['octopus', 'squid']], 'dog']
three_dimensional_list[1][2][1]

# Two dimensional lists:
## Same idea, declare lists with []'s and separate elements with commas. 
## Even if those elements are other lists.
students = [           # Start with an open bracket
    ["Popeye", 24],  # Each element is a list with 2 elements [name, age]
    ["Tabatha", 23], # We still have to separate each item in our large list with commas
    ["Jerry", 25],
    ["Flynn", 23],    
    ["Sally", 40]
]                   # End with a close bracket

students

# To access the LAST element in the list, we can use -1.
# So let's say we want the 2nd to last element in the list:
students[-2]

# Get the item at index position 4 in the outer list
# then get the item at index position 0 of that item.
students[4][0]

# Now let's say we want Sally and Michael's information but want to access it 
# by indexing from the back of the list:
students[-4:-2]

# From the beginning of the list to the third element (not including the third)
students[:3]

## Remember, we're actually getting elements 0, 1  and 2.
### The element at index 3 would be Flynn's info, but because slicing returns
### up to by not including include whatever index is provided second.

# .append method/function:
## Appends one Element to the end of the list.
students.append(['Luiz', 21])
students

# .insert method/function:
## Inserts one Element of the right hand side Argument, on the index number of the left hand side
## and pushes other Elements to +1 index number on the list.
students.insert(0, ['Amanda', 34])
students

# Changing Elements from a List:
## We can change an element within a list by accessing that element via its index
## and then reassigning that index to a new value.
### Luiz was 21, now he is 32.
students[6][1] = 32
students

# Same as before, but now we changed the entire sub list of index 6.
## Index 6 was ['Luiz', 32], now its ['Ricardo', 26].
students[6] = ['Ricardo', 26]
students

# Removing Elements from a List and Storing it on a variable:
## We can remove an item at a specific index in a list using the .pop() method/function.
## This method/function will also store in a variable, the value that we have removed from the list.
ricardo = students.pop(6)
ricardo

# Removing Elements from a List:
# If you want to remove an Element by its value but not by its index you can
# use the .remove() method/function.
students.remove(['Amanda', 34])
students

"""### **Dictionaries:**"""

# Dictionaries:
# Left hand side always a 'string key', on the right hand side can be anything.
activities = {'rain': 'read a book',
              'sunny': 'go for a swim',
              'snowy': 'build a fire' 
             }

# Dictionaries can be made with other data types:
numbers = {'one': 1,
           'two': 2.0,
           'three': 3
          }

numbers['three']

activities['sunny']

type(numbers)

"""### **Numpy:**"""

# Numpy has a nifty method to convert regular Python lists into Numpy arrays:
import numpy as np
weights = [70.2, 85.6, 75.9, 79.0, 82.7]
heights = [170.9, 188.5, 181.2, 179.9, 174.3]
ages = [23, 35, 31, 28, 43]

np_weights = np.asarray(weights)
np_heights = np.asarray(heights)
np_ages = np.asarray(ages)

88.362 + (13.397 * np_weights) + (4.799 * np_heights) - (5.677 * np_ages)

# Let's declare an array to hold our BMR values:
bmr = 88.362 + (13.397 * np_weights) + (4.799 * np_heights) - (5.677 * np_ages)
bmr

# Numpy also has really awesome random number generators:
np.random.seed(42) ### Locks the random numbers to a Seed.
y = np.random.randint(5, size=(3, 4))
y

# Every time you run this cell, it'll output different numbers.

# Confused about what that was? Remember the built-in help() function!

"""So we have three rows and six columns. How might we subset a specific value now?

Let's say we want the value in the 3rd row and the 2nd column (value is 1).
"""

y[2,1]

"""Remember that Python is 0-indexed! (Since it starts at 0, the 3rd element is at index position 2.)"""

# Alternatively, we could also do...
y[2][1]

"""Slicing, revisited!"""

# Ok, let's say we want only the first two columns of each row:
y[:,0:2]

"""Remember that slicing ranges have an inclusive start and an exclusive end. Meaning the start value is included in the slicing, but the end value is not.  

At the same time, a colon will include the entire range of that row/column.
"""

# Now let's just get the third row:
y[2,:]

"""Summary Statistics

A numerical library wouldn't be much good if it couldn't give us some basic stats about our data, now would it?
"""

# Calculate the average of an array
np.mean(bmr)

# Median
np.median(bmr)

# Standard Deviation
np.std(bmr)

"""### **Pandas:**"""

# Importing pandas and giving it an alias called "pd"
## Placing the DataFrame inside a variable called "df"
import pandas as pd
# df = pd.read_csv('archiveName.csv')
df = pd.read_csv("https://raw.githubusercontent.com/axrd/datasets/master/gdp.csv")
df.head(2)

# The grid shape of the DataFrame:
df.shape

# Renaming a Columns:
df = df.rename(columns={'COUNRY':'COUNTRY'})
df.columns

# Using the dataframe.drop() method to drop 'Unnamed: 0'

# The the following two lines of code are equivalent
df = df.drop(df.columns[0], axis=1)
# df = df.drop('Unnamed: 0', axis=1)
df.head(1)

# Max GDP:
df.loc[df['GDP (BILLIONS)'].idxmax()]

# Median GDP:
print([df['GDP (BILLIONS)'].median()])

df = pd.read_csv('https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv')
df.head(5)

# Return entries 25 through 30.
df.iloc[25:31,:]

# Return Saturdays:
data = df.loc[0:]['day'] == 'Sat'
df[data]

df = pd.read_csv('https://raw.githubusercontent.com/axrd/datasets/master/gdpmessy2.csv')
# Pandas has a nifty tool to check for null values. For now, you can think of 
# nulls as missing values.

## We'll subset our data by choosing ALL the rows that have missing values.
df[df.isnull().any(axis=1)]

# Ok, but scrolling throuh several rows looking for df.isnull() "True" sounds awful. There has 
# to be a better way, right? There is. Remember the sum function?

df.isnull().sum()

# We specify the row index, the column name, and the value we'd like to assign to it:
df.at[6, "countrys"] = "Anguilla"
df.at[14, "code"] = "BHS"
df.at[16, "GDP"] = 186.60
df.at[20, "countrys"] = "Belize"
df.at[55, "code"] = "DNK"
df.at[70, "GDP"] = 2902.0
df.at[90, "code"] = "HUN"
df.at[96, "GDP"] = 245.80
df.at[100, "code"] = "JAM"
df.at[106, "countrys"] = "Kiribati"
df.at[200, "code"] = "TGO"
df.at[206, "countrys"] = "Tuvalu"

# Checking if there's any null left after correction:
df[df.isnull().any(axis=1)]

# Looking for duplicates:
df["code"].value_counts(sort=True).head(3)

# Finding the duplicates:
df[df['code'] == "ZMB"]

"""### **Data Visualization / Statistics:**"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv", index_col=0)

# Describes 'tip' mean, median (50%), min, max, std and etc...
df['tip'].describe()

# Plot density:
df['tip'].plot.density();

"""Skewness: left, right, or middle?

![Skewness](https://cdn-images-1.medium.com/max/1600/1*nj-Ch3AUFmkd0JUSOW_bTQ.jpeg)
"""

# Box Plot:
df.boxplot(column='tip', by='size');

# Histograms:
df['day'].hist(bins=10);

# Useful for discrete data counts.
df['day'].value_counts()

# Useful for discrete data counts with plot visualization:
df['day'].value_counts().plot(kind='barh'); # You can use (kind=bar) or (kind=barh) to make it horizontal.

"""**Variability:** how spread out is our data?

**Also known as the *spread* of a set of values, variability measures how different they are from each other. More intuitively, variability is a measure of how far values are from one specific value. Can you guess which one? Hint, how can you describe a group of values with just one value?**



*   **Range**: the difference between the largest and smallest values in a set.
*   **Variance**: the difference between the largest and smallest values in a set.
*   **Standard deviation**: the average distance from the mean.

"""

# Lets calculate the Standard Deviation:
# Standard Deviation is the average distance of each point from the mean
## ddof=1 means that will make the same calculation as .describe() from pandas library
np.std(df['total_bill'], ddof=1)

# Let's calculate the Variance:
# Variance is the average squared distance of each point from the mean.
np.var(df['total_bill'], ddof=1)

# The Standard Deviation is the Square Root of the variance. 
np.sqrt(np.var(df['total_bill'], ddof=1))

"""### **Correlation:**

You've probably heard people describe two things as *correlated* -- but what does that mean exactly? Well, correlation is basically whether or not two variables move in the same direction. It is yet another descriptive statistic that can help us get a sense of what a set of values looks like.




"""

# Now let's bring in our dataset of MPG data:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/mpg.csv")
df.head()

"""**What does the relationship between the values look like?**"""

# MPG (miles per gallon) is a measure of a car's fuel efficiency. Basically, how much distance
# can it travel per unit of fuel. Let's see if there are any relationships between MPG and
# the other features.

df.plot.scatter(x='mpg', y='cylinders');
# plt.show()

# In case you forgot, adding a ';' at the end hides some extra info that comes with the plot.
# Feel free to remove it to see for yourself!

df.plot.scatter(x='mpg', y='displacement');

df.plot.scatter(x='mpg', y='horsepower');

df.plot.scatter(x='mpg', y='weight');

df.plot.scatter(x='mpg', y='acceleration');

df.plot.scatter(x='mpg', y='model-year');

"""**Measuring the relationship between variables:**

*Pearson correlation coefficient*

$\rho = \frac{\text{cov}(X,Y)}{\sigma_x \sigma_y}$

**Don't worry too much about the formula for now. We'll go deeper into the math later on in the course. For now, just understand this:**  

*A value of 1 represents a perfect positive relationship, -1 a perfect negative relationship, and 0 indicates the absence of a relationship between variables.*
"""

# Here's a way to see the correlation coefficients of all the features:
df.corr()

"""DataFrame.Corr() [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html).

**To recap:**

*   **Central tendency** is basically the value most representative of a group of values.
*   **Variability** tells you how spread out (or different) your values are from one another.
*   **Correlation** gives you an idea of the relationship between two variables. Namely, how do they move relative to one another.
*   **Correlation coefficient** gives you a measure, between 0 and 1, of how correlated two variables are.

### **Continuous, discrete, orginal, numeric, binary, categorical:**
"""

# Simply run this cell to import the tips dataset:

df = pd.read_csv("https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv", index_col=0)
df.head()

"""*   **total_bill** is continuous, ordinal, and numeric
*   **tip** is also continuous, ordinal, and numeric
*   **sex** is categorical or discrete; it's also binary (male vs. female)
*   **smoker** same as *sex*
*   **day** is categorical but not binary (there are 7 categories, 1 for each day of the week)
*   **time** is categorical (discrete)
*   **size** is numeric and categorical/discrete (can't have 3.4 people at a table)

### **Basic Info:**
"""

values = [11.82, 65, 77, 19.89, 180, 1078, 173]
# Smallest value:
min(values)

values = [11.82, 65, 77, 19.89, 180, 1078, 173]
# Largest value:
max(values)

values = [11.82, 65, 77, 19.89, 180, 1078, 173]
# Sort the values:
sorted(values)

# \n Jumps to the next line:
print('It will jump to the next line.\nok, line jumped.')

# Variables:
x = 2
y = 2
x+y

# Print:
z = 'Hello Word'
print(z)

# Type:
type(z)

# Booleans:
a = True
b = False

type(a), type(b)

# Changing float to a string at the formula with str()
a = 'π is approximately equal to '
b = 3.14159

a + str(b)

"""### **Remember:** *Different* data types have *different* behavior:"""

# Integers & floats can be added together arithmetically
23 + 17

# Strings are concatenated (bunched) together
'ac' + 'dc'

# You can also think of true or false as 1 or 0 (binary)
True + False

"""# **Tips:**
**Parameters:** They are inside where the ***function*** is defined "***def***".

**Iterables:** They are a category of data structures that hold multiple items in them. ***A list is an iterable!***

**Indent:** They are 2 spaces before the **methods** and **functions** inside a "***def***", "***for***" loop, "***if***" statements, "***elif***" and "***else***" condition. It will be considered part of a loop, statement, condition or where a function defined.

**Functions:** You can think of functions as ***sets of instructions that are packaged together in order to perform a specific action***. Python has some built-in functions. You can also download Libraries and Packages of functions from other people.

**Methods:** They each have unique functions, called methods, that **apply only to objects of that data type**. Python has **String Methods** and **List Methods**.

**Arguments:** They are inside **methods** and **functions**.

**Attributes:** They look like Methods, but they don't need () Arguments.

**Objects:** ***(GET MORE INFO ON GOOGLE)***

**Syntax:** ***(GET MORE INFO ON GOOGLE)***

**Lists:** They hold **elements** inside. It can hold any data type and can be nested inside another list.

**Dictionaries:** Associating this with that. Dictionaries are made up of **paired keys** and **values**.

**Libraries:** They are functions from other people. ***(GET MORE INFO ON GOOGLE)***

**Packages:** The are packages of functions from other people. ***(GET MORE INFO ON GOOGLE)***

**Numpy:** Short for Numerical Python, is a staple in every data scientist's tool kit. It's a powerful Python library that comes in handy when doing complex calculations on lots of data.

**Pandas:** Pandas has methods to read different types of data files and turn them into a DataFrame. In practice, you could be pulling data from different databases, different websites, your local computer, or a combination of all the above. The most common pandas method is the **CSV** and it stands for "comma separated values".

***pandas.read_csv('finaName.csv or website link')***



# **Errors:**

**List index out of range:** The list is missing an index or the nested index is wrong.

# **Simbols:**

- Semicolon ;
- Colon :
- Parentheses (x)
- Square Brackets [x]
- Brackets {x}
- Curly Braces {x}

# **Shortcuts:**

CTRL + / Comments all selected lines at once.

# **Order of Operations:**

1. Inner Most Set of Parenthesis / Parenthesis
2. Exponents
3. Multiplication / Division
4. Addition / Subtraction

# **Functions:** Reusable bits of code

### What is a function?
To recap, Python can do some very useful things: 

*   Store single values to variables
*   Store multiple values to the same variable, and keep track of their order in lists.
*   Loop over lists and other iterables to run certain blocks of code repeatedly.
*   Evaluate conditions to control *which* blocks of code get run.

For example, that BMI calculator you built -- pretty cool, right? But what if you wanted to calculate the BMI of ten people? Swapping in values for each person would get pretty tedious.  

That's where ***functions*** come in!  

You can think of functions as ***sets of instructions that are packaged together in order to perform a specific action***. You also call a function by using its name, so, like variables, they must be specific and case-sensitive.

# **Methods:** built-in functions for different data types
Each of the structures above is what's called an ***object*** in Python. They are made up of the values assigned to them via variables. Each object represents a different data _type_ depending on its value(s). 

They each have unique functions, called ***methods***, that apply only to objects of that data type.

# **Layout Commands:**

# Big Header

## Smaller Header

### Even smaller Header

This is paragraph text.

**Bold Text**

<https://lambdaschool.com>

---

[Lambda Shool](https://lambdaschoo.com)

> Indent Block

- This is a bulleted list
 - an indented bullet
- and another bullet

```
# This is formatted as code
```
"""