# Bio-image Analysis Notebooks
[![DOI](https://zenodo.org/badge/449194300.svg)](https://zenodo.org/badge/latestdoi/449194300)

This collection of [Python](https://www.python.org/)
[jupyter](https://jupyter.org/) notebooks are written for Python beginners who are interested in 
analysing three dimensional images acquired using modern fluorescence microscopes. 
The journey starts with Python basics and introduces general concepts of bio-image analysis. 
Special emphasis is put on image data showing cells and nuclei forming tissues and organisms. 
Demonstrations of basic principles are done in two-dimensional image data and more sophisticated examples demonstrate 
the basic principles in three-dimensional image data, potentially also over time.

The reader may note that we start with basic python, transit towards standard libraries for image processing such as 
[scikit-image](http://scikit-image.org/) and [numpy](https://numpy.org/), and from there use increasingly GPU-acceleration libraries such as 
[pyclesperanto](https://github.com/clEsperanto/pyclesperanto_prototype). 
The more the content shifts towards three dimensional biological image processing and life-sciences specific quantiative analysis,
the more we make use of custom open source libraries. These libraries are specialized for processing imaging data showing 
cells and tissues acquired with fluorescence microscopy.

## Material origin

This repository contains Jupyter notebooks collected from multiple sources. They are maintained here to produce course materials with more streamlinded relationships between contents. In case you are interested in specific topics, you may find more recent materials in the notebook source repositories.

Sources (alphabetical)
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


## License

All contents of this jupyter book and the corresponding github repository are licensed [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) and 
BSD3 by the [authors and contributors](https://github.com/haesleinhuepf/BioImageAnalysisNotebooks/contributors), unless mentioned otherwise.

## Contributing

If you see any issues in this book, have questions or suggestions, please open a [github issue](https://github.com/haesleinhuepf/BioImageAnalysisNotebooks/issues). Contributions of any kind (pull-requests, feedback, suggestions) are very welcome. If you send a pull-request, please make sure that you own the copyright of the materials you send. In case your materials are merged, and your contribution is more than just minor corrections and additions, you will be listed under authors and copyright holders. Also please make sure that the algorithms you present are well-explained and contain links to additional resources such as [Wikipedia](https://www.wikipedia.org/) pages, online videos and tutorials.

## Work-in-progress

In January 2022 I just pulled together all these notebooks in one repository. I will now in the following months reorganize their content and streamline transitions between the topics. I'm doing this in the open because I like receiving feedback early on. If you have interesting notebooks that fit in the topic, your pull-request is very welcome. Also if you experience any issues, please [get in touch](https://github.com/haesleinhuepf/BioImageAnalysisNotebooks/issues). I'm just saying, this repository is work-in-progress and it will take some time. :-) 

Cheers,

Robert Haase

[@haesleinhuepf](https://twitter.com/haesleinhuepf)
