#!/usr/bin/env python
# coding: utf-8

# # Basic types in python
# We already learned there are numbers in python which can be stored in variables. We can also print out the type of a vairable.
# 
# See also
# * [Built-in types in python](https://docs.python.org/3/library/stdtypes.html)
# * [Basic types in python](https://realpython.com/python-data-types/)
# 
# This is an integer number:

# In[1]:


a = 5


# In[3]:


type(a)


# And this is a floating point variable:

# In[4]:


b = 3.5


# In[5]:


type(b)


# When combining variables of different types, Python makes a decision which type the new variable should have

# In[6]:


c = a + b


# In[7]:


type(c)


# # Strings
# Variables can also hold text. We call them a "string" in this case:

# In[1]:


first_name = "Robert"
last_name = 'Haase'


# Strings can be concatenated using the `+` operator:

# In[2]:


first_name + last_name


# In[3]:


first_name + " " + last_name


# In[4]:


text = "She said 'Hi'."
print(text)


# In[5]:


text = 'He said "How are you?".'
print(text)


# ## Combining strings and numbers

# When combining variables of numeric types and string types, errors may appear:

# In[11]:


first_name + a


# Those can be prevented by converting the numeric variable to a string type using the `str()` function:

# In[12]:


first_name + str(a)


# You can also convert strings to numbers in case they contain numbers:

# In[13]:


d = "5"


# In[14]:


int(d)


# In[16]:


a + int(d)


# If the string does not contain a number, an error message may appear:

# In[17]:


int("hello")


# In[18]:


int("")


# In[19]:


int("5")


# # Exercise
# [Marie Curie's](https://en.wikipedia.org/wiki/Marie_Curie) name and birthdate are stored in variables. Concatenate them in one string variable and print it out. The output should be "Marie Curie, * 7 November 1867"

# In[21]:


first_name = "Marie"
last_name = "Curie"

birthday_day = 7
birthday_month = "November"
birthday_year = 1867


# In[ ]:




