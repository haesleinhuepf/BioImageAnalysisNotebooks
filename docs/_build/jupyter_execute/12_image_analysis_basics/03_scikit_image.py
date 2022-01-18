#!/usr/bin/env python
# coding: utf-8

# # scikit-image for processing images

# Opening images

# In[1]:


from skimage.io import imread

image = imread("blobs.tif")


# Showing images

# In[2]:


import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()


# In[5]:


plt.imshow(image, cmap="hot")
plt.show()


# In[6]:


plt.imshow(image, cmap="gray")
plt.show()


# # Filters

# In[16]:


from skimage import filters

# Gaussian blur
gaussian_blurred_image = filters.gaussian(image, 5)
plt.imshow(gaussian_blurred_image)
plt.show()

# LoG
laplacian_of_gaussian = filters.laplace(gaussian_blurred_image)
plt.imshow(laplacian_of_gaussian)
plt.show()

# another Gaussian blur
gaussian_blurred_image_2 = filters.gaussian(image, 10)
plt.imshow(gaussian_blurred_image_2)
plt.show()

# DoG
difference_of_gaussian = gaussian_blurred_image - gaussian_blurred_image_2
plt.imshow(difference_of_gaussian)
plt.show()


# Some images ask for a structuring element "selem", for example "disc" with a given radius:

# In[44]:


from skimage.morphology import disk

median_filtered = filters.median(image, disk(5))
plt.imshow(median_filtered)
plt.show()


# In[ ]:





# The threshold_otsu operation delivers a number - the threshold to be applied

# In[29]:


from skimage import filters

threshold = filters.threshold_otsu(blurred_image)
print(threshold)


# Using numpy arrays, we can apply the threshold by applying the >= operato

# In[30]:


thresholded_image = blurred_image >= threshold

plt.imshow(thresholded_image)
plt.show()


# Postprocessing operations, to refine binary masks, can be found in the morphology package

# In[31]:


from skimage import morphology

eroded_binary_image = morphology.binary_erosion(thresholded_image)

plt.imshow(eroded_binary_image)
plt.show()


# # Connected components analysis

# In[32]:


from skimage import measure

# run connected components analysis
label_image = measure.label(thresholded_image)

plt.imshow(label_image)
plt.show()


# # Feature extraction
# To read out properties from regions, we use the regionprops_table function:

# In[45]:


from skimage import measure

# analyse objects
table = measure.regionprops_table(label_image)

# show table
table

This function also allows us to specify what we want to measure:
# In[46]:


from skimage import measure

# analyse objects
table = measure.regionprops_table(label_image, properties=('area', 
                                                           'centroid',
                                                           'orientation',
                                                           'major_axis_length',
                                                           'minor_axis_length'))

# show table
table


# We can access this table like a dictionary containing arrays, e.g. to derive the mean of the colum "area":

# In[48]:


from skimage import measure
import numpy as np

# analyse objects
table = measure.regionprops_table(label_image, properties=('area',))

# measure mean area
np.mean(table['area'])


# In[ ]:




