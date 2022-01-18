#!/usr/bin/env python
# coding: utf-8

# # Multi-channel image data
# Beyond two dimensional images which can be expressed as 2-D matrix, also higher dimensional, multi-channel images are quite common.

# In[2]:


from skimage.io import imread, imshow
image = imread('../../data/hela-cells.tif')

imshow(image)


# This visualization is not perfect as discussed [here](https://forum.image.sc/t/display-multi-channel-images-with-scikit-image/51009). We need to normalize the image first. Normalization in this context means distributing all pixel intensities between 0 and 1. We can do this by dividing the image by its maximum intensity.

# In[3]:


imshow(image / image.max())


# To understand what we see, we should take a look at the image's shape. The image is abviously 672 pixels wide, 512 pixels high and has 3 channels:

# In[4]:


image.shape


# We can visualize these three channels independently by cropping them out. Furthermore, we can arrange multiple images side-by-side using [matplotlib subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html):

# In[5]:


channel1 = image[:,:,0]
channel2 = image[:,:,1]
channel3 = image[:,:,2]

import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(15,15))

axs[0].imshow(channel1)
axs[1].imshow(channel2)
axs[2].imshow(channel3)


# Furthermore, [imshow from matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html) also takes lookup tables / color maps as parameter. See [all color maps](https://matplotlib.org/stable/tutorials/colors/colormaps.html) supported by matplotlib.

# In[6]:


fig, axs = plt.subplots(1, 3, figsize=(15,15))

axs[0].imshow(channel1, cmap='plasma')
axs[1].imshow(channel2, cmap='hsv')
axs[2].imshow(channel3, cmap='cool')


# ## Exercise
# Explore look-up tables, a.k.a. [colormaps in matplotlib](https://matplotlib.org/stable/tutorials/colors/colormaps.html) and visualize the three channels above as similar as possible to how the image is visualized in ImageJ.

# In[ ]:




