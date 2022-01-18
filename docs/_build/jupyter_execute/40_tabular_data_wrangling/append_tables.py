#!/usr/bin/env python
# coding: utf-8

# # Append tables

# In[1]:


import pandas as pd


# In[2]:


dict1 = {
    "A":[1,2],
    "B":[3,4],
    "C":[5,6],
    }


# In[3]:


dict2 = {
    "C":[1,2],
    "B":[3,4],
    "D":[5,6],
    }


# In[6]:


table1 = pd.DataFrame(dict1)
table1


# In[7]:


table2 = pd.DataFrame(dict2)
table2


# In[16]:


combined_tables = table1.append(table2, ignore_index=True)
combined_tables


# In[17]:


combined_tables.to_dict()


# In[ ]:


c

