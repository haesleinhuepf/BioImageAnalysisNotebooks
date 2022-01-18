#!/usr/bin/env python
# coding: utf-8

# # Working with images
# For analysing image data, we need to open them, apply filters to them, segment objects in the image and do measurements.
# 
# See also
# * [Lecture notes on scikit image by Emmanuelle Gouillart](https://scipy-lectures.org/packages/scikit-image/index.html)
# * [Histograms of images](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html)
# 
# ## Opening images
# Most images read using the [imread](https://scikit-image.org/docs/dev/api/skimage.io.html#skimage.io.imread) function. In case your image doesn't you should consult the documentation of the given file format.

# In[1]:


from skimage.io import imread

image = imread("blobs.tif")


# As shown earlier, images are just matrices of intensities. However, showing them as such is not convenient.

# In[2]:


image


# As a recap, we can show images using [imshow in scikit image](https://scikit-image.org/docs/dev/api/skimage.io.html#skimage.io.imshow).

# In[3]:


from skimage.io import imshow

imshow(image)


# ## Lookup tables (a.k.a. color maps)
# We can also change the [look-up table](https://matplotlib.org/stable/tutorials/colors/colormaps.html), a.k.a. "color map" for the visualization.

# In[5]:


imshow(image, cmap="hot")


# In[6]:


imshow(image, cmap="gray")


# ## Image statistics
# As a recap, we can use [numpy](https://numpy.org/) to determine mean intensity and standard deviation of the image, because it is just a matrix of numbers.

# In[7]:


import numpy as np
np.mean(image)


# In[8]:


np.std(image)


# The histogram of an image represents its grey value distribution. It tells us if there are bright and dark regions.

# In[9]:


number_of_bins = 256
min_max = [0,255]
histogram,bins = np.histogram(image.ravel(),number_of_bins,min_max)


# In[10]:


histogram


# In[11]:


bins


# Using matplotlibs' [hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html) function, we can visualize the histogram as plot.

# In[12]:


from matplotlib import pyplot as plt

plt.hist(image.ravel(), number_of_bins, min_max)
plt.show()


# ## Exercise
# Open the `banana020.tif` data set, visualize it in a yellowish lookup table side by side with its histogram and measure the minimum and maximum intensity of the image.

# In[ ]:




