#!/usr/bin/env python
# coding: utf-8

# # Exercise: Analyse the bending of a banana in MRI

# In[3]:


from skimage.filters import threshold_otsu, threshold_yen

data_folder = '../data/banana/'


# In[4]:


import os

# get a list of files in that folder
file_list = os.listdir(data_folder)

# filter the list so that only tif images remain
image_file_list = [file for file in file_list if file.endswith(".tif")]
image_file_list


# In[5]:


def process_image(filename, threshold_function):
    """
    Process a given image file name 
    """
    
    # load data
    from skimage.io import imread
    image = imread(filename)
    
    # segment it
    binary_image = image > threshold_function(image)
    
    from skimage.measure import label
    labels = label(binary_image)
    
    # measure radius
    from skimage.measure import regionprops
    statistics = regionprops(labels)
    areas = [s.area for s in statistics]
     
    import numpy as np
    return np.max(areas)

process_image('../data/banana/banana0026.tif', threshold_otsu)


# In[8]:


slice_areas1 = [process_image(data_folder + file, threshold_otsu) for file in image_file_list]
print(slice_areas1)


# In[9]:


slice_areas2 = [process_image(data_folder + file, threshold_yen) for file in image_file_list]
print(slice_areas2)


# In[10]:


import numpy as np
from statsmodels.graphics.agreement import mean_diff_plot

m1 = np.asarray(slice_areas1)
m2 = np.asarray(slice_areas2)

plot = mean_diff_plot(m1, m2)


# In[ ]:




