# To make this script run in Fiji, please activate the clij, clij2
# and clijx-assistant update sites in your Fiji. 
# Read more: 
# https://clij.github.io/
# 
# To make this script run in python, install pyclesperanto_prototype:
# conda install -c conda-forge pyopencl
# pip install pyclesperanto_prototype
# Read more: 
# https://clesperanto.net
# 
import pyclesperanto_prototype as cle

blobs_image = cle.imread("C:/structure/code/clesperanto_SIMposium/blobs.tif")

cle.imshow(blobs_image, "Blobs", False, 0, 255)

# Threshold Otsu
binary_image = cle.create_like(blobs_image)
cle.threshold_otsu(blobs_image, binary_image)

cle.imshow(binary_image, "Threshold Otsu of CLIJ2 Image of blobs.gif", False, 0.0, 1.0)

# Connected Components Labeling Box
label_image = cle.create_like(binary_image)
cle.connected_components_labeling_box(binary_image, label_image)

cle.imshow(label_image, "Connected Components Labeling Box of Threshold Otsu of CLIJ2 Image of blobs.gif", True, 0.0, 64.0)

# The following code is ImageJ specific. If you run this code from 
# Python, consider replacing this part with skimage.io.imsave
from ij import IJ
IJ.saveAs("tif","C:/structure/code/clesperanto_SIMposium/blobs_labels_clesperanto_imagej.tif");