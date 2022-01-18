#!/usr/bin/env python
# coding: utf-8

# # Sequential object (re-)labeling
# 
# As mentioned above, depending on the use-case it might be important to label objects in an image subsequently. It could for example be that a post-processing algorithm for label images crashes in case we pass a label image with missing labels. Hence, we should know how to relabel an image sequentially.

# In[1]:


import numpy as np
from skimage.segmentation import relabel_sequential
import pyclesperanto_prototype as cle


# Our starting point is a label image with labels 1-5, where label 3 is not present:

# In[8]:


label_image = np.asarray([
    [1,1,2,2,0],
    [0,1,4,5,0]
])
print(label_image)
cle.imshow(label_image, labels=True)


# We can now relabel this image and remove these gaps using [scikit-image's `relabel_sequential()` function](https://scikit-image.org/docs/dev/api/skimage.segmentation.html#skimage.segmentation.relabel_sequential):

# In[13]:


relabeled, _, _ = relabel_sequential(label_image)

print(relabeled)
cle.imshow(relabeled, labels=True)


# We're entering the `_` as additional return variables as we're not interested in them. This is necessary because the `relabel_sequential` function returns three things, but we only need the first.
# 
# ## Relabeling using pyclesperanto
# Also pyclesperanto has a function relabeling label images sequentially. The result is supposed identical to the result in scikit-image. It just doesn't return the additional values.

# In[16]:


relabeled1 = cle.relabel_sequential(label_image)

print(relabeled1)
cle.imshow(relabeled1, labels=True)


# In[ ]:




