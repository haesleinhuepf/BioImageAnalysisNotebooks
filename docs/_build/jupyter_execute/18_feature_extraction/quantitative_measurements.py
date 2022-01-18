#!/usr/bin/env python
# coding: utf-8

# # Quantitative image analysis
# After segmenting and labeling objects in an image, we can measure properties of these objects.
# 
# See also
# * [SciPy lecture notes: Measuring region properties](https://scipy-lectures.org/packages/scikit-image/index.html#measuring-regions-properties)
# * [Plot regionprops](https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_regionprops.html)
# 
# Before we can do measurements, we need an `image` and a corresponding `label_image`. Therefore, we recapitulate filtering, thresholding and labeling:

# In[1]:


# load image
from skimage.io import imread
image = imread("blobs.tif")

# denoising
from skimage import filters
blurred_image = filters.gaussian(image, sigma=1)

# binarization
threshold = filters.threshold_otsu(blurred_image)
thresholded_image = blurred_image >= threshold

# labeling
from skimage import measure
label_image = measure.label(thresholded_image)

# visualization
from matplotlib.pyplot import imshow
imshow(label_image)


# # Measurements / region properties
# To read out properties from regions, we use the [regionprops](https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.regionprops) function:

# In[2]:


from skimage import measure

# analyse objects
properties = measure.regionprops(label_image, intensity_image=image)


# The results are stored as `RegionProps` objects, which are not very informative:

# In[3]:


properties[0:5]


# We can reorganize the measurements into a dictionary containing arrays. We introduced them earlier as [tables](https://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/06_Dictionaries_and_tables.ipynb):

# In[4]:


statistics = {
    'area':       [p.area               for p in properties],
    'mean':       [p.mean_intensity     for p in properties],
    'major_axis': [p.major_axis_length  for p in properties]
}

statistics


# You can also add custom columns by computing your own metric, for example the `aspect_ratio`:

# In[5]:


statistics['aspect_ratio'] = [p.major_axis_length / p.minor_axis_length for p in properties]


# Reading those dictionaries of arrays is not very convenient. Thus, we use the [pandas library]() which is a common asset for data scientists.

# In[6]:


import pandas as pd

dataframe = pd.DataFrame(statistics)
dataframe


# Those dataframes can be saved to disk conveniently:

# In[7]:


dataframe.to_csv("blobs_analysis.csv")


# Furthermore, one can measure properties from our `statistics` table using [numpy](https://numpy.org/doc/stable/). For example the mean area:

# In[8]:


import numpy as np

# measure mean area
np.mean(statistics['area'])


# # Exercises
# Analyse the loaded blobs `image`. 

# * How many objects are in it?

# In[ ]:





# * How large is the largest object?

# In[ ]:





# * What are mean and standard deviation of the image?

# In[ ]:





# * What are mean and standard deviation of the area of the segmented objects?

# In[ ]:




