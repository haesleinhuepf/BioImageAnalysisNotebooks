# Advanced python programming

In this chapter we will take a closer look at what's possible with Python. We will dive into types, workflows, decorators and functions that take functions as parameters that take functions as parameters that take functions as parameter. If you're more interested in image analysis, you can skip this chapter for now and come back later when you see a reference pointing here. It's not mandatory to understand all the concepts here for understanding the following sections.

## Python libraries used in this chapter
Therefore, we'll be introducing other Python libraries for dealing with data and workflows, called [dask](https://dask.dev), and [joblib](https://joblib.readthedocs.io/en/latest/index.html) for parallelization. We will also take a look at the [napari-workflows](https://github.com/haesleinhuepf/napari-workflows) library which brings some convenience to knit dask and napari together. You can install them as simple as this:

```
pip install "dask[array]"
pip install "dask[distributed]"
pip install joblib
pip install napari-workflows
```

In one example we will also use [numba](https://numba.pydata.org/) for compiling python code to speedup execution. 

```
conda install numba
```
