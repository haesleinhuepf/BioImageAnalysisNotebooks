#!/usr/bin/env python
# coding: utf-8

# # Basic statistics with pyclesperanto
# A common use case for image processing in the biology context is deriving statistics of segmented objects. clEsperanto offers a function for that: [statistics_of_labelled_pixels](https://clij.github.io/clij2-docs/reference_statisticsOfLabelledPixels).

# In[1]:


import pyclesperanto_prototype as cle

from skimage.io import imread, imsave, imshow
import matplotlib
import numpy as np

# initialize GPU
cle.select_device("RTX")


# In[2]:


# load data
image = imread('https://samples.fiji.sc/blobs.png')

# segment the image
labels = cle.voronoi_otsu_labeling(image, spot_sigma=3.5)
cle.imshow(labels, labels=True)


# ## Deriving basic statistics of labelled objects

# In[3]:


statistics = cle.statistics_of_labelled_pixels(image, labels)
statistics


# We can use [pandas](https://pandas.pydata.org/) to process that kind of tabular data. 

# In[4]:


import pandas as pd


# In[5]:


table = pd.DataFrame(statistics)
table


# In[6]:


table.describe()


# In[ ]:




