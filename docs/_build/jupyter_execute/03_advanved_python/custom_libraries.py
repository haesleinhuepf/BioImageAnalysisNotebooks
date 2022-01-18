#!/usr/bin/env python
# coding: utf-8

# # Custom libraries
# When programming python for some time, you may be using again and again the same code. You could copy&paste it from jupyter notebook to jupyter notebook. However, notebooks are not meant to hold many functions. Notebooks are meant to show short and concise examples of code. Thus, in order to organize our code, we can put function we use more often into a python file, a custom library, and then import the functions.
# 
# See also:
# * [The import system](https://docs.python.org/3/reference/import.html)
# 
# Within the same folder, there exists a [my_library.py](my_library.py) file. It contains two functions. Let's import them and use them:

# In[1]:


from my_library import square


# In[2]:


square(5)


# In[4]:


from my_library import *


# In[5]:


wuzzle(5)


# When maintaining your own library of functions, make sure that the functions have reasonable names and useful docstrings. You may otherwise be confused about your own code later on.
# 
# This is a good example:

# In[6]:


print(square.__doc__)


# This is a bad example:

# In[8]:


print(wuzzle.__doc__)


# ## Modifying code in custom libraries
# If you modify code in a python library file side-by-side with the code in a notebook, you may have restart your notebook after modifying the library file. You can do this in the menu `Kernel > Restart & Run All`.

# # Exercise
# Create an own library and write a function that can compute the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between two points. The point coordinates are given as tuples. Hint: You will need a for-loop in this function that iterates pair-wise over the two coordinates:

# In[9]:


p = (1.5, 6.4, 7.3)
q = (3.4, 1.0, 0.9)


# In[ ]:




