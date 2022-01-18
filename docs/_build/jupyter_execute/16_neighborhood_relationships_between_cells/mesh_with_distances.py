#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyclesperanto_prototype as cle
from numpy import random
from skimage.io import imshow


# # Get a test label image

# In[2]:


pointlist = cle.push(random.random((2,25)) * 200) 
print(pointlist)


# In[3]:


labelled_spots = cle.pointlist_to_labelled_spots(pointlist)
cle.imshow(labelled_spots, labels=True)


# In[4]:


cells = cle.extend_labeling_via_voronoi(labelled_spots)
cle.imshow(cells)


# # Analyze and visualize distances between labelled objects

# In[5]:


centroids = cle.label_centroids_to_pointlist(cells)
print(centroids)


# In[6]:


distance_matrix = cle.generate_distance_matrix(centroids, centroids)
cle.imshow(distance_matrix)


# In[7]:


touch_matrix = cle.generate_touch_matrix(cells)
cle.imshow(touch_matrix)


# In[8]:


touch_distance_matrix = cle.multiply_images(touch_matrix, distance_matrix)
cle.imshow(touch_distance_matrix)


# In[9]:


distance_mesh = cle.touch_matrix_to_mesh(centroids, touch_distance_matrix)
cle.imshow(distance_mesh)


# # Sepcial meshes
# ## Mesh of touching neighbors

# In[10]:


angle_mesh = cle.touch_matrix_to_mesh(centroids, touch_matrix)
cle.imshow(angle_mesh)


# ## Mesh nearest neighbors

# In[11]:


nearest_neighbor_mesh = cle.draw_mesh_between_n_closest_labels(cells, n=1)
cle.imshow(nearest_neighbor_mesh)


# ## Meshes of proximal neighbors/

# In[12]:


close_neighbors_mesh = cle.draw_mesh_between_proximal_labels(cells, maximum_distance=25)
cle.imshow(close_neighbors_mesh)


# ## Distance meshes
# This is the same custom mesh as shown in the section on top

# In[13]:


distance_mesh = cle.draw_distance_mesh_between_touching_labels(cells)
cle.imshow(distance_mesh)


# # Angle meshes
# An angle mesh describes in which directions lines point. Angles range from -0.5pi to 0.5pi radians or -90 to 90 degrees, respectively. 90 and -90 degrees corresponds to top/bottom, 0 degrees corresponds to right to the left.

# In[14]:


angle_matrix = cle.generate_angle_matrix(centroids, centroids)
# convert
angle_matrix = cle.radians_to_degrees(angle_matrix)
# correct NaNs for visualisation

angle_matrix = cle.undefined_to_zero(angle_matrix)

cle.imshow(angle_matrix, color_map='twilight')


# In[15]:


angle_touch_matrix = cle.multiply_images(angle_matrix, touch_matrix)
angle_mesh = cle.touch_matrix_to_mesh(centroids, angle_touch_matrix)
cle.imshow(angle_mesh, color_map='twilight')


# In[ ]:





# In[ ]:




