# Clustering
In this chapter we will group data points together according to their properties. We will not provide annotations the computer can learn from and thus, the methods we use here belong in the category [_unsupervised machine learning_](https://en.wikipedia.org/wiki/Unsupervised_learning).

## Explorative image data science and hypothesis generation
In this chapter, we use methods of image data exploration. None of those allows to draw conclusions directly. For example, you may conclude from one of the following notebooks that a combination of mean intensity, the variance of intensity and shape descriptors of segmented nuclei allow grouping the nuclei into groups such as _mitotic_ and _not mitotic_. The notebook's purpose was to allow you to generate this hypothesis. However, this hypothesis needs to be confirmed on a representative dataset.
The presented methods such as dimensionality reduction, scaling and clustering allow you to gain insights into relationships between parameters measured in images. For academic purposes we do this on single images. Please note that none of the shown procedures are generalizable. It is possible that applying the same notebooks to a different example images leads to different results. Whenever you plan to apply these techniques to image data, it is recommended to:
* Use measurements from multiple images
* Make sure you selected a representative set of samples from the population of data you want to understand better.
* Use the insights gained from the present explorative data analysis techniques to setup follow-up experiments to prove the presumed relationships.

## Installation
We will use the libraries [scikit-learn](https://scikit-learn.org/), [umap_learn](https://umap-learn.readthedocs.io/) and [hdbscan](https://hdbscan.readthedocs.io/). For data visualization we will be using [seaborn](https://seaborn.pydata.org/).
All can be installed using mamba/conda.

```
mamba install scikit-learn umap-learn hdbscan seaborn
```
