# Parameter optimization

In this chapter we will apply some strategies to optimize parameters of image processing workflows. 
In general, it is important to have high-quality ground truth data, such as manually segmented images. 
Furthermore, a well-engineered fitness function (sometimes also called loss-function) is necessary.
For parameter optimization we will use [scipy's optimize package](https://docs.scipy.org/doc/scipy/reference/optimize.html) and the Napari plugin [napari-workflow-optimizer](https://github.com/haesleinhuepf/napari-workflow-optimizer).
