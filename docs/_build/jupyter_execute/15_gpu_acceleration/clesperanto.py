#!/usr/bin/env python
# coding: utf-8

# # clEsperanto
# [clEsperanto](http://clesperanto.net) is a project between multiple bio-image analysis ecosystem aiming at removing language barriers. It is based on [OpenCL](https://www.khronos.org/opencl/), an open standard for programming graphics processing units (GPUs, and more) and its python wrapper [pyopencl](https://documen.tician.de/pyopencl/). Under the hood, it uses processing kernels originating from the [clij](https://clij.github.io) project.
# 
# See also
# * [GPU-accelerated image analysis in Fiji and Napari, EuroBioimaging Virtual Pub](https://www.youtube.com/watch?v=MERVnf5_QkI)
# * [pyclesperanto-prototype](https://github.com/clEsperanto/pyclesperanto_prototype)
# * [pyclesperanto API](https://clij.github.io/clij2-docs/reference__pyclesperanto)
# * [Napari pyclesperanto Assistant](https://clesperanto.github.io/napari_pyclesperanto_assistant/)
# 
# ## GPU Initialization
# We'll start with initializing checking out what GPUs are installed:

# In[1]:


import pyclesperanto_prototype as cle

# list available devices
cle.available_device_names()


# In[2]:


# select a specific device with only a part of its name
cle.select_device("2080")


# In[3]:


# check which device is uses right now
cle.get_device()


# ## Processing images
# For loading image data, we use scikit-image as usual:

# In[5]:


from skimage.io import imread, imshow

image = imread("../data/blobs.tif")
imshow(image)


# The `cle.` gateway has all methods you need, it does not have sub-packages:

# In[7]:


# noise removal
blurred = cle.gaussian_blur(image, sigma_x=1, sigma_y=1)

imshow(blurred)


# In[8]:


# binarization
binary = cle.threshold_otsu(blurred)

imshow(binary)


# In[9]:


# labeling
labels = cle.connected_components_labeling_box(binary)

# visualize results
imshow(labels)


# `cle.` also comes with an imshow function, that allows for example showing label images more conveniently:

# In[10]:


cle.imshow(labels, labels=True)


# Some of these operations, e.g. [voronoi_otsu_labeling](https://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/demo/segmentation/voronoi_otsu_labeling.ipynb) are in fact short-cuts and combine a number of operations such as Gaussian blur, Voronoi-labeling and Otsu-thresholding to go from a raw image to a label image directly:

# In[11]:


labels = cle.voronoi_otsu_labeling(image, spot_sigma=3.5, outline_sigma=1)

cle.imshow(labels, labels=True)


# Also, just a reminder, read the documentation of methods you haven't used before:

# In[12]:


print(cle.voronoi_otsu_labeling.__doc__)


# ## Interoperability 
# In pyclesperanto, images are handled in the random access memory (RAM) of your GPU. If you want to use other libraries, which process images on the GPU, the memory must be transferred back. Usually, this happens transparently for the user, e.g. when using scikit-image for measuring region properties:

# In[13]:


from skimage.measure import regionprops

statistics = regionprops(labels)

import numpy as np
np.mean([s.area for s in statistics])


# If you want to explicitly convert your image, e.g. into a numpy array, you can do it like this:

# In[14]:


np.asarray(labels)


# ## Memory management
# In jupyter noteboooks, variables are kept alive as long as the notebook kernel is running. Thus, your GPU may fill up with memory. Thus, if you don't need an image anymore, set it to `None`. It will then be remove from GPU memory thanks to [pyopencl](https://documen.tician.de/pyopencl/) magic.

# In[15]:


image = None
blurred = None
binary = None
labels = None


# ## Napari integration
# There is nothing special when using clEsperanto and napari together from jupyter notebooks. For processing 3D image data it is recommended to use a 3D-viewer such as napari:

# In[18]:


import napari

# start viewer
viewer = napari.Viewer()
napari.run()

# load image
from skimage.io import imread
image = imread("../data/Lund_000500_resampled-cropped.tif")

viewer.add_image(image)


# In[19]:


import pyclesperanto_prototype as cle

background_subtracted = cle.top_hat_box(image, radius_x=10, radius_y=10, radius_z=10)

labels = cle.voronoi_otsu_labeling(background_subtracted, spot_sigma=2, outline_sigma=1)

viewer.add_labels(labels)


# In[18]:


napari.utils.nbscreenshot(viewer)


# ## Support & feedback
# Feedback is very welcome. In case you need support, please open a thread on [image.sc](https://image.s) . Use the tags [#clEsperanto](https://image.sc/tags/clesperanto) and [@haesleinhuepf](https://github.com/haesleinhuepf/)

# In[ ]:




