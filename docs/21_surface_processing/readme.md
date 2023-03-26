# Surface processing

In this chapter we will process surface data. Surfaces, also known as meshes consist of points in 3D space, so called vertices, that are connected to each other forming triangles, also known as faces. Many triangles together form a surface. If the surface is closed so that no ray could go from the inside to the outside without crossing a triangle, the surface is called watertight.

## Installing requirements

We will use the [vedo](https://vedo.embl.es/) library for processing and visualizing surfaces and the programmable napari plugin [napari-process-points-and-surfaces](https://github.com/haesleinhuepf/napari-process-points-and-surfaces). Both can be installed like this:

```
mamba install vedo
pip install napari-process-points-and-surfaces
```
