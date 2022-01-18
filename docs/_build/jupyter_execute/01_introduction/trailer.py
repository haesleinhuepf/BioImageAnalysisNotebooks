#!/usr/bin/env python
# coding: utf-8

# # Trailer: Bio-image Analysis with Python
# In this collection of notebooks we will dive into image analysis, machine learning and bio-statistics with Python. This notebook serves as a trailer of what we will be doing.
# 
# ## Working with image data

# In[1]:


from skimage.io import imread
from pyclesperanto_prototype import imshow


# In[4]:


# open an image file
image = imread("../../data/blobs.tif")
print("Image size", image.shape)


# In[5]:


# visualizing an image
imshow(image)


# ## Image segmentation

# In[6]:


# normalize image
from csbdeep.utils import normalize
normalized_image = normalize(image, 1,99.8, axis=(0,1))

# load pretrained deep-learning model
from stardist.models import StarDist2D 
model = StarDist2D.from_pretrained('2D_versatile_fluo')

# predict labels
label_image, details = model.predict_instances(normalized_image)
imshow(label_image, labels=True)


# ## Measurements and feature extraction

# In[4]:


from skimage import measure

# analyse objects
table = measure.regionprops_table(label_image, intensity_image=image,
                                  properties=('area', 'mean_intensity'))


# ## Working with tables

# In[5]:


# show table
import pandas as pd
dataframe = pd.DataFrame(table)
dataframe


# ## Statistical analysis

# In[6]:


import numpy as np
print("Mean blob area is ", np.mean(dataframe['area']))


# In[ ]:




