#!/usr/bin/env python
# coding: utf-8

# # Functions
# We have used functions is past lessions. Functions have a name and parameters. Some of them return a result, others don't. We typically call them using `result = name(parameters)`.
# 
# See also
# * [Python functions](https://www.tutorialspoint.com/python/python_functions.htm)
# * [List of built-in functions](https://docs.python.org/3/library/functions.html)
# 
# Let's take a look at some functions, for example `print(text)` and `pow(x, y)`. The print function takes a parameter (or multiple parameters) and returns nothing:

# In[1]:


result = print('Hello world')


# In[3]:


result


# The [pow](https://docs.python.org/3/library/functions.html#pow) function has two parameters and returns a result:

# In[4]:


result = pow(2, 3)


# In[5]:


result


# # Custom functions
# You can DEFine your own functions using the `def` statement. After the def statement, you should specify your functions' name and in brackets its parameters. Afterwards follows a colon `:` and all following lines of code which are indented are part of this function. A final `return` statement sends the result back to from where the function was called.

# In[1]:


def sum_numbers(a, b):
    
    result = a + b
    
    return result


# You can then call your function as often as you like

# In[2]:


sum_numbers(3, 4)


# In[3]:


sum_numbers(5, 6)


# Sometimes, you want to save the result of your function in a variable.

# In[4]:


c = sum_numbers(4, 5)
print(c)


# # Simplify code using functions
# Assume you have a complicated algorithm which can tell you if a number if odd or even. Let's put this algorithm in a function and call it later on. For our algorithm, we will use the [modulo operator %](https://en.wikipedia.org/wiki/Modulo_operation).

# In[13]:


def print_odd_or_even(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


# In[14]:


print_odd_or_even(3)


# In[15]:


print_odd_or_even(4)


# In[16]:


print_odd_or_even(10)


# Thus, instead of writing the same `if-else` block again and again, we can just call our custom `print_odd_or_even` function.

# # Documenting functions
# You can document what a function does in its so called doc string. The doc string follows right after the functions header and looks like this:

# In[10]:


def square(number):
    '''
    Squares a number by multiplying it with itself  and returns its result.
    '''

    return number * number


# You can then later read the documentation of the function like this:

# In[11]:


print(square.__doc__)


# Also try this if you want to have the docstring shown side-by-side in your notebook:

# In[5]:


get_ipython().run_line_magic('pinfo', 'square')


# By the way, you can do this with any function:

# In[8]:


import math
print(math.sqrt.__doc__)


# In[9]:


print(math.exp.__doc__)


# # Exercise
# Write a function that takes two parameters: `number_of_points_in_exam` and `number_of_total_points_in_exam` and returns a grade from 1 to 5. Students with > 95% of the points get grade 1, above 80% they get grade 2, above 60% grade 3 and above 50% grade 4. Students with less than 50% get grade 5 and have to repeat the exam. Then, call the function for three students who had 15, 25 and 29 points in an exam with 30 total points.

# In[ ]:




