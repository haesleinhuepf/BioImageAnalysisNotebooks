# Image deconvolution
Image deconvolution is also _just_ a special form of image filtering. We dedicate a whole chapter to it because deconvolution play a special role in fluorescent microscopy.

We will demonstrate most of the principles in two dimensional images. It shall be highlighted though that deconvolution should be done in three dimensions if possible because the physical principles behind are not the same in all directions, the point spread function is typically not symmetrical in fluorescent microscopy.

## Installing dependencies

In this section, we will use [Redlionfish](https://github.com/rosalindfranklininstitute/RedLionfish) and [SimpleITK](https://simpleitk.readthedocs.io/) for deconvolving images. For the ease-of-use, we will work with the latter via a convenience layer, [napari-simpleitk-image-processing](https://github.com/haesleinhuepf/napari-simpleitk-image-processing). Enter these commands to install everything:

```
conda install reikna pyopencl -c conda-forge
pip install redlionfish
pip install napari-simpleitk-image-processing
```

## See also
* [BioDIP Dresden, How to deconvolve images using Huygens](https://www.biodip.de/wiki/How_to_deconvolve_images_using_Huygens)


