#!/usr/bin/env python
# coding: utf-8

# # Optimize image segmentation / labeling with spare annotations

# In[1]:


from skimage.io import imread
from napari_workflow_optimizer import JaccardLabelImageOptimizer, Optimizer, Workflow
import pyclesperanto_prototype as cle


# In[2]:


w = Workflow()
w.set("labeled", cle.voronoi_otsu_labeling, "input", spot_sigma=1, outline_sigma=5)


# In[3]:


w.set("input", imread("blobs.tif"))
result = w.get("labeled")

cle.imshow(result, labels=True)


# In[4]:


ground_truth = imread("blobs_sparse_labels.tif")
cle.imshow(ground_truth, labels=True)


# In[5]:


jlio = JaccardLabelImageOptimizer(w)
best_param = jlio.optimize("labeled", ground_truth, maxiter=20)
jlio.set_numeric_parameters(best_param)
cle.imshow(w.get("labeled"), labels=True)


# In[6]:


import matplotlib.pyplot as plt
attempt, quality = jlio.get_plot()

plt.plot(attempt, quality)

