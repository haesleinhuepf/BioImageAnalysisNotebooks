# Deep Learning based image segmentation

In this chapter, we will use deep learning based algorithms for image segmentation. 

## Installation of requirements

For using [cellpose](https://cellpose.readthedocs.io/) and [stardist](https://github.com/stardist/stardist), these dependencies must be installed:

```
mamba install cellpose pytorch=1.8.2 cudatoolkit=10.2 -c pytorch-lts
pip install tensorflow
pip install stardist
```

The notebooks in this folder have been tested using 
* `torch==2.0.1`
* `stardist==0.8.3`
* `tensorflow==2.12.0`
* `csbdeep==0.7.3`
* `cellpose==2.2.1`
