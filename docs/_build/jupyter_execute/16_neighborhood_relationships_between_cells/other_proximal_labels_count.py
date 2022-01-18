#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pyclesperanto_prototype as cle

cle.get_device()


# Our starting point is a label image and another label image, where some of the labels in the first image are selected from.

# In[2]:


label_image = cle.artificial_tissue_2d()
cle.imshow(label_image, labels=True)


# In[3]:


random_vector = np.random.random((1, int(label_image.max() + 1)))
sparse_labels = cle.exclude_labels_with_values_out_of_range(random_vector, label_image, minimum_value_range=0, maximum_value_range=0.3)
cle.imshow(sparse_labels, labels=True)


# We now count for every label in `label_image`, how many labels are proximal to it in the `sparse_labels` image. For measuring the distance, we use the centroid distance.

# In[4]:


count_map = cle.proximal_other_labels_count_map(label_image, sparse_labels, maximum_distance=25)
cle.imshow(count_map)


# In[ ]:




