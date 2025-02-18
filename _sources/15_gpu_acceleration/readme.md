# GPU accelerated image processing

As we work often with three-dimensional image data, potentially over time, classical image processing takes quite some time. 

Hence, we will also dive into image processing on graphics processing units (GPUs) using [OpenCL](https://www.khronos.org/opencl/), [pyopencl](https://documen.tician.de/pyopencl/) and [pyclesperanto](https://github.com/clesperanto/pyclesperanto_prototype). This technology allows us to process image faster, GPU accelerated. Classical algorithms and GPU-accelerated image processing may differ in the very details but we users should not recognize that. A specific image processing operation should deliver similar results independent from how it is computed.

## Installation of requirements
User of Windows and Mac should not need to install OpenCL. Everything you need should be pre-installed. Linux users need to install an OpenCL-ICD-Loader. 

Hence, linux users may have to run commands like this, depending on the linux distribution:

```
sudo apt update
sudo apt install ocl-icd-opencl-dev
```

Afterwards, installation can proceed using conda _and_ pip:
```
mamba install -c conda-forge l pyclesperanto-prototype
```

Afterwards, you can test it for example by executing these commands in a python script or jupyter notebook:
```
import pyclesperanto_prototype as cle

print("Used GPU:", cle.get_device())
```

Also feel free to install the [napari-pyclesperanto-assistant plugin in napari](https://clesperanto.github.io/napari_pyclesperanto_assistant/).

## Installation of optional requirements

In this chapter, we will also take a look at [cupy](https://cupy.dev), an [NVidia CUDA](https://en.wikipedia.org/wiki/CUDA) based GPU-accelerated processing library and [napari-cupy-image-processing](https://github.com/haesleinhuepf/napari-cupy-image-processing), a scriptable napari plugin. These two can be installed using the following commands. This will however only work on computers that have a CUDA-compatible NVidia graphics card.

```
mamba install -c conda-forge cupy cudatoolkit=10.2
mamba install -c conda-forge napari
pip install napari-cupy-image-processing
```

Note: Depending on your CUDA installation, you may want to replace the "10.2" in the command line above with the CUDA version you installed on your computer.

See also
* [Performance of dedicated laptop GPUs versus desktop GPUs (Linus Tech Tips video)](https://www.youtube.com/watch?v=z9fk9d6pry4)
* [Cupy installation](https://docs.cupy.dev/en/stable/install.html#installing-cupy)
