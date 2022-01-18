# Image segmentation

Image analysist refer to image segmentation when subdividing an image into multiple groups of pixels having different characteristics. In this chapter we will learn basic algorithms for binarizing images, for labeling objects in images. We will also do a dive into machine learning and deep learning based image segmentation algorithms.

## Installation of requirements

As in the chapters before, we will use [scikit-image](https://scikit-image.org/), [pyclesperanto-prototype](https://github.com/clEsperanto/pyclesperanto_prototype) and [napari-simpleitk-image-processing](https://github.com/haesleinhuepf/napari-simpleitk-image-processing) for segmenting the images. Some visualization will again be done using [matplotlib](https://matplotlib.org/). 

## Installation of optional dependencies

For some short-cuts to watershed-based image segmentation algorithms, installation of the scriptable napari plugin [napari-segment-blobs-and-things-with-membranes](https://github.com/haesleinhuepf/napari-segment-blobs-and-things-with-membranes) is recommended. You can install it using pip:

```
pip install napari-segment-blobs-and-things-with-membranes
```

In the second half of this chaper, we will explore deep learning based algorithms for image segmentation. If you want to try out the tools presented there, [cellpose](https://cellpose.readthedocs.io/) and [stardist](https://github.com/stardist/stardist), you should install them, for example using pip:

```
pip install stardist numpy==1.21.5
pip install cellpose[all]
```

Mac users may have to execute the second command like this:
```
pip install "cellpose[all]"
```
