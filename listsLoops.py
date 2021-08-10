#!/usr/bin/env python
# coding: utf-8

# ## Part 1: Lists
# 

# ### Use the provided lists to answer the questions and prompts.
# Make sure to run the cell so the lists are declared with their corresponding values.



heights = [184, 177, 190, 188, 159, 166]
weights = [84.5, 81.8, 86.1, 92.2, 69.6, 72.0 ]
names = ['John', 'Ryan', 'Bobby', 'Pete', 'Esther', 'Jane']


# ### 1.1 Create a new empty list named "BMI".



BMI = []


# ### 1.2 Combine the three lists into a new list where each element is a person's name, weight, and height. Call it "person_data".



person_data = []
for i, val in enumerate(names):
  elements = [names[i], weights[i], heights[i]]
  person_data.append(elements)
print(person_data)


# ### 1.3 Retrieve the last element of person_data.



print(person_data[-1])


# ### 1.4 Retrieve the 2nd and 3rd elements of person_data.



print(person_data[1:3])


# ### 1.5 Change the 1st element of person_data: increase weight to 84.9. Keep the other values unchanged.



person_data[0][1] = 84.9
print(person_data)


# ### 1.6 Add another person, Samantha, to person_data. Her height is 162 cm and her weight is 51.3 kg. 



person_data.insert(0, ['Samantha', 51.3, 162])
print(person_data)


# ## Part 2: Loops

# ### 2.1 Explain a for loop in your own words.



# For loops is an iteration that needs definitive iterables to loop a block of code multiple times.


# *Or add it to this Text Cell...*

# ### 2.2 Use a for loop to calculate the BMI of each person.
# >$\frac{Weight(kg)}{Height(m)^2} = BMI$  



# Solution 1:
for i, val in enumerate(person_data):
  BMI_RESULT = round(person_data[i][1] / ((person_data[i][2] / 100) ** 2), 1)
  BMI_RETRIEVE = [person_data[i][0], BMI_RESULT]
  BMI.append(BMI_RETRIEVE)
print(BMI)




# Solution 2:
for i in range(len(person_data)):
  BMI = (person_data[i][1]) / ((person_data[i][2] / 100) **2)
  print(person_data[i][0] + "'s", "BMI =", round(BMI, 1))


# ### 2.2 BONUS: Do it using list comprehension.



BMI_list_comp = [[person_data[i][0], round((person_data[i][1]) / ((person_data[i][2] / 100) **2), 1)] for i in range(len(person_data))]
print(BMI_list_comp)
