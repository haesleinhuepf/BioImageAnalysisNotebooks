# Bio-image Analysis Notebooks
[![DOI](https://zenodo.org/badge/449194300.svg)](https://zenodo.org/badge/latestdoi/449194300)

This collection of [Python](https://www.python.org/)
[jupyter](https://jupyter.org/) notebooks are written for Python beginners who are interested in 
analyzing three dimensional images of cells and tissues acquired using modern fluorescence microscopes. It is written for biologists, biochemists and biophysicists, introducing the technical language computer scientists use when describing image segmentation, scientific computing and image data science.
Special emphasis is put on image data showing cells and nuclei forming tissues and organisms. 
Demonstrations of basic principles are done in two-dimensional image data and more sophisticated examples demonstrate the basic principles in three-dimensional image data, potentially also over time.

## Structure of this Jupyter book

The chapter of this book initially cover basics in Python and image processing. The order of the chapters reflects typical image analysis workflows, starting at image visualization, filtering and segmentation, followed by feature extraction, tabular data wrangling, statistics, plotting and data visualization. At the beginning of every chapter, basic terminology is introduced and installation instructions for the required Python libraries covered in this chapter are presented. The notebooks aim to be self-contained, self-explanatory and fully reproducible. Hence, the reader can download this Jupyter book and execute all notebooks as they are. As a general requirement, a conda environment should be present on the reader's computer as explained in the first chapter.

## Covered Python libraries
The reader may note that we start with basic python, transit towards standard libraries for image processing such as 
[scikit-image](http://scikit-image.org/) and [numpy](https://numpy.org/), and from there use increasingly GPU-acceleration libraries such as 
[pyclesperanto](https://github.com/clEsperanto/pyclesperanto_prototype). 
The more the content shifts towards three dimensional biological image processing and life-sciences specific quantitative analysis,
the more we make use of custom open source libraries. These libraries are specialized for processing imaging data showing cells and tissues acquired with fluorescence microscopy.

* [apoc](https://github.com/haesleinhuepf/apoc)
* [cupy](https://cupy.dev/)
* [dask](https://dask.org/)
* [dask-image](http://image.dask.org/en/latest/)
* [matplotlib](https://matplotlib.org/)
* [napari](https://napari.org/)
* [napari-cupy-image-processing](https://github.com/haesleinhuepf/napari-cupy-image-processing)
* [napari-segment-blobs-and-things-with-membranes](https://github.com/haesleinhuepf/napari-segment-blobs-and-things-with-membranes)
* [napari-simpleitk-image-processing](https://github.com/haesleinhuepf/napari-simpleitk-image-processing)
* [numpy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
* [pyclesperanto_prototype](https://github.com/clEsperanto/pyclesperanto_prototype)
* [pycudadecon](https://github.com/tlambert03/pycudadecon)
* [RedLionFish](https://github.com/rosalindfranklininstitute/RedLionfish/)
* [scikit-image](http://scikit-image.org/)
* [scikit-learn](https://scikit-learn.org)
* [scipy](https://scipy.org/)
* [seaborn](https://seaborn.pydata.org/)
* [SimpleITK](https://simpleitk.readthedocs.io/en/master/)
* [zarr](https://zarr.readthedocs.io/en/stable/)

## Related works

This is not the first collection of Python Jupyter notebooks and teaching materials focusing on Bio-image Analysis and related fields. There are other amazing resources, where also we learned from. Additionally, we also produced materials before which are available online and will certainly overlap with this Jupyter book.

### Written resources
For the readers who prefer written tutorials and executable Python Jupyter notebooks, the following list of resources might be of interest.

* [Guillaume Witz' Deep Learning for imaging](https://github.com/guiwitz/DLImaging)
* [Guillaume Witz' Introduction to Numpy and Pandas](https://github.com/guiwitz/NumpyPandas_course)
* [Guillaume Witz' NEUBIAS Academy @HOME: Interactive Bioimage Analysis with Python and Jupyter](https://github.com/guiwitz/neubias_academy_biapy)
* [Image Analysis Focused Interest Group of the Royal Microscopical Society (IAFIG-RMS) Python for Bioimage Analysis Course](https://github.com/IAFIG-RMS/Python-for-Bioimage-Analysis)
* [Juan Nunez-Iglesias' Using Python for Science](https://github.com/jni/using-python-for-science)
* [Robert Haase's lecture materials Applied Bio-image Analysis (2020)](https://git.mpi-cbg.de/rhaase/lecture_applied_bioimage_analysis_2020)
* [Robert Haase's & Anna Poetsch lecture materials about Bio-image Analysis, Biostatistics, Programming and Machine Learning for Computational Biology (2021)](https://github.com/BiAPoL/Bio-image_Analysis_with_Python)
* [Scikit-image's example galery](https://scikit-image.org/docs/stable/auto_examples/index.html)
* [Sreeni's Python for Microscopists](https://github.com/bnsreenu/python_for_microscopists)
* [Stefan van der Walt's Python lecture materials](https://github.com/stefanv/teaching)
* [Talley Lambert's Python introduction for microscopists](https://github.com/tlambert03/hms_pyintro2)

### Videos
Focusing on a variety of topics, there are YouTubers who upload videos about microscopy, bio-image analysis, python programming and statistics.

* [Dominik Waithe's YouTube channel about bio-image analysis and Python](https://www.youtube.com/user/odlogo)
* [iBiology YouTube channel focusing on Microscopy and bio-mage analysis](https://www.youtube.com/c/ibiology)
* [HHMI Janelia Optica Interest Group YouTube channel](https://www.youtube.com/watch?v=stiM1v0oY9c&list=PLqwpOkZ9dxzKUjBx3dyaqjv6igKhGvAOG)
* [MicroCourses YouTube channel focusing on microscopy and image formation](https://www.youtube.com/c/Microcourses/about)
* [NEUBIAS Academy YouTube channel about Bio-image Analysis tools](https://youtube.com/neubias)
* [Robert Haase's YouTube lecture on Bio-image Analysis, (Python starting at lesson 9)](https://www.youtube.com/playlist?list=PL5ESQNfM5lc7SAMstEu082ivW4BDMvd0U)
* [Sreeni's YouTube channel (formerly Python for Microscopists)](https://www.youtube.com/channel/UC34rW-HtPJulxr5wp2Xa04w)
* [StatQuest with Josh Starmer YouTube channel about statistics and machine learning](https://www.youtube.com/channel/UCtYLUTtgS3k1Fg4y5tAhLbw)

## Material origin

This repository contains Jupyter notebooks collected from multiple sources. They are maintained here to produce course materials with more streamlined relationships between contents. In case you are interested in specific topics, you may find more recent materials in the notebook source repositories.

* [apoc](https://github.com/haesleinhuepf/apoc)
* [BiaPol blog](https://github.com/biapol/blog)
* [Bio-image_Analysis_with_Python](https://github.com/BiAPoL/Bio-image_Analysis_with_Python)
* [label_neighbor_filters](https://github.com/haesleinhuepf/label_neighbor_filters)
* [lecture_applied_bioimage_analysis_2020](https://git.mpi-cbg.de/rhaase/lecture_applied_bioimage_analysis_2020)
* [napari-cupy-image-processing](https://github.com/haesleinhuepf/napari-cupy-image-processing)
* [napari-segment-blobs-and-things-with-membranes](https://github.com/haesleinhuepf/napari-segment-blobs-and-things-with-membranes)
* [napari-simpleitk-image-processing](https://github.com/haesleinhuepf/napari-simpleitk-image-processing)
* [napari-workflow-optimizer](https://github.com/haesleinhuepf/napari-workflow-optimizer)
* [napari-workflows](https://github.com/haesleinhuepf/napari-workflows)
* [on_the_fly_image_processing_napari](https://github.com/BiAPoL/on_the_fly_image_processing_napari)
* [pyclesperanto-prototype](https://github.com/clesperanto/pyclesperanto_prototype/)

## Example image data

We want to acknowledge the people who produced the images we are using for demonstration purposes in this Jupyter book.
* Anne Carpenter, Broad Institute, Boston, MA, United States
* Anne Esslinger, Alberti Lab, MPI-CBG, Germany
* Daniela Vorkel, Myers Lab, MPI-CBG / CSBD, Dresden, Germany
* David Legland, INRAE, UR BIA, Nantes, France
* Jean-Karim Hériché, Cell Biology/Biophysics Unit, EMBL Heidelberg, Germany
* Mauricio Rocha Martins, Norden Lab, MPI-CBG, Germany
* Nasreddin Abolmaali, OncoRay, TU Dresden, Germany
* Sascha M. Kuhn, Nadler Lab, MPI-CBG Dresden, Germany
* Theresa Suckert, OncoRay, University Hospital Carl Gustav Carus, TU Dresden
* Tony Collins, the creator of ImageJ for Microscopy

## License

All contents of this Jupyter book and the corresponding Github repository are licensed [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) and 
BSD3 by the [authors and contributors](https://github.com/haesleinhuepf/BioImageAnalysisNotebooks/contributors), unless mentioned otherwise.

## Contributing

If you see any issues in this book, have questions or suggestions, please open a [github issue](https://github.com/haesleinhuepf/BioImageAnalysisNotebooks/issues). Contributions of any kind (pull-requests, feedback, suggestions) are very welcome. If you send a pull-request, please make sure that you own the copyright of the materials you send. In case your materials are merged, and your contribution is more than just minor corrections and additions, you will be listed under authors and copyright holders. Also please make sure that the algorithms you present are well-explained, in the language of the target audience, and contain links to additional resources such as [Wikipedia](https://www.wikipedia.org/) pages, online videos and tutorials.

## Questions and answers

If you want to discuss lessons in this Jupyter book, have feedback and/or suggestions, please open a thread on [image.sc](https://image.sc/) and tag @haesleinhuepf.

## Work-in-progress

In January 2022 I just pulled together all these notebooks in one repository. I will now in the following months reorganize their content and streamline transitions between the topics. I'm doing this in the open because I like receiving feedback early on. If you have interesting notebooks that fit in the topic, your pull-request is very welcome. Also if you experience any issues, please [get in touch](https://github.com/haesleinhuepf/BioImageAnalysisNotebooks/issues). I'm just saying, this repository is work-in-progress and it will take some time. :-) 

Cheers,

Robert Haase

[@haesleinhuepf](https://twitter.com/haesleinhuepf)
