#!/usr/bin/env python
# coding: utf-8

# # Quantitative maps from neighbor statistics

# In[1]:


import pyclesperanto_prototype as cle
import numpy as np
from numpy import random
from skimage.io import imshow, imread
import matplotlib


# In[2]:


# Image data source Ignacio Arganda-Carreras, https://imagej.net/File:MorphoLibJ-region-adjacency-graph.png
intensity_image = imread('MorphoLibJ_example_image.tif')
imshow(intensity_image)


# # Starting point: Label map

# In[3]:


binary = cle.binary_not(cle.threshold_otsu(intensity_image))
cells = cle.voronoi_labeling(binary)

cle.imshow(cells, labels=True)


# ## Nearest neighbor distance maps

# In[4]:


average_distance_of_n_closest_neighbors_map = cle.average_distance_of_n_closest_neighbors_map(cells, n=1)
cle.imshow(average_distance_of_n_closest_neighbors_map, color_map='jet')


# In[5]:


average_distance_of_n_closest_neighbors_map = cle.average_distance_of_n_closest_neighbors_map(cells, n=5)
cle.imshow(average_distance_of_n_closest_neighbors_map, color_map='jet')


# ## Touching neighbor distance map

# In[6]:


average_neighbor_distance_map = cle.average_neighbor_distance_map(cells)
cle.imshow(average_neighbor_distance_map, color_map='jet')


# ## Shape descriptors: Area

# In[7]:


pixel_count_map = cle.label_pixel_count_map(cells)
cle.imshow(pixel_count_map, color_map='jet')


# ## Shape descriptors: Extension ratio

# In[8]:


maximum_extension_ratio_map = cle.label_maximum_extension_ratio_map(cells)
cle.imshow(maximum_extension_ratio_map, color_map='jet')


# In[ ]:




