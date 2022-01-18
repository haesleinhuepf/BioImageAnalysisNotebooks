#!/usr/bin/env python
# coding: utf-8

# # Conditions
# The `if` statement can be used to execute code conditionally. That means only if an expression is true. 
# 
# See also:
# * [if…elif…else in Python](https://www.datacamp.com/community/tutorials/elif-statements-python)
# 
# Let's take a look at some expressions first

# In[1]:


3 > 4


# In[2]:


a = 3
b = 4

a > b


# In[3]:


a < b


# In[4]:


# not equal
a != b


# In[6]:


# equal
a == b


# In[8]:


# Note: Do not mix it up with this:
a = b


# # The `if` statement
# After using `if` in combination with an expression, you need to put a colon `:` and following code must be indented:

# In[9]:


if 3 < 4:
    print("Math is great.")


# In[10]:


if 3 > 4:
    print("Math is weird.")


# You can also write more sophisticated comparisons:

# In[1]:


c = 10

if 4 < c < 20:
    print("C is between 4 and 20.")


# Or combine expressions using `and` and `or`:

# In[2]:


if c > 4 and c < 10:
    print("C is between 4 and 20.")


# If you want to check if an element is in an array, do it like this:

# In[4]:


animals = ['cat', 'dog', 'mouse']

if 'cat' in animals:
    print('Our list of animals contains a cat')


# You can also analyse strings. For example check if they start or end with certain characters:

# In[1]:


filename = "cells.tif"

if filename.endswith("tif"):
    print("The file is an image!")


# ## The `if-else` statement
# If you have two different pieces of code that should be executed alternatively, use `if-else`:

# In[5]:


quality_in_percent = 89

if quality_in_percent > 90:    
    print("Our quality is high enough.")
else:
    print("We need to improve our quality.")


# # The `elif` statement
# For executing code depending on multiple conditions, use the `elif`-statement:

# In[7]:


# determining the exam grade depending on 
number_of_correct_points = 23
number_of_total_points = 30

# compute percentage
percentage = number_of_correct_points / number_of_total_points * 100

if percentage > 95:
    grade = 1
elif percentage > 80:
    grade = 2
elif percentage > 60:
    grade = 3
elif percentag > 50:
    grade = 4
else:
    grade = 5
    
print("You scored", number_of_correct_points, "out of", number_of_total_points)
print("Your grade is", grade)


# # Exercise
# Write python code that prints out the daytime, e.g. "morning", "noon", "afternoon", "evening" and "night" depending on a given time.

# In[10]:


# it's 12:15
time_hours = 12
time_minutes = 15


# In[ ]:




