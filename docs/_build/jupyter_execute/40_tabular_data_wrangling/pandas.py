#!/usr/bin/env python
# coding: utf-8

# # Working with tables in pandas

# Load a csv file from disc and show it

# In[1]:


import pandas as pd

data_frame = pd.read_csv("Measurements_ImageJ.csv", delimiter=',')

# show it
data_frame


# Take a column out of the table

# In[3]:


data_frame["Round"]


# In[11]:


data_frame["Mean"]


# Determine the mean of a column

# In[15]:


import numpy as np
np.mean(data_frame["Mean"])


# Read out one particular cell of the table

# In[12]:


data_frame["Mean"][0]


# Iterate with a for loop over all cells in a column

# In[13]:


for mean_intensity in data_frame["Mean"]:
    print(mean_intensity)


# Make a new table from scratch

# In[18]:


header = ['A', 'B', 'C']

data = [
    [1, 2, 3],  # this will later be colum A
    [4, 5, 6],  #                          B
    [7, 8, 9]   #                          C
]

# convert the data and header arrays in a pandas data frame
data_frame = pd.DataFrame(data, header)

# show it
data_frame


# In[19]:


# rotate/flip it
data_frame = data_frame.transpose()

# show it
data_frame


# In[20]:


# save a dataframe to a CSV
data_frame.to_csv("output.csv")


# In[ ]:




