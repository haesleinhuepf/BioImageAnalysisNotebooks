#!/usr/bin/env python
# coding: utf-8

# # Optimize segmentation / labeling

# In[1]:


from skimage.io import imread
from napari_workflow_optimizer import JaccardLabelImageOptimizer, Optimizer, Workflow
import pyclesperanto_prototype as cle


# In[2]:


w = Workflow()
# define background subtraction
w.set("deblurred", cle.gaussian_blur, "input", sigma_x=5, sigma_y=5)
# define segmentation
w.set("binarized", cle.threshold_otsu, "deblurred")
w.set("labeled", cle.label, "binarized")


# In[3]:


w.set("input", imread("blobs.tif"))
result = w.get("labeled")

cle.imshow(result, labels=True)


# In[4]:


ground_truth = imread("blobs_labeled.tif")
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

