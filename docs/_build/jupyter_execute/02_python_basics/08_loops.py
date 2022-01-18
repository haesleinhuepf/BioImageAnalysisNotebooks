#!/usr/bin/env python
# coding: utf-8

# # Loops
# If you want code to be executed repeatedly, you can make use of loops.
# 
# See also
# * [Python loops Tutorial](https://www.youtube.com/watch?v=4dN4Cn4u2M0)
# * [Python for loops](https://www.w3schools.com/python/python_for_loops.asp)

# # For loops
# For looping over a range of numbers, we can use a simple `for` loop and the [range](https://www.w3schools.com/python/ref_func_range.asp) function.
# 
# In the following cell, the `print(i)` command will be executed a couple of times for different values of `i`. We **i**terate over a range of values: 

# In[2]:


for i in range(0, 5):
    print(i)


# Note that the above code that is indented will only be excuted for the first given number (0) and continue until the last number (5) but not including it.
# 
# You can also loop over a range of numbers with a defined step, for example step 3:

# In[3]:


for i in range(0, 10, 3):
    print(i)


# Iterating over arrays allows you to do something with all array elements:

# In[4]:


for animal in ["Dog", "Cat", "Mouse"]:
    print(animal)


# You can iterate over two arrays in parallel, pair-wise like this:

# In[6]:


# going through arrays pair-wise
measurement_1 = [1, 9, 7, 1, 2, 8, 9, 2, 1, 7, 8]
measurement_2 = [4, 5, 5, 7, 4, 5, 4, 6, 6, 5, 4]

for m_1, m_2 in zip(measurement_1, measurement_2):
    print("Paired measurements: " + str(m_1) + " and " + str(m_2))


# If you want to know the index of the element in the list as well, us the [enumerate](https://realpython.com/python-enumerate/) function:

# In[5]:


# numbering and iterating through collections
for index, animal in enumerate(["Dog", "Cat", "Mouse"]):
    print("The animal number " + str(index) + " in the list is " + animal)


# ## Generating lists in loops
# On can generate lists using for loops. The conventional way of doing this involves multiple lines of code:

# In[2]:


# we start with an empty list
numbers = []

# and add elements
for i in range(0, 5):
    numbers.append(i * 2)
    
print(numbers)


# One can also write that shorter. The underlying concept is called [generators](https://wiki.python.org/moin/Generators).

# In[4]:


numbers = [i * 2 for i in range(0, 5)]

print(numbers)


# The conventional combination involving an if-statements looks like this:

# In[6]:


# we start with an empty list
numbers = []

# and add elements
for i in range(0, 5):
    # check if the number is odd
    if i % 2:
        numbers.append(i * 2)
    
print(numbers)


# And the short version like this:

# In[7]:


numbers = [i * 2 for i in range(0, 5) if i % 2]

print(numbers)


# # While loops
# Another way of looping is using the `while` loop. It works by checking a condition, similar to the `if` statement. It will interrupt execution as soon as the condition is no longer true:

# In[7]:


number = 1024

while (number > 1):
    number = number / 2
    print(number)


# # Interrupting loops
# You can interrupt loops at specific points in your code using the `break` command:

# In[8]:


number = 1024

while (True):
    number = number / 2
    print(number)
    
    if number < 1:
        break;


# # Skipping iterations in loops
# If you want to skip iterations, you can use the `continue` statement. That often makes sense in combination with an `if`:

# In[12]:


for i in range(0, 10):
    if i >= 3 and i <= 6:
        continue
    print(i)


# # Exercise 1
# Assume you have a list of filenames and you want to do something with them, for example print them out. Program a for loop which print out all file names which end with "tif".

# In[1]:


file_names = ['dataset1.tif', 'dataset2.tif', 'summary.csv', 'readme.md', 'blobs.tif']


# In[ ]:





# # Exercise 2
# Assume you have a list of circle radii. Make a table with two columns: radius and area. 
# Hint: See the table exercise from last week.

# In[2]:


radii = [3, 15, 67, 33, 12, 8, 12, 9, 22]


# In[ ]:




