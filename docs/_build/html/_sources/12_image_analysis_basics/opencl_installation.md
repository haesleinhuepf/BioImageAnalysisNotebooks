# OpenCL installation
Graphics processing units (GPUs) allow accelerated processing of image data, especially in three dimensions. 
[OpenCL](https://en.wikipedia.org/wiki/OpenCL) is one technology allowing to exploit GPUs for image processing.
Before we can dive into this topic, we need to install it.

## OpenCL installation in Python
For python, there exist a couple of image processing libraries using OpenCL. We will work with 
[pyopencl](https://documen.tician.de/pyopencl/) and 
[clEsperanto](https://github.com/clEsperanto/pyclesperanto_prototype). 
You can install them into your conda environment using these commands:
```
conda install -c conda-forge pyopencl
pip install pyclesperanto-prototype
```

Afterwards, you can test it for example by executing these commands in python:
```
import pyclesperanto_prototype as cle

print("Used GPU:", cle.get_device().name)
```

Also feel free to install the [napari-pyclesperanto-assistant plugin in napari](https://clesperanto.github.io/napari_pyclesperanto_assistant/).
