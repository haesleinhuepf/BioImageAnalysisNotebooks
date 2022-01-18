#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pyclesperanto_prototype as cle

cle.select_device("RTX")


# In[14]:


def generate_centroid_distance_matrix(label_image1, label_image2):
    centroids1 = cle.centroids_of_labels(label_image1)
    
    if label_image1 is label_image2:
        centroids2 = centroids1
    else:
        centroids2 = cle.centroids_of_labels(label_image1)

    return cle.generate_distance_matrix(centroids1, centroids2)


# In[15]:


image = np.asarray([[0,2,1,4,4],
                    [0,2,3,4,4]])


# In[16]:


generate_centroid_distance_matrix(image, image)


# In[ ]:




