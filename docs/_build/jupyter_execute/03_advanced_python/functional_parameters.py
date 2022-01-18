#!/usr/bin/env python
# coding: utf-8

# # Functional parameters
# A core concept of the python language is [functional programming](https://en.wikipedia.org/wiki/Functional_programming): We define functions and apply them to our data.

# In[1]:


import numpy as np 

values = np.asarray([1, 2, 3, 4, 10])


# In[2]:


def double_number(x):
    return x * 2


# In[3]:


double_number(values)


# In python you can also have variables that contain a function and can be executed:

# In[4]:


my_function = double_number

my_function(values)


# ## Custom functional parameters
# You can also define your custom functions taking functional parameters. For example, we can define a `count_blobs` function that takes an `image` and a `threshold_algorithm`-function as parameter.

# In[5]:


import matplotlib.pyplot as plt
from skimage.measure import label

def count_blobs(image, threshold_algorithm):
    # binarize the image using a given 
    # threshold-algorithm
    threshold = threshold_algorithm(image)
    binary = image > threshold
    
    # show intermediate result
    # plt.imshow(binary)
    
    # return count blobs
    labels = label(binary)
    return labels.max()


# We now open an image and analyse it twice.

# In[6]:


from skimage.io import imread, imshow

blobs_image = imread('../../data/blobs.tif')

imshow(blobs_image)


# We now count the blobs in this image with two different algorithms we provide as parameter:

# In[7]:


from skimage.filters import threshold_otsu

count_blobs(blobs_image, threshold_otsu)


# In[8]:


from skimage.filters import threshold_yen

count_blobs(blobs_image, threshold_yen)


# ## Exercise
# Assume you want to find out which threshold algorithm works best for your image. Therefore, you may want to take a look at the image being thresholded by multiple algoritms. Define a list of threshold algorithms, e.g. from [this list](https://scikit-image.org/docs/dev/search.html?q=threshold_&check_keywords=yes&area=default). Program a for-loop that applies the threshold algorithms to the blobs image and shows the results. The result should look similar to [this example](https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_thresholding.html).

# In[ ]:




