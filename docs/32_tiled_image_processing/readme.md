# Tiled image processing

If image data is too large to fit into memory, it becomes necessary to split the image into multiple _tiles_ and process them individually. While this is step is straightforward, it can become very challenging to stitch the resulting image tiles together and return one big result image. In this section we will elaborate on multiple strategies to deal with tiled image processing.

See als
* [Dask image documentation](http://image.dask.org/en/latest/)
* [Dask examples: image processing](https://examples.dask.org/applications/image-processing.html)
