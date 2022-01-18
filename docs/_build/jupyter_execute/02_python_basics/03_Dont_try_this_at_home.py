#!/usr/bin/env python
# coding: utf-8

# # Pitfalls when working with Jupyter notebooks
# You can execute the same cell in Jupyter notebooks multiple times. This may lead to notebooks which make no sense to the reader.

# In[3]:


a = 5
b = 5


# In[6]:


a = a + 1


# In[7]:


a + b


# You can execute them in the wrong order which leads to the same effect.

# In[10]:


d = 5


# In[9]:


d = 10


# In[11]:


d


# You can see that cells were executed in wrong order, repeatedly or not subsequently, by reading the number `In [?]` on the left.
# 
# Tip: When your notebook is ready, click on menu `Kernel > Restart & Run all` to make sure all cells in the notebook are executed in the right order.

# In[ ]:




