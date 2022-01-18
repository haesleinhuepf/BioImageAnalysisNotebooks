#!/usr/bin/env python
# coding: utf-8

# # Object segmentation on OpenCL-compatible GPUs
# APOC is based on [pyclesperanto](https://github.com/clEsperanto/pyclesperanto_prototype) and [sklearn](https://scikit-learn.org/stable/). For object segmentation, it uses a pixel classifier and connected components labeling.
# 
# Let's start with loading an example image and some ground truth:

# In[1]:


from skimage.io import imread, imshow, imsave
import pyclesperanto_prototype as cle
import numpy as np
import apoc

image = imread('blobs.tif')
imshow(image)


# In[2]:


if False: # you can use this to make manual annotations
    import napari

    # start napari
    viewer = napari.Viewer()
    napari.run()

    # add image
    viewer.add_image(image)

    # add an empty labels layer and keep it in a variable
    labels = np.zeros(image.shape).astype(int)
    viewer.add_labels(labels)
else:
    labels = imread('annotations.tif')


# In[3]:


#imsave('annotations.tif', labels)
manual_annotations = labels

from skimage.io import imshow
imshow(manual_annotations, vmin=0, vmax=3)


# ## Training
# We now train a ObjectSegmenter, which is under the hood a [scikit-learn RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html). After training, the classifier will be converted to [clij-compatible OpenCL code](https://github.com/clEsperanto/clij-opencl-kernels) and save to disk under a given filename.

# In[4]:


# define features
features = apoc.PredefinedFeatureSet.medium_quick.value

# this is where the model will be saved
cl_filename = 'my_model.cl'

apoc.erase_classifier(cl_filename)
clf = apoc.ObjectSegmenter(opencl_filename=cl_filename, positive_class_identifier=2)
clf.train(features, manual_annotations, image)


# ## Prediction / segmentation
# The classifier can then be used to classify all pixels in the given image. Starting point is again, the feature stack. Thus, the user must make sure that the same features are used for training and for prediction. Prediction can be done on the CPU using the original scikit-learn code and on the GPU using the generated OpenCL-code. OCLRFC works well if both result images look identical.

# In[5]:


segmentation_result = clf.predict(features=features, image=image)
cle.imshow(segmentation_result, labels=True)


# # Segmentation from a loaded segmenter

# In[6]:


clf = apoc.ObjectSegmenter(opencl_filename=cl_filename)

segmentation_result = clf.predict(image=image)
cle.imshow(segmentation_result, labels=True)


# ## Next: Object classification

# In[7]:


annotation = cle.push(imread('label_annotation.tif'))


# In[8]:


features = 'area,mean_max_distance_to_centroid_ratio,standard_deviation_intensity'

# Create an object classifier
classifier = apoc.ObjectClassifier("object_classifier.cl")

# train it
classifier.train(features, segmentation_result, annotation, image)

# determine object classification
classification_result = classifier.predict(segmentation_result, image)

imshow(classification_result)


# In[ ]:





# In[ ]:




