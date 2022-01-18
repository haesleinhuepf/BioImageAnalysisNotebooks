#!/usr/bin/env python
# coding: utf-8

# # Measure overlap between two label images

# In[1]:


import pyclesperanto_prototype as cle

from skimage.io import imread, imsave, imshow
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# initialize GPU
cle.select_device("GTX")


# In[2]:


# load data
labels = cle.voronoi_otsu_labeling(imread('https://samples.fiji.sc/blobs.png'), spot_sigma=4)

cle.imshow(labels, labels=True)


# In[3]:


extended_labels = cle.dilate_labels(labels, radius=5)

cle.imshow(extended_labels, labels=True)


# In[4]:


# measure the ratio of overlap
overlap_ratio = cle.label_nonzero_pixel_count_ratio_map(extended_labels, labels)

cle.imshow(overlap_ratio, colorbar=True)


# In[ ]:




