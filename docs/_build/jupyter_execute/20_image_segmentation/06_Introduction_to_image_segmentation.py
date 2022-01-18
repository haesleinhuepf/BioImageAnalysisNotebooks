#!/usr/bin/env python
# coding: utf-8

# # Image segmentation
# Image segmentation is the process of separating an image into multiple regions. 
# 
# See also
# * [Image manipulation and processing using Numpy and Scipy by Emmanuelle Gouillart and Gaël Varoquaux](https://scipy-lectures.org/advanced/image_processing/index.html#basic-image)
# * [Tutorial on image segmentation with scikit-image](https://scikit-image.org/docs/dev/user_guide/tutorial_segmentation.html)
# 
# Let's start again by defining an image as a two dimensional array and visualize it using pyclesperanto.

# In[5]:


import numpy as np
from pyclesperanto_prototype import imshow


# In[6]:


image = np.asarray([
    [1, 0, 2, 1, 0, 0, 0],
    [0, 3, 1, 0, 1, 0, 1],
    [0, 5, 5, 1, 0, 1, 0],
    [0, 6, 6, 5, 1, 0, 2],
    [0, 0, 5, 6, 3, 0, 1],
    [0, 1, 2, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0]
])


# In[7]:


imshow(image, colorbar=True)


# ## Binary images
# The most basic way of that is binarization, turning the image into a "positive" and a "negative" region. Typically, binary images are used for that, which could for example contain two different pixel values `True` and `False` representing "positive" and "negative", respectively. Technically, every image can be interpreted as a binary image using the rationale "Every pixel is considered positive that is neither `False` nor `0`."
# 
# ## Image thresholding
# A very basic algorithm for separating low intensity regions from high intensity regions in the image is thresholding.
# We will now make a new image containing `True` and `False` as pixel values depending on if the original image had intensity lower or higher a given threshold. As this image has just two different pixel values, it is a binary image:

# In[8]:


threshold = 4

binary_image = image > threshold


# In[9]:


binary_image


# In[10]:


imshow(binary_image)


# [Matplotlib](https://matplotlib.org/) might be more flexible when visualizing images, e.g. for drawing outlines around regions of interest:

# In[11]:


import matplotlib.pyplot as plt

# create a new plot
fig, axes = plt.subplots(1,1)

# add two images
axes.imshow(image, cmap=plt.cm.gray)
axes.contour(binary_image, [0.5], linewidths=1.2, colors='r')


# In[ ]:




