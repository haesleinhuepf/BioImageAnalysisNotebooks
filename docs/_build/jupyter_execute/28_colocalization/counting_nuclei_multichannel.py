#!/usr/bin/env python
# coding: utf-8

# # Counting nuclei according to expression in multiple channels
# A common bio-image analysis task is counting cells according to their signal expression in multiple channels. In this example we take a two-channel image of nuclei which express Cy3 and eGFP. Visually, we can easily see that some nuclei expressing Cy3 also express eGFP, others don't. This notebook demonstrates how to count these groups of nuclei.

# In[1]:


import pyclesperanto_prototype as cle
import numpy as np
from skimage.io import imread, imshow
import matplotlib.pyplot as plt

cle.get_device()


# We're using a dataset published by [Heriche et al.](https://doi.org/10.1091/mbc.E13-04-0221) licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) available in the [Image Data Resource](https://idr.openmicroscopy.org/webclient/img_detail/179719/).

# In[2]:


# load file
raw_image = imread('plate1_1_013 [Well 5, Field 1 (Spot 5)].png')

# visualize
imshow(raw_image)


# First, we need to split channels ([read more](https://github.com/BiAPoL/Bio-image_Analysis_with_Python/blob/a62070dee408814cee4258758f5187f135774519/image_processing/03_multi_channel_image_data.ipynb)). After that, we can actually see that not all cells marked with Cy3 (channel 0) are also marked with eGFP (channel 1):

# In[3]:


# extract channels
channel_0 = raw_image[...,0]
channel_1 = raw_image[...,1]

# visualize
fig, axs = plt.subplots(1, 2, figsize=(15,15))
axs[0].imshow(channel_0, cmap='gray')
axs[1].imshow(channel_1, cmap='gray')


# ## Segmenting nuclei
# As the staining marks the whole nucleus in both cases, it is reasonable to segmentn nuclei in both images and then process the segmented images further. We use [Voronoi-Otsu-Labeling](https://github.com/clEsperanto/pyclesperanto_prototype/blob/f9c9b73c1f9f194fdabdab8bd8507eb73c3ef8c9/demo/segmentation/voronoi_otsu_labeling.ipynb) for the segmentation because it is a quick and straightforward approach.

# In[4]:


# segmentation
nuclei_cy3 = cle.voronoi_otsu_labeling(channel_0, spot_sigma=20)
nuclei_egfp = cle.voronoi_otsu_labeling(channel_1, spot_sigma=20)

# visualize
fig, axs = plt.subplots(1, 2, figsize=(15,15))
cle.imshow(nuclei_cy3, plot=axs[0], labels=True)
cle.imshow(nuclei_egfp, plot=axs[1], labels=True)


# The above shown label images have inside nuclei pixel intensity values that correspond to the number of the nucleus. In nucleus 1, all pixels have intensity 1. In nucleus 2, all pixels have intensity 2 and so on. Hence, from these label images, we can already determine the number of nuclei in both channels, by measuring the maximum intensity in the label images:

# In[5]:


# determine maximum in both label images
number_of_nuclei_cy3 = nuclei_cy3.max()
number_of_nuclei_egfp = nuclei_egfp.max()

# print out result
print("Nuclei Cy3 positive:", number_of_nuclei_cy3)
print("Nuclei eGFP positive:", number_of_nuclei_egfp)


# Technically, we haven't checked yet if all eGFP positive nuclei are also Cy3 positive. We can do this by determining how many eGFP positive nuclei are close by each individual Cy3 positive nucleus. Therefore, we need to set a maximum distance threshold allowing us to specify how far away centroids of nuclei are allowed to be.

# In[6]:


maximum_distance = 15 # pixels

# draw a parametric map of cell counts
count_map = cle.proximal_other_labels_count_map(nuclei_cy3, nuclei_egfp)
cle.imshow(count_map, colorbar=True)


# The `count_map` is a parametric image. We can identify all the nuclei where the count value >= 1. These are all the Cy3-positive nuclei which have at least one eGFP-positive nucleus with a centroid distance <= 15 pixels. 

# In[7]:


double_positive_nuclei = cle.exclude_labels_with_map_values_out_of_range(
    count_map, 
    nuclei_cy3, 
    minimum_value_range=1)

cle.imshow(double_positive_nuclei, labels=True)


# And we can also count those similar to shown above:

# In[8]:


number_of_double_positives = double_positive_nuclei.max()
print("Number of Cy3 positives that also express eGFP", number_of_double_positives)


# ## Visualization
# We can also use the outlines around cells which are double positive and visualize those on the original images of both channels.

# In[9]:


# determine outlines
outlines = cle.detect_label_edges(double_positive_nuclei)

# add outlines to original images. As outlines have value 1, 
# we need to multiply them to make them properly visible:
channel_0_with_outlines = cle.maximum_images(channel_0, outlines * channel_0.max())

# visualize result
cle.imshow(channel_0_with_outlines)

# let's zoom in
cle.imshow(channel_0_with_outlines.get()[400:800, 1000:1700])


# For interactive visualization, we can also use [napari](https://napari.org):

# In[10]:


# startup a viewer
import napari
viewer = napari.Viewer()

# add raw images in color to the viewer
viewer.add_image(channel_0, colormap='magenta')
viewer.add_image(channel_1, colormap='green', blending='additive')

# add labels and configure it so that we see the contours as thick lines
labels_layer = viewer.add_labels(double_positive_nuclei)
labels_layer.contour=5

# make a screenshot of the viewer
napari.utils.nbscreenshot(viewer)


# ## References

# Some of the functions we used might be uncommon. Hence, we can add their documentation for reference.

# In[11]:


print(cle.voronoi_otsu_labeling.__doc__)


# In[12]:


print(cle.proximal_other_labels_count_map.__doc__)


# In[13]:


print(cle.exclude_labels_with_map_values_out_of_range.__doc__)


# In[14]:


print(cle.detect_label_edges.__doc__)


# In[15]:


print(cle.maximum_images.__doc__)


# In[16]:


print(napari.Viewer.__doc__)


# In[17]:


print(napari.Viewer.add_image.__doc__)


# In[18]:


print(napari.Viewer.add_labels.__doc__)


# In[ ]:




