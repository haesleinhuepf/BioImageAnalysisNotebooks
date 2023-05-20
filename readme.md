# Bio-Image Analysis Notebooks
[![DOI](https://zenodo.org/badge/449194300.svg)](https://zenodo.org/badge/latestdoi/449194300)

This repository contains a collection of Python Jupyter notebooks explaining bio-image analysis to a broad audience, focusing on life-scientists working with three dimensional fluorescence microscopy for analyzing cells and tissues. The content is available at

https://haesleinhuepf.github.io/BioImageAnalysisNotebooks

It is maintained using [Jupyter lab](https://jupyterlab.readthedocs.io/en/stable/) and build using [Jupyter book](https://jupyterbook.org/intro.html).

To edit this book, install depencencies like this:

```
pip install pyclesperanto-prototype
pip install jupyterlab
pip install jupyter-book
pip install jupyterlab-spellchecker

git clone https://github.com/haesleinhuepf/BioImageAnalysisNotebooks
cd BioImageAnalysisNotebooks
jupyter lab
```

To build the book, you can run this from the same folder (tested on MacOS only):
```
chmod u+x ./build.sh
./build.sh
```

To clear the build, e.g. before committing using git, run this:
```
chmod u+x ./clean.sh
./clean.sh
```

## Acknowledgements

R.H. acknowledges support by the Deutsche Forschungsgemeinschaft under Germany’s Excellence Strategy—EXC2068–Cluster of Excellence Physics of Life of TU Dresden.
This project has been made possible in part by grant numbers 2021-240341, 2021-237734 and 2022-252520 from the Chan Zuckerberg Initiative DAF, an advised fund of the Silicon Valley Community Foundation.


