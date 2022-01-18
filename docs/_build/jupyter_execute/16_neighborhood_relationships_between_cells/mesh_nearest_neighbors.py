#!/usr/bin/env python
# coding: utf-8

# # Mesh nearest neighbors
# In this notebook, we draw connections between nearest neighbors

# In[1]:


import pyclesperanto_prototype as cle
from numpy import random
from skimage.io import imshow


# In[2]:


pointlist = cle.push(random.random((2,25)) * 100) 
print(pointlist)


# In[3]:


labelled_spots = cle.pointlist_to_labelled_spots(pointlist)
cle.imshow(labelled_spots, labels=True)


# In[4]:


cells = cle.extend_labeling_via_voronoi(labelled_spots)
membranes = cle.detect_label_edges(cells)
cle.imshow(membranes)


# In[5]:


nearest_neighbors_mesh = cle.draw_mesh_between_n_closest_labels(cells, n=1)
cle.imshow(nearest_neighbors_mesh)


# In[6]:


two_nearest_neighbors_mesh = cle.draw_mesh_between_n_closest_labels(cells, n=2)
cle.imshow(two_nearest_neighbors_mesh)


# In[7]:


three_nearest_neighbors_mesh = cle.draw_mesh_between_n_closest_labels(cells, n=3)
cle.imshow(three_nearest_neighbors_mesh)


# In[8]:


four_nearest_neighbors_mesh = cle.draw_mesh_between_n_closest_labels(cells, n=4)
cle.imshow(four_nearest_neighbors_mesh)


# In[9]:


ten_nearest_neighbors_mesh = cle.draw_mesh_between_n_closest_labels(cells, n=10)
cle.imshow(ten_nearest_neighbors_mesh)


# In[ ]:




