#!/usr/bin/env python
# coding: utf-8

# # Differentiating nuclei according to signal intensity
# A common bio-image analysis task is differentiating cells according to their signal expression. In this example we take a two-channel image of nuclei which express Cy3 and eGFP. Visually, we can easily see that some nuclei expressing Cy3 also express eGFP, others don't. This notebook demonstrates how to differentiate nuclei segmented in one channel according to the intensity in the other channel.

# In[1]:


import pyclesperanto_prototype as cle
import numpy as np
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import pandas as pd

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
channel_cy3 = raw_image[...,0]
channel_egfp = raw_image[...,1]

# visualize
fig, axs = plt.subplots(1, 2, figsize=(15,15))
axs[0].imshow(channel_cy3, cmap='gray')
axs[1].imshow(channel_egfp, cmap='gray')


# ## Segmenting nuclei
# As the staining marks the nuclei in the Cy3 channel, it is reasonable to segment nuclei in this channel and afterwards measure the intensity in the other channel. We use [Voronoi-Otsu-Labeling](https://github.com/clEsperanto/pyclesperanto_prototype/blob/f9c9b73c1f9f194fdabdab8bd8507eb73c3ef8c9/demo/segmentation/voronoi_otsu_labeling.ipynb) for the segmentation because it is a quick and straightforward approach.

# In[4]:


# segmentation
nuclei_cy3 = cle.voronoi_otsu_labeling(channel_cy3, spot_sigma=20)

# visualize
fig, axs = plt.subplots(1, 2, figsize=(15,15))
cle.imshow(channel_cy3, plot=axs[0], color_map="gray")
cle.imshow(nuclei_cy3, plot=axs[1], labels=True)


# Firstly, we can measure the intensity in the second channel, marked with eGFP and visualize that measurement in a parametric image. In such a parametric image, all pixels inside a nucleus have the same value, in this case the mean average intensity of the cell.

# In[5]:


intensity_map = cle.mean_intensity_map(channel_egfp, nuclei_cy3)

# visualize
fig, axs = plt.subplots(1, 2, figsize=(15,15))
cle.imshow(channel_egfp, plot=axs[0], color_map="gray")
cle.imshow(intensity_map, plot=axs[1], color_map="gray")


# From such a parametric image, we can retrieve the intensity values and get them in a vector. The first item in this list has value 0 and corresponds to the intensity of the background, which is 0 in the parametric image.

# In[6]:


intensity_vector = cle.read_intensities_from_map(nuclei_cy3, intensity_map)
intensity_vector


# There is by the way also an alternative way to come to the mean intensities directly, by measuring all properties of the nuclei including position and shape. It the statistics can be further processed as [pandas](https://pandas.pydata.org/) DataFrame.

# In[7]:


statistics = cle.statistics_of_background_and_labelled_pixels(channel_egfp, nuclei_cy3)

statistics_df = pd.DataFrame(statistics)
statistics_df.head()


# The intensity vector can then be retrieved from the tabular statistics. Note: In this case, the background intensity is not 0, because we were directly reading it from the original image.

# In[8]:


intensity_vector2 = statistics['mean_intensity']
intensity_vector2


# To get an averview about the mean intensity measurement, we can use [matplotlib](https://matplotlib.org/) to plot a histogram. We ignore the first element, because it corresponds to the background intensity.

# In[9]:


plt.hist(intensity_vector2[1:])


# From such a histogram, we could conclude that objects with intensity above 50 are positive. 
# 
# ## Selecting labels above a given intensity threshold
# We next generate a new labels image with the nuclei having intensity > 50. Note, all the above steps for extracting the intensity vector are not necessary for this. We just did that to get an idea about a good intensity threshold.
# 
# The following label image show the nuclei segmented in the Cy3 channel which have a high intensity in the eGFP channel.

# In[10]:


intensity_threshold = 50

nuclei_with_high_intensity_egfg = cle.exclude_labels_with_map_values_within_range(intensity_map, nuclei_cy3, maximum_value_range=intensity_threshold)
intensity_map = cle.mean_intensity_map(channel_egfp, nuclei_cy3)

# visualize
fig, axs = plt.subplots(1, 2, figsize=(15,15))
cle.imshow(channel_egfp, plot=axs[0], color_map="gray")
cle.imshow(nuclei_with_high_intensity_egfg, plot=axs[1], labels=True)


# And we can also count those by determining the maximum intensity in the label image:

# In[11]:


number_of_double_positives = nuclei_with_high_intensity_egfg.max()
print("Number of Cy3 nuclei that also express eGFP", number_of_double_positives)


# ## References

# Some of the functions we used might be uncommon. Hence, we can add their documentation for reference.

# In[12]:


print(cle.voronoi_otsu_labeling.__doc__)


# In[13]:


print(cle.mean_intensity_map.__doc__)


# In[14]:


print(cle.read_intensities_from_map.__doc__)


# In[15]:


print(cle.statistics_of_background_and_labelled_pixels.__doc__)


# In[16]:


print(cle.exclude_labels_with_map_values_within_range.__doc__)


# In[ ]:




