# Tiled image processing

If image data is too large to fit into memory, it becomes necessary to split the image into multiple _tiles_ and process them individually. While this step is straightforward, it can become very challenging to stitch the resulting image tiles together and return one big result image. In this section we will elaborate on multiple strategies to deal with tiled image processing. The [dask library](https://docs.dask.org/en/stable/) enables processing tiled images easy to use. This chapter starts with a complete workflow showing dask in action and then explains the individual steps for setting up a proper workflow for processing your data afterwards.

See also
* Genevieve Buckley's talk about ["dask-image: distributed image processing for large data" ](https://www.youtube.com/watch?v=MpjgzNeISeI&t=1359s) (PyConline AU 2020) [Slides](https://genevievebuckley.github.io/dask-image-talk-2020/)
* John Kirkham's talk about ["dask image:A Library for Distributed Image Processing"](https://www.youtube.com/watch?v=XGUS174vvLs) (SciPy 2019)
* [Dask documentation](https://docs.dask.org/en/stable/)
* [Dask image documentation](http://image.dask.org/en/latest/)
* [Dask examples: image processing](https://examples.dask.org/applications/image-processing.html)
* https://github.com/VolkerH/DaskFusion