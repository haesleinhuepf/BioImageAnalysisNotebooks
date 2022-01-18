#!/usr/bin/env python
# coding: utf-8

# # Introduction to image processing
# [Numpy](https://numpy.org) is a library for processing arrays and matrices of numerical data. Images are exactly that.
# 
# See also
# * [Image manipulation and processing using Numpy and Scipy by Emmanuelle Gouillart and Gaël Varoquaux](https://scipy-lectures.org/advanced/image_processing/index.html#basic-image)
# * [Tutorial on image segmentation with scikit-image](https://scikit-image.org/docs/dev/user_guide/tutorial_segmentation.html)
# 
# Let's start by defining an image as a two dimensional array; a matrix.

# In[1]:


raw_image_array = [
    [1, 0, 2, 1, 0, 0, 0],
    [0, 3, 1, 0, 1, 0, 1],
    [0, 5, 5, 1, 0, 1, 0],
    [0, 6, 6, 5, 1, 0, 2],
    [0, 0, 5, 6, 3, 0, 1],
    [0, 1, 2, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0]
]


# We can turn this matrix into a numpy array. Processing numpy arrays is more convenient as introduced in [lecture 02](https://github.com/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/00_Python_data_structures.pdf).

# In[2]:


import numpy as np

image = np.asarray(raw_image_array)


# In[3]:


image


# We can also create empty images containing [zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html) and [random](https://numpy.org/doc/1.16/reference/generated/numpy.random.random.html#numpy.random.random) images, which is sometimes good for playing with algorithms.

# In[4]:


image_size = (5, 10)

np.zeros(image_size)


# In[5]:


np.zeros((5, 10))


# In[6]:


np.random.random((3, 5))


# ## Pixel statistics
# Numpy also allows us to derive basic descriptive statistical measurements from images such as mean, minimum, maximum and standard deviation of intensities:

# In[7]:


np.mean(image)


# In[8]:


np.min(image)


# In[9]:


np.max(image)


# In[10]:


np.std(image)


# In[11]:


image.std()


# ## Image visualization
# For visualizing images, we use the [scikit-image](https://scikit-image.org) library.

# In[12]:


from skimage.io import imshow

imshow(image)


# In[ ]:




