#!/usr/bin/env python
# coding: utf-8

# # Touching object labeling

# In[2]:


import numpy as np
import pandas as pd
from skimage.io import imread, imshow
from napari_simpleitk_image_processing import threshold_otsu, median_filter, gaussian_blur, signed_maurer_distance_map,    morphological_watershed, morphological_watershed, connected_component_labeling,     touching_objects_labeling, watershed_otsu_labeling, binary_fill_holes

import pyclesperanto_prototype as cle


# In[7]:


blobs = imread('../../data/blobs.tif')
binary = threshold_otsu(blobs)
imshow(binary)


# ## Touching objects labeling

# In[8]:


touching_labels = touching_objects_labeling(binary)
cle.imshow(touching_labels, labels=True)

