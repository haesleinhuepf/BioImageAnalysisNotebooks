# Image deconvolution
Image deconvolution is also _just_ a special form of image filtering. We dedicate a whole chapter to it because deconvolutions play an important role in fluorescence microscopy.

We will demonstrate the principles in two dimensional images. It shall be highlighted though that deconvolution should be done in three dimensions if possible because the physical principles behind are not the same in all directions, the point spread function is typically not symmetrical in fluorescence microscopy.

## Installing requirements

We will use [RedLionFish](https://github.com/rosalindfranklininstitute/RedLionfish) and [SimpleITK](https://simpleitk.readthedocs.io/) for deconvolving images. For the ease-of-use, we will work with the latter via a convenience layer, [napari-simpleitk-image-processing](https://github.com/haesleinhuepf/napari-simpleitk-image-processing). Enter these commands in the terminal to install everything:

```
mamba install reikna pyopencl -c conda-forge
pip install redlionfish
pip install napari-simpleitk-image-processing
```

<!--
## Installing optional dependencies

In one notebook we will also use NVidia CUDA for deconvolution. If your graphics processing unit supports cuda, feel free to install [pycudadecon](https://github.com/tlambert03/pycudadecon).

```
mamba install -c conda-forge pycudadecon
```
-->

## See also
* [BioDIP Dresden, How to deconvolve images using Huygens](https://www.biodip.de/wiki/How_to_deconvolve_images_using_Huygens)