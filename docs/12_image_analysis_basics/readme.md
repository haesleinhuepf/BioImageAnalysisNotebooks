# Image analysis basics

This chapter covers image processing and image analysis basics. We will introduce what images are and how we can process them. 

## Installation of required libraries

We will be mostly using the [numpy library](https://numpy.org), [scipy](https://scipy.org/) and [scikit-image](https://scikit-image.org). For visualization, we will make use of [matplotlib](https://matplotlib.org/). You can install them using pip.

```
pip install numpy scipy scikit-image matplotlib
```

or conda:
```
conda install numpy scipy scikit-image matplotlibmatplotlib
```

We will also dive into image processing on graphics processing units using [OpenCL](https://www.khronos.org/opencl/), [pyopencl](https://documen.tician.de/pyopencl/) and [pyclesperanto](https://github.com/clesperanto/pyclesperanto_prototype). User of Windows and Mac should not need to install OpenCL. Everything you need should be pre-installed. Linux users need to install an OpenCL-ICD-Loader.

Hence, linux users may have to run commands like this, depending on the linux distribution:

```
sudo apt update
sudo apt install ocl-icd-opencl-dev
```

Afterwards, installation can proceed using conda _and_ pip:
```
conda install -c conda-forge pyopencl
pip install pyclesperanto-prototype
```

Afterwards, you can test it for example by executing these commands in a python script or jupyter notebook:
```
import pyclesperanto_prototype as cle

print("Used GPU:", cle.get_device().name)
```

Also feel free to install the [napari-pyclesperanto-assistant plugin in napari](https://clesperanto.github.io/napari_pyclesperanto_assistant/).
