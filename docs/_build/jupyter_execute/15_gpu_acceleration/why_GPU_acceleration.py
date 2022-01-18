#!/usr/bin/env python
# coding: utf-8

# # Why GPU-acceleration makes sense
# In this notebook we demonstrate speedup through GPU-acceleration using a Gaussian blur filter. We'll be using the [clEsperanto](https://github.com/clEsperanto/pyclesperanto_prototype/) library which uses [OpenCL](https://www.khronos.org/opencl/) and is compatible to a wide range of Intel, AMD and NVidia GPUs. Feel free to run it on your GPU and measure the speedup!
# 
# See also
# * [clEsperanto benchmarking noteboosk](https://github.com/clEsperanto/pyclesperanto_prototype/#benchmarking)
# * [cupy](https://cupy.dev/)
# * [cucim](https://github.com/rapidsai/cucim)
# 
# **Note:** benchmarking results vary heavily depending on image size, kernel size, used operations, parameters and used hardware. Use this notebook to adapt it to your use-case scenario and benchmark on your target hardware. If you have different scenarios or use-cases, you are very welcome to submit your notebook as pull-request!

# In[1]:


import pyclesperanto_prototype as cle
from skimage import filters
import time

# to measure kernel execution duration properly, we need to set this flag. It will slow down exection of workflows a bit though
cle.set_wait_for_kernel_finish(True)

# selet a GPU with the following in the name. This will fallback to any other GPU if none with this name is found
cle.select_device('RTX')


# In[2]:


# test data
import numpy as np

from skimage.io import imread
test_image = imread('Lund_000500_resampled-cropped.tif')

sigma = 10


# In[3]:


# convolve with scikit-image
result_image = None

for i in range(0, 10):
    start_time = time.time()
    result_image = filters.gaussian(test_image, output=result_image, sigma=sigma)
    print("skimage Gaussian duration: " + str(time.time() - start_time))
    


# In[4]:


# convolve with pyclesperanto
result_image_gpu = None

test_image_gpu = cle.push(test_image)

for i in range(0, 10):
    start_time = time.time()
    result_image_gpu = cle.gaussian_blur(test_image_gpu, result_image_gpu, sigma_x=sigma, sigma_y=sigma, sigma_z=sigma)
    print("pyclesperanto Gaussian duration: " + str(time.time() - start_time))


# Let's just check if the results look similar

# In[5]:


import napari

viewer = napari.Viewer()
napari.run()


# In[6]:


viewer.add_image(test_image)
viewer.add_image(result_image)
viewer.add_image(result_image_gpu)


# In[7]:


napari.utils.nbscreenshot(viewer)


# In[ ]:




