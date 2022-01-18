#!/usr/bin/env python
# coding: utf-8

# # Introduction to image segmentation
# Image segmentation is the process of separating an image into multiple regions. 
# 
# See also
# * [Image manipulation and processing using Numpy and Scipy by Emmanuelle Gouillart and Gaël Varoquaux](https://scipy-lectures.org/advanced/image_processing/index.html#basic-image)
# * [Tutorial on image segmentation with scikit-image](https://scikit-image.org/docs/dev/user_guide/tutorial_segmentation.html)
# 
# Let's start by defining an image as a two dimensional array; a matrix.

# In[1]:


import numpy as np

image = np.asarray([
    [1, 0, 2, 1, 0, 0, 0],
    [0, 3, 1, 0, 1, 0, 1],
    [0, 5, 5, 1, 0, 1, 0],
    [0, 6, 6, 5, 1, 0, 2],
    [0, 0, 5, 6, 3, 0, 1],
    [0, 1, 2, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0]
])


# ## Image segmentation
# A very basic algorithm for separating low intensity regions from high intensity regions in the image is thresholding.
# We will now make a new image containing `True` and `False` as pixel values depending on if the original image had intensity lower or higher a given threshold. As this image has just two different pixel values, it is a binary image:

# In[2]:


threshold = 4

binary_image = image > threshold


# In[3]:


binary_image


# ## Image visualization
# For visualizing images, we use the [scikit-image](https://scikit-image.org) library.

# In[4]:


from skimage.io import imshow

imshow(image)


# In[5]:


imshow(binary_image)


# [Matplotlib](https://matplotlib.org/) might be more flexible when visualizing images, e.g. for drawing outlines around regions of interest:

# In[6]:


import matplotlib.pyplot as plt

# create a new plot
fig, axes = plt.subplots(1,1)

# add two images
axes.imshow(image, cmap=plt.cm.gray)
axes.contour(binary_image, [0.5], linewidths=1.2, colors='r')

