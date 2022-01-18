#!/usr/bin/env python
# coding: utf-8

# # Loading, processing and visualising 3D images 
# with scikit-image, numpy and matplotlib

# In[3]:


from skimage.io import imread

image = imread('../../data/Haase_MRT_tfl3d1.tif')

# print out the spatial dimensions of the image
print(image.shape)


# In[4]:


import matplotlib.pyplot as plt 

plt.imshow(image)
plt.show()


# Showing it slice by slice

# In[5]:


import matplotlib.pyplot as plt 

plt.imshow(image[0])
plt.show()

plt.imshow(image[25])
plt.show()

plt.imshow(image[50])
plt.show()

plt.imshow(image[100])
plt.show()


# Maximum projection

# In[6]:


import numpy as np

max_z = np.max(image, axis=0)
plt.imshow(max_z)
plt.show()

max_y = np.max(image, axis=1)
plt.imshow(max_y)
plt.show()

max_x = np.max(image, axis=2)
plt.imshow(max_x)
plt.show()


# In[7]:


voxel_size_x = 0.52
voxel_size_y = 0.52
voxel_size_z = 2

aspect_xz = voxel_size_z / voxel_size_x
aspect_yz = voxel_size_z / voxel_size_y

def showXYZprojection(image):
    max_z = np.max(image, axis=0)
    plt.imshow(max_z)
    plt.show()

    max_y = np.max(image, axis=1)
    plt.imshow(max_y, aspect=aspect_xz)
    plt.show()

    max_x = np.max(image, axis=2)
    plt.imshow(max_x, aspect=aspect_yz)
    plt.show()

showXYZprojection(image)


# In[ ]:




