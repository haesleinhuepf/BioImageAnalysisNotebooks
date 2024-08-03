# Image segmentation

Image analysts refer to image segmentation when subdividing an image into multiple groups of pixels having different characteristics. In this chapter we will learn basic algorithms for binarizing images, for labeling objects in images.

## Installation of requirements

As in the chapters before, we will use [scikit-image](https://scikit-image.org/), [pyclesperanto-prototype](https://github.com/clEsperanto/pyclesperanto_prototype) and [napari-simpleitk-image-processing](https://github.com/haesleinhuepf/napari-simpleitk-image-processing) for segmenting the images. Some visualization will again be done using [matplotlib](https://matplotlib.org/).

## Installation of optional dependencies

For some short-cuts to watershed-based image segmentation algorithms, installation of the scriptable napari plugin [napari-segment-blobs-and-things-with-membranes](https://github.com/haesleinhuepf/napari-segment-blobs-and-things-with-membranes) is recommended. You can install it using pip:

```
pip install napari-segment-blobs-and-things-with-membranes
```

See also
* [SimpleITK notebooks](https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks)
