#!/usr/bin/env python
# coding: utf-8

# # Basic math in python
# For understanding how python works, we will do some basic math using python variables and functions. Both play an important role in python and will accompany us through the whole semester.
# 
# This is a variable called "a" and we assigne a value to it, 5:

# In[10]:


a = 5


# Afterwards, we can re-use this variable, for example to print it out:

# In[11]:


print(a)


# Somtimes, it might be helpful to put some additonal explanatory text when printing out variables:

# In[12]:


print("The area is", a)


# We can use more variables and combine them using mathematical operators:

# In[13]:


b = 3
c = a + b


# In[14]:


print(c)


# In[15]:


d = 6
e = 7
f = a * d
g = f / e
h = 1 + g


# In[16]:


print(h)


# We can also get the value of a variable or expression (combination of variables) by putting it in a cell alone.

# In[17]:


h


# In[18]:


a + b


# If you run illegal operationsn, such a dividing by zero, you receive an error message like this:

# In[43]:


a / 0


# If a variable is not defined, you would receive an error message like this:

# In[42]:


a / k


# # Built-in math functions
# Python comes with a list of [built-in functions](https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch04s04.html)

# In[20]:


pow(3, 2)


# In[32]:


abs(-8)


# In[29]:


round(4.6)


# Some of these operations are not exactly doing what you expect. Better try them out before you use them.

# In[33]:


round(4.5)


# ## The math library
# There is pre-installed python library of additional [math functions](https://docs.python.org/3/library/math.html). Before you can use them, you need to import this library. Otherwise, you would receive an error like this:

# In[39]:


math.sqrt(9)


# When importing a library, you tell the python interpreter that you want to make use of everying that is part of a given library, in our case "math":

# In[40]:


import math


# After importing the "math" library, you can use functions that are part of math.

# In[41]:


math.sqrt(9)


# # Exercise
# Assume you have two points specified by their x and y coordinates. Calculate the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#Two_dimensions) between them.

# In[44]:


x1 = 5
y1 = 3

x2 = 8
y2 = 11

