#!/usr/bin/env python
# coding: utf-8

# # Plotting
# So far we only printed out results of operations as text. We should draw some scientific plots as visualization. For drawing plots, we use the [matplotlib](https://matplotlib.org/) library.
# 
# See also:
# * [Matplotlib sample plots](https://matplotlib.org/stable/tutorials/introductory/sample_plots.html)
# * [Matplotlib plotting](https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html)
# 
# Let's start with importing the python-plotting module of matplotlib. We give it a short alias name "plt" to have easier access to it:

# In[2]:


import matplotlib.pyplot as plt


# If this import command resulted in an error message suggesting that "matplotlib" is not known, install it. You can do this by opening another console window, activating the same conda environment and running this:
# ```
# conda install matplotlib
# ```

# For plotting, we need values to plot. Let's start with a list of x-values:

# In[3]:


x_values = range(0, 360, 10)


# To compute the corresponding y-values, we use a for loop, that creates a new list of values equal to the `x_values` list and computes a new number for each entry:

# In[4]:


import math
y_values = [math.sin(x * math.pi / 180) for x in x_values]


# Then, let's draw a simple plot

# In[5]:


plt.plot(x_values, y_values)


# Plots can be modified in various ways.

# In[6]:


plt.plot(x_values, y_values, '*')


# In[7]:


plt.plot(x_values, y_values, color='green')


# If you want to combine multiple plots in one figure, you can do this:

# In[8]:


plt.plot(x_values, y_values, color='green')

neg_y_values = [- y for y in y_values]
plt.plot(x_values, neg_y_values, color='magenta')


# ## Sub figures
# The [subplots](https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html) command allows you to have multiple plots in one block.

# In[11]:


fig,axs = plt.subplots(1, 2)

axs[0].plot(x_values, y_values, color='green')
axs[1].plot(x_values, neg_y_values, color='magenta')


# In[15]:


fig,axs = plt.subplots(2, 3, figsize=[15,10])

axs[0,0].plot(x_values, y_values, color='green')
axs[0,1].plot(x_values, neg_y_values, color='magenta')
axs[0,2].plot(x_values, neg_y_values, color='red')
axs[1,0].plot(x_values, neg_y_values, color='cyan')
axs[1,1].plot(x_values, neg_y_values, color='blue')
axs[1,2].plot(x_values, neg_y_values, color='yellow')


# # Exercise
# Plot sinus and cosinus of values between 0 and 360 degrees in one plot.

# In[ ]:




