#!/usr/bin/env python
# coding: utf-8

# # Processing images using SimpleITK

# In[1]:


import numpy as np
import pandas as pd
from skimage.io import imread, imshow
from napari_simpleitk_image_processing import threshold_otsu, median_filter, gaussian_blur, signed_maurer_distance_map,    morphological_watershed, morphological_watershed, connected_component_labeling,     touching_objects_labeling, watershed_otsu_labeling, binary_fill_holes


# In[2]:


blobs = imread('https://samples.fiji.sc/blobs.png')
imshow(blobs)


# ## Median filter

# In[3]:


imshow(median_filter(blobs, 5, 5, 0))


# # Gaussian blur

# In[4]:


imshow(gaussian_blur(blobs, 10, 10, 0))


# ## Threshold Otsu

# In[5]:


from napari_simpleitk_image_processing import threshold_otsu
binary = threshold_otsu(blobs)
imshow(binary)


# In[6]:


from napari_simpleitk_image_processing import otsu_multiple_thresholds
imshow(otsu_multiple_thresholds(blobs, number_of_thresholds=4))


# ## Distance Map

# In[7]:


distance_image = signed_maurer_distance_map(binary)
imshow(distance_image)


# ## Morphological Watershed

# In[8]:


imshow(morphological_watershed(distance_image))


# ## Connected component labeling

# In[9]:


imshow(connected_component_labeling(binary))


# ## Touching objects labeling

# In[10]:


touching_labels = touching_objects_labeling(binary)
imshow(touching_labels)


# 
# ## Watershed-Otsu-Labeling

# In[11]:


labels = watershed_otsu_labeling(blobs)
imshow(labels)


# ## Simple linear iterative clustering

# In[12]:


from napari_simpleitk_image_processing import simple_linear_iterative_clustering
imshow(simple_linear_iterative_clustering(blobs, grid_size_x=15, grid_size_y=15))


# ## Scalar image K-means clustering

# In[13]:


from napari_simpleitk_image_processing import scalar_image_k_means_clustering
imshow(scalar_image_k_means_clustering(blobs))


# ## Label post-processing

# In[14]:


from napari_simpleitk_image_processing import relabel_component
imshow(relabel_component(labels, minimumObjectSize=450))


# ## Label contours

# In[15]:


from napari_simpleitk_image_processing import label_contour
imshow(label_contour(touching_labels))


# ## Label statistics

# In[16]:


from napari_simpleitk_image_processing import label_statistics
regionprops = label_statistics(blobs, labels, None, True, True, True, True, True, True)

print(regionprops.keys())
pd.DataFrame(regionprops)


# ## Edge enhancement / edge detection

# In[17]:


from napari_simpleitk_image_processing import laplacian_filter
imshow(laplacian_filter(blobs))


# In[18]:


from napari_simpleitk_image_processing import laplacian_of_gaussian_filter
imshow(laplacian_of_gaussian_filter(blobs, sigma=20))


# In[19]:


from napari_simpleitk_image_processing import sobel
imshow(sobel(blobs))


# In[20]:


from napari_simpleitk_image_processing import gradient_magnitude
imshow(gradient_magnitude(blobs))


# In[21]:


from napari_simpleitk_image_processing import morphological_gradient
imshow(morphological_gradient(blobs))


# In[22]:


from napari_simpleitk_image_processing import standard_deviation_filter
imshow(standard_deviation_filter(blobs))


# In[23]:


from napari_simpleitk_image_processing import canny_edge_detection
imshow(canny_edge_detection(blobs))


# ## Denoising

# In[24]:


from napari_simpleitk_image_processing import bilateral_filter
imshow(bilateral_filter(blobs, radius=10))


# In[25]:


from napari_simpleitk_image_processing import binominal_blur_filter
imshow(binominal_blur_filter(blobs, repetitions=20))


# In[26]:


from napari_simpleitk_image_processing import curvature_flow_denoise
imshow(curvature_flow_denoise(blobs, number_of_iterations=150))


# In[27]:


from napari_simpleitk_image_processing import regional_maxima
imshow(regional_maxima(blobs))


# In[28]:


from napari_simpleitk_image_processing import regional_minima
imshow(regional_minima(blobs))


# ## Deconvolution

# In[29]:


kernel = np.zeros((15, 15))
kernel[7,7] = 1
kernel = gaussian_blur(kernel, variance_x=3, variance_y=3)
imshow(kernel)


# In[30]:


from napari_simpleitk_image_processing import richardson_lucy_deconvolution
imshow(richardson_lucy_deconvolution(blobs, kernel))


# In[31]:


from napari_simpleitk_image_processing import wiener_deconvolution
imshow(wiener_deconvolution(blobs, kernel))


# In[32]:


from napari_simpleitk_image_processing import tikhonov_deconvolution
imshow(tikhonov_deconvolution(blobs, kernel, regularization_constant=0.5))


# ## Background / foreground removal

# In[33]:


from napari_simpleitk_image_processing import white_top_hat
imshow(white_top_hat(blobs))


# In[34]:


from napari_simpleitk_image_processing import black_top_hat
imshow(black_top_hat(blobs))


# In[35]:


from napari_simpleitk_image_processing import h_maxima
imshow(h_maxima(blobs, height=100))


# In[36]:


from napari_simpleitk_image_processing import h_minima
imshow(h_minima(blobs, height=100))


# ## Other filters

# In[37]:


from napari_simpleitk_image_processing import rescale_intensity
rescaled = rescale_intensity(blobs)

print(rescaled.max())
imshow(rescaled)


# In[38]:


from napari_simpleitk_image_processing import adaptive_histogram_equalization
imshow(adaptive_histogram_equalization(blobs, radius_x=5, radius_y=5))


# In[39]:


from napari_simpleitk_image_processing import invert_intensity
imshow(invert_intensity(blobs))


# In[ ]:




