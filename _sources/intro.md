# Bio-image Analysis Notebooks
[![DOI](https://zenodo.org/badge/449194300.svg)](https://zenodo.org/badge/latestdoi/449194300)

This collection of [Python](https://www.python.org/)
[jupyter](https://jupyter.org/) notebooks are written for Python beginners who are interested in 
analyzing three dimensional images of cells, tissues, organoids and organisms acquired using modern fluorescence microscopes. 
Basic principles are demonstrated in two-dimensional image data and more sophisticated examples applied to three-dimensional image data and time-lapse data sets.
This book is written for biologists, biochemists and biophysicists. 
We introduce the technical language computer scientists and data scientists use when describing image segmentation, scientific computing and image data science.
In case you see room for improvement, please [create a github issue](https://github.com/haesleinhuepf/BioImageAnalysisNotebooks/issues) and/or consider [contributing](https://github.com/haesleinhuepf/BioImageAnalysisNotebooks/blob/main/CONTRIBUTING.md).

## Structure of this Jupyter book

The chapters of this book initially cover basics in Python, image processing and image analysis. 
Afterwards more advanced topics are covered including machine learning and statistics.
The order of the chapters reflects typical image analysis workflows, starting at image visualization, filtering and segmentation, followed by feature extraction, tabular data wrangling, statistics, plotting and data visualization. 
At the beginning of every chapter, basic terminology is introduced and installation instructions for the required Python libraries covered in this chapter are presented. 
The notebooks aim to be self-contained, self-explanatory and fully reproducible. 
Hence, the reader can download this Jupyter book and execute all notebooks as they are. 
As a general requirement, a conda environment should be present on the reader's computer as explained in the first chapter.

## Covered Python libraries

The notebooks cover basic python topics and afterwards transit towards standard libraries for image processing such as 
[scikit-image](http://scikit-image.org/), [scipy](https://scipy.org) and [numpy](https://numpy.org/). 
In the advanced topics we make use increasingly of GPU-acceleration libraries such as 
[pyclesperanto](https://github.com/clEsperanto/pyclesperanto_prototype) and [apoc](https://github.com/haesleinhuepf/apoc). 
The more the content shifts towards three-dimensional biological image processing and life-sciences specific quantitative analysis, 
the more we make use of custom open source libraries maintained by us and our collaborators. 

* [aicsimageio](https://github.com/AllenCellModeling/aicsimageio)
* [apoc](https://github.com/haesleinhuepf/apoc)
* [cupy](https://cupy.dev/)
* [czifile](https://pypi.org/project/czifile/)
* [dask](https://dask.org/)
* [dask-image](http://image.dask.org/en/latest/)
* [hdbscan](https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html)
* [langchain](https://python.langchain.com/en/latest/index.html)
* [matplotlib](https://matplotlib.org/)
* [napari](https://napari.org/)
* [napari-cupy-image-processing](https://github.com/haesleinhuepf/napari-cupy-image-processing)
* [napari-segment-blobs-and-things-with-membranes](https://github.com/haesleinhuepf/napari-segment-blobs-and-things-with-membranes)
* [napari-process-points-and-surfaces](https://github.com/haesleinhuepf/napari-process-points-and-surfaces)
* [napari-simpleitk-image-processing](https://github.com/haesleinhuepf/napari-simpleitk-image-processing)
* [numpy](https://numpy.org/)
* [Nyxus](https://nyxus.readthedocs.io/en/latest/)
* [OpenAI API](https://openai.com/blog/openai-api)
* [pandas](https://pandas.pydata.org/)
* [pandasql](https://github.com/yhat/pandasql/)
* [pyclesperanto_prototype](https://github.com/clEsperanto/pyclesperanto_prototype)
* [pycudadecon](https://github.com/tlambert03/pycudadecon)
* [pyncclient](https://github.com/pragmaticindustries/pyncclient)
* [pyocclient](https://github.com/owncloud/pyocclient)
* [readlif](https://github.com/nimne/readlif)
* [RedLionFish](https://github.com/rosalindfranklininstitute/RedLionfish/)
* [scikit-image](http://scikit-image.org/)
* [scikit-learn](https://scikit-learn.org)
* [scipy](https://scipy.org/)
* [seaborn](https://seaborn.pydata.org/)
* [SimpleITK](https://simpleitk.readthedocs.io/en/master/)
* [stackview](https://github.com/haesleinhuepf/stackview)
* [statsmodels](https://www.statsmodels.org/stable/index.html)
* [the-segmentation-game](https://github.com/haesleinhuepf/the-segmentation-game)
* [umap-learn](https://umap-learn.readthedocs.io/en/latest/)
* [vedo](https://vedo.embl.es/)
* [zarr](https://zarr.readthedocs.io/en/stable/)

## Bio-image Analysis GPT

This collection of Jupyter notebooks serves to create the [Bio-image Analysis GPT](https://chat.openai.com/g/g-psAohb1OY-bio-image-analysis), some chatGPT based chat bot specialized in Bio-image Analysis using Python.

## Related works

This is not the first collection of Python Jupyter notebooks and teaching materials focusing on Bio-image Analysis and related fields. There are other amazing resources, where also we learned from. Additionally, we also produced materials before which are available online and will certainly overlap with this Jupyter book.

### Written resources

For the readers who prefer written tutorials and executable Python Jupyter notebooks, the following list of resources might be of interest.

* [Guillaume Witz' Deep Learning for imaging](https://github.com/guiwitz/DLImaging)
* [Guillaume Witz' Introduction to Numpy and Pandas](https://github.com/guiwitz/NumpyPandas_course)
* [Guillaume Witz' NEUBIAS Academy @HOME: Interactive Bioimage Analysis with Python and Jupyter](https://github.com/guiwitz/neubias_academy_biapy)
* [Image Analysis Focused Interest Group of the Royal Microscopical Society (IAFIG-RMS) Python for Bioimage Analysis Course](https://github.com/IAFIG-RMS/Python-for-Bioimage-Analysis)
* [Juan Nunez-Iglesias' Using Python for Science](https://github.com/jni/using-python-for-science)
* [NEUBIAS' training resources](https://neubias.github.io/training-resources/) 
* [Pete Bankheads' Introduction to Bioimage Analysis](https://bioimagebook.github.io/) 
* [Robert Haase's lecture materials Applied Bio-image Analysis (2020)](https://git.mpi-cbg.de/rhaase/lecture_applied_bioimage_analysis_2020)
* [Robert Haase's & Anna Poetsch lecture materials about Bio-image Analysis, Biostatistics, Programming and Machine Learning for Computational Biology (2021)](https://github.com/BiAPoL/Bio-image_Analysis_with_Python)
* [Scikit-image's example galery](https://scikit-image.org/docs/stable/auto_examples/index.html)
* [Sreeni's Python for Microscopists](https://github.com/bnsreenu/python_for_microscopists)
* [Stefan van der Walt's Python lecture materials](https://github.com/stefanv/teaching)
* [Talley Lambert's Python introduction for microscopists](https://github.com/tlambert03/hms_pyintro2)
* [The Turing Way](https://the-turing-way.netlify.app/)

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

This repository contains Jupyter notebooks collected from multiple sources. 
They are maintained here to produce course materials with more streamlined relationships between contents. 
In case you are interested in specific topics, you may find more recent materials in the source repositories.

* [apoc](https://github.com/haesleinhuepf/apoc)
* [BiaPol blog](https://github.com/biapol/blog)
* [Bio-image_Analysis_with_Python](https://github.com/BiAPoL/Bio-image_Analysis_with_Python)
* [Image analysis with Python and Napari - A Helmholtz Imaging Summer Academy 2022](https://github.com/BiAPoL/HIP_Introduction_to_Napari_and_image_processing_with_Python_2022)
* [Image data science with Python and Napari course 2022 @EPFL](https://github.com/BiAPoL/Image-data-science-with-Python-and-Napari-EPFL2022)
* [label_neighbor_filters](https://github.com/haesleinhuepf/label_neighbor_filters)
* [lecture_applied_bioimage_analysis_2020](https://git.mpi-cbg.de/rhaase/lecture_applied_bioimage_analysis_2020)
* [napari-cupy-image-processing](https://github.com/haesleinhuepf/napari-cupy-image-processing)
* [napari-segment-blobs-and-things-with-membranes](https://github.com/haesleinhuepf/napari-segment-blobs-and-things-with-membranes)
* [napari-simpleitk-image-processing](https://github.com/haesleinhuepf/napari-simpleitk-image-processing)
* [napari-workflow-optimizer](https://github.com/haesleinhuepf/napari-workflow-optimizer)
* [napari-workflows](https://github.com/haesleinhuepf/napari-workflows)
* [on_the_fly_image_processing_napari](https://github.com/BiAPoL/on_the_fly_image_processing_napari)
* [pyclesperanto-prototype](https://github.com/clesperanto/pyclesperanto_prototype/)
* [Quantitative Bio-Image Analysis with Python Course 2022 at DIGS-BB / IMPRS](https://github.com/BiAPoL/Quantitative_Bio_Image_Analysis_with_Python_2022)

## Questions and answers

If you want to discuss lessons in this Jupyter book, have feedback and/or suggestions, please open a thread on [image.sc](https://image.sc/) and tag @haesleinhuepf.

## Acknowledgements

We also thank authors who shared their teaching materials openly so that we could reuse and modify them:
* Anna Poetsch, Biotec, TU Dresden
* Dominik Waithe, University of Oxford
* Guillaume Witz, University of Bern
* Johannes Müller, PoL, TU Dresden
* Laura Žigutytė, PoL, TU Dresden
* Pete Bankhead, University of Edinburgh
* Ryan George Savill, MPI-CBG Dresden / PoL, TU Dresden

We want to acknowledge the people who produced the images we are using for demonstration purposes in this Jupyter book.
* Alba Villaronga Luque, MPI-CBG Dresden
* Alexandr Khrapichev, University of Oxford, UK
* Anne Carpenter, Broad Institute, Boston, MA, United States
* Anne Esslinger, Alberti Lab, MPI-CBG, Germany
* Daniela Vorkel, Myers Lab, MPI-CBG / CSBD, Dresden, Germany
* David Legland, INRAE, UR BIA, Nantes, France
* Jean-Karim Hériché, Cell Biology/Biophysics Unit, EMBL Heidelberg, Germany
* Jesse Veenvliet, MPI-CBG Dresden
* Mauricio Rocha Martins, Norden Lab, MPI-CBG, Germany
* Nasreddin Abolmaali, OncoRay, TU Dresden, Germany
* Sascha M. Kuhn, Nadler Lab, MPI-CBG Dresden, Germany
* Theresa Suckert, OncoRay, University Hospital Carl Gustav Carus, TU Dresden
* Tony Collins, the creator of ImageJ for Microscopy

We acknowledge the financial support by the Federal Ministry of Education and Research of Germany and by Sächsische Staatsministerium für Wissenschaft, Kultur und Tourismus in the programme Center of Excellence for AI-research „Center for Scalable Data Analytics and Artificial Intelligence Dresden/Leipzig“, project identification number: ScaDS.AI
We acknowledge support by the Deutsche Forschungsgemeinschaft under Germany’s Excellence Strategy—EXC2068–Cluster of Excellence Physics of Life of TU Dresden.
This project has been made possible in part by grant numbers 2021-240341, 2021-237734 and 2022-252520 from the Chan Zuckerberg Initiative DAF, an advised fund of the Silicon Valley Community Foundation.

## License

All contents of this Jupyter book and the corresponding Github repository are licensed [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) and 
BSD3 by the [authors and contributors](https://github.com/haesleinhuepf/BioImageAnalysisNotebooks/contributors), unless mentioned otherwise.

## Contributing

Please see our [CONTRIBUTING](https://github.com/haesleinhuepf/BioImageAnalysisNotebooks/blob/main/CONTRIBUTING.md) guide for details.
