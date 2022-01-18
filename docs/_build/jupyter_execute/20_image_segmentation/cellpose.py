#!/usr/bin/env python
# coding: utf-8

# # Image Segmentation with CellPose
# CellPose is a deep-learning based segmentation algorithm for cells and nuclei in microscopy images.
# 
# ## Installation
# In order to use this notebook, you need to [install CellPose](https://github.com/MouseLand/cellpose#local-installation). In very short this means you should run the following command from the command line in your conda environment:
# ```
# pip install cellpose
# ```
# 
# See also
# * [Cellpose in Nature Methods](https://www.nature.com/articles/s41592-020-01018-x)
# * [Cellpose on github](https://github.com/MouseLand/cellpose)
# * [Cellpose example notebook](https://github.com/MouseLand/cellpose/blob/master/notebooks/run_cellpose.ipynb)
# 
# As usual, we start with loading an example image.

# In[1]:


from skimage.io import imread, imshow
image = imread('https://samples.fiji.sc/blobs.png')


# In[2]:


imshow(image)


# ## Loading a pretrained model
# CellPose comes with a number of pretrained models, e.g. for segmenting images showing cells or nuclei. We will just load a model for segmenting nuclei.

# In[3]:


from cellpose import models, io

model = models.Cellpose(gpu=False, model_type='nuclei')


# We let the model "evaluate" the image to produce masks of segmented nuclei.

# In[4]:


channels = [0,0] # This means we are processing single-channel greyscale images.

masks, flows, styles, diams = model.eval(image, diameter=None, channels=channels)

imshow(masks)


# ## Result visualization
# Cell / nuclei segmentation results can be checked best if the resulting label image is overlaid to the original image or by drawing outlines around segmented regions.

# In[5]:


from cellpose import plot
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,5))
plot.show_segmentation(fig, image, masks, flows[0], channels=channels)
plt.tight_layout()
plt.show()


# ## More available pretrained models
# CellPose offers a couple of pretrained models. You can print their names out like this:

# In[6]:


import cellpose
cellpose.models.urls


# In[ ]:




