#!/usr/bin/env python
# coding: utf-8

# # GPU-accelerated image processing using CUPY and CUCIM
# Processing large images with python can take time. In order to accelerate processing, graphics processing units (GPUs) can be exploited, for example using [NVidia CUDA](https://en.wikipedia.org/wiki/CUDA). For processing images with CUDA, there are a couple of libraries available. We will take a closer look at [cupy](https://cupy.dev/), which brings more general computing capabilities for CUDA compatible GPUs, and [cucim](https://github.com/rapidsai/cucim), a library of image processing specific operations using CUDA. Both together can serve as GPU-surrogate for [scikit-image](https://scikit-image.org/).
# 
# See also
# * [StackOverflow: Is it possible to install cupy on google colab?](https://stackoverflow.com/questions/49135065/is-it-possible-to-install-cupy-on-google-colab)
# * [Cucim example notebooks](https://github.com/rapidsai/cucim/blob/branch-0.20/notebooks/Welcome.ipynb)
# 
# Before we start, we need to install CUDA and CUCIM it properly. The following commands make this notebook run in Google Colab.

# In[1]:


get_ipython().system('curl https://colab.chainer.org/install | sh -')

get_ipython().system('pip install cucim')
get_ipython().system('pip install scipy scikit-image cupy-cuda100')


# In[2]:


import numpy as np
import cupy as cp
import cucim
from skimage.io import imread, imshow
import pandas as pd


# In the following, we are using image data from Paci et al shared under  the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. See also: https://doi.org/10.17867/10000140 
# 

# In[3]:


image = imread('https://idr.openmicroscopy.org/webclient/render_image_download/9844418/?format=tif')

imshow(image)


# In order to process an image using CUDA on the GPU, we need to convert it. Under the hood of this conversion, the image data is sent from computer random access memory (RAM) to the GPUs memory.

# In[4]:


image_gpu = cp.asarray(image)

image_gpu.shape


# Extracting a single channel out of the three-channel image works like if we were working with numpy. Showing the image does not work, because the CUDA image is not available in memory. In order to get it back from GPU memory, we need to convert it to a numpy array.

# In[5]:


single_channel_gpu = image_gpu[:,:,1]

# the following line would fail
# imshow(single_channel_gpu)

# get single channel image back from GPU memory and show it
single_channel = cp.asnumpy(single_channel_gpu)
imshow(single_channel)

# we can also do this with a convenience function
def gpu_imshow(image_gpu):
  image = np.asarray(image_gpu)
  imshow(image)


# ## Image filtering and segmentation
# 
# The cucim developers have re-implemented many functions from sckit image, e.g. the [Gaussian blur filter](https://docs.rapids.ai/api/cucim/stable/api.html#cucim.skimage.filters.gaussian), [Otsu Thresholding](https://docs.rapids.ai/api/cucim/stable/api.html#cucim.skimage.filters.threshold_otsu) after [Otsu et al. 1979](https://ieeexplore.ieee.org/document/4310076), [binary erosion](https://docs.rapids.ai/api/cucim/stable/api.html#cucim.skimage.morphology.binary_erosion) and [connected component labeling](https://docs.rapids.ai/api/cucim/stable/api.html#cucim.skimage.measure.label).

# In[6]:


from cucim.skimage.filters import gaussian

blurred_gpu = gaussian(single_channel_gpu, sigma=5)

gpu_imshow(blurred_gpu)


# In[7]:


from cucim.skimage.filters import threshold_otsu

# determine threshold
threshold = threshold_otsu(blurred_gpu)

# binarize image by apply the threshold
binary_gpu = blurred_gpu > threshold

gpu_imshow(binary_gpu)


# In[8]:


from cucim.skimage.morphology import binary_erosion, disk

eroded_gpu = binary_erosion(binary_gpu, selem=disk(2))

gpu_imshow(eroded_gpu)


# In[9]:


from cucim.skimage.measure import label

labels_gpu = label(eroded_gpu)

gpu_imshow(labels_gpu)


# For visualization purposes, it is recommended to turn the label image into an RGB image, especially if you want to save it to disk.

# In[10]:


from cucim.skimage.color import label2rgb

labels_rgb_gpu = label2rgb(labels_gpu)

gpu_imshow(labels_rgb_gpu)


# ## Quantitative measurements
# 
# Also quantitative measurments using [regionprops_table](https://docs.rapids.ai/api/cucim/stable/api.html#cucim.skimage.measure.regionprops_table) have been implemented in cucim. A major difference is that you need to convert its result back to numpy if you want to continue processing on the CPU, e.g. using [pandas](https://pandas.pydata.org/).

# In[11]:


from cucim.skimage.measure import regionprops_table 

table_gpu = regionprops_table(labels_gpu, intensity_image=single_channel_gpu, properties=('mean_intensity', 'area', 'solidity'))

table_gpu


# In[12]:


# The following line would fail.
# pd.DataFrame(table_gpu)

# We need to convert that table to numpy before we can pass it to pandas.
table = {item[0] : cp.asnumpy(item[1]) for item in table_gpu.items()}
pd.DataFrame(table)


# In[12]:




