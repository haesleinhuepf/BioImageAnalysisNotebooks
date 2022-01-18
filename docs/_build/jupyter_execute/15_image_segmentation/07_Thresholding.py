#!/usr/bin/env python
# coding: utf-8

# # Thresholding
# Thresholding is a technique of image segmentation. It separates a given single-channel image (or stack) into two regions: Pixels with intensity below a given threshold, also called "background" and pixels with intensity above a given threshold, "foreground". Typically those algorithms result in binary images where background intensity is 0 and foreground intensity is 1. When applying such algorithms in ImageJ, foreground pixels are 255. In scikit-image, background pixels are `False` and foreground pixels are `True`.
# 
# See also
# * [Thresholding (wikipedia)](https://en.wikipedia.org/wiki/Thresholding_(image_processing))
# * [Threshold algorithms in scikit-image](https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_thresholding.html)

# In[1]:


from skimage.io import imread
from matplotlib.pyplot import imshow

image = imread("blobs.tif")
imshow(image)


# ## Image segmentation by thresholding
# The [threshold_otsu](https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.threshold_otsu) operation delivers a number - the threshold to be applied.

# In[2]:


from skimage import filters

threshold = filters.threshold_otsu(image)
print(threshold)


# Using numpy arrays, we can apply the threshold by applying the >= operato

# In[3]:


binary_image = image >= threshold

imshow(binary_image)


# In[4]:


from skimage.morphology import binary_erosion

shrinked_objects = binary_erosion(binary_image)

imshow(shrinked_objects)


# In[5]:


import matplotlib.pyplot as plt

# create a new plot
fig, axes = plt.subplots(1,1)

# add two images
axes.imshow(image, cmap=plt.cm.gray)
axes.contour(binary_image, [0.5], linewidths=1.2, colors='r')


# To visualize a segmentation result, napari can be used.

# In[6]:


import napari

# start napari
viewer = napari.Viewer()

# add image
viewer.add_image(image)

# add binary image as labels
labels = viewer.add_labels(binary_image)


# In[7]:


napari.utils.nbscreenshot(viewer)


# In[8]:


# hide labels layer
labels.visible = False


# There is a list of [thresholding algorithms](https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_thresholding.html) available. It is possible to apply them all to your data and see differences:

# In[9]:


from skimage.filters import try_all_threshold
from matplotlib import pyplot as plt

fig, ax = try_all_threshold(image, figsize=(10, 8), verbose=False)
plt.show()


# # Exercise
# Segment blobs.tif using the Yen algorithm. Use matplotlib to draw a green outline of the segmented objects around the regions on the original image.

# In[ ]:





# Segment the image using a calculated threshold according to this equation:

# In[ ]:


threshold = mean + 2 * standard_deviation


# In[ ]:





# Visualize the resulting segmentation with a red outline on top of the original image and the green outline from above.

# In[ ]:





# Alternatively, put both segmentation results in napari and compare it there visually.

# In[ ]:




