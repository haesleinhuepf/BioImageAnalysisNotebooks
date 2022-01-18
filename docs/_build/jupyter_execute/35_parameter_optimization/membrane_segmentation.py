#!/usr/bin/env python
# coding: utf-8

# # Segmenting cells with fluorescent membranes using Random Forest Classifiers
# 

# In[1]:


from skimage.io import imread
from napari_workflow_optimizer import JaccardLabelImageOptimizer, Workflow
import napari_segment_blobs_and_things_with_membranes as nsbatwm
import pyclesperanto_prototype as cle


# In[2]:


w = Workflow()
w.set("labeled", nsbatwm.thresholded_local_minima_seeded_watershed, "input", spot_sigma=2, outline_sigma=2)


# In[3]:


w.set("input", imread("membranes_2d.tif")) # image data source: scikit-image cells3d example, slice 28
input_image = w.get("input")
cle.imshow(input_image)


# In[4]:


result = w.get("labeled")
cle.imshow(result, labels=True)


# In[5]:


ground_truth = imread("membranes_2d_sparse_labels.tif")
cle.imshow(ground_truth, labels=True)


# In[6]:


jlio = JaccardLabelImageOptimizer(w)
jlio.get_numeric_parameters()


# In[7]:


best_param = jlio.optimize("labeled", ground_truth, maxiter=20)
jlio.set_numeric_parameters(best_param)
cle.imshow(w.get("labeled"), labels=True)


# In[8]:


import matplotlib.pyplot as plt
attempt, quality = jlio.get_plot()

plt.plot(attempt, quality)


# In[ ]:




