# Glossary

This glossary contains terms used throughout the jupyter book. The descriptions should be interpreted in the context of biological image analysis.

## Array

A common term for datastructures that contain multiple values. In python, two common array types are [lists](#list) and [tuples](#tuple).
Multi-dimensional arrays are also called [matrices](#matrix) and [hyperstacks](#hyperstack).

## Binarization

Binarization is the act of segmenting an image into two classes: True and False. True typically is referring to a region in the image where there are objects, also calle the foreground.
False refers to the background region where there are no objects present.

## Binary image

A binary image is an image that contains only two different intensities. Depending on the used software that can be the [boolean](#boolean) values True and False, numbers such as 0 and 1, or like in ImageJ 0 and 255. 
A common definition is to associate 0 with False and all other possible values with True.

## Boolean

A variable of type boolean can only contain two values: True or False.

## Classification

Classification is the task of categorizing things such as cells or pixels into different categories ("classes").
Classification can be achieved using simple classical methods such as the python `if` statement, and using more complext [machine learning](#machine-learning) techniques.

## Clustering

Algorithms that group objects or pixels together according to their properties are clustering algoithms. These algorithms can be used for [semantic segmentation](#semantic-segmentation) and cell [classification](#classification).

## Connected component labeling

Connected component analysis or _labeling_ is a category of algorithms that typically take binary images as input and produce [label images](#label-image).
These algorithms label neighboring pixels that are marked as objects equally. Pixels where there is connection are labeled differently.
See also [wikipedia](https://en.wikipedia.org/wiki/Connected-component_labeling).

## Convolution

Convolution is the procedure that combines an image and a filter [kernel](#kernel) to produce a new image. For every pixel, its intensity and its neighbor pixels intensities are combined as defined by the filter kernel to calculate the intensity of the corresponding pixel in the output image.

## Convolutional neural networks

Convolutional neural networks are a category of machine learning algorithms that are commonly used in image denoising, restoration and segmentation. 
These algorithms use architectures simulating the functionality of the brain to learn how to perform [regression](#regression) or [classification](#classification) tasks.

## DataFrame

A [pandas](https://pandas.pydata.org/) DataFrame is a data structure mimicking a table. 
DataFrames are commonly used by data scientists to store tabular data such as quantitative measurements to perform statistical analysis.

## Deep learning

Deep learning, often associated with Deep [convolutional neural networks](#convolutional-neural-networks), is a category of machine learning algorithms with high complexity and large architectures.
These algorithms are used in more and more scientific fields and prove outperforming classical algorithms.
On the other hand, often large amounts of training data and large computational resources are necessary to train these models.

## Feature image

Feature images are used for [pixel classification](#classification) algorithms such as [random forest classifiers](#random-forest-classifier).
Those images are produces by applying [filters](#filter) to image data.

## Filter

In image processing, a filter is an operation that takes an input image to produce an output image. Input and output images can be of different dimensionality and size.
Linear image processing filters are produced by applying [convolution](#convolution) to images.
Non-linear image processing filters combine pixel intensities in a defined local neighborhood of every pixel in a non-linear way, for example by determining the minimum, maximum or median value in this region.

## GPU

Graphics processing unit. Used for processing image data and for training machine learning algorithms, [deep learning](#deep-learning) algorithms in particular.

## Hyperstack

The term hyperstack is commonly used in image processing to describe an image data set that has more then 3 dimensions. The additional, typically non-spatial dimensions can be time, wavelength, or other information such as stored in [parametric images](#parametric-image).

## Instance segmentation

Segmentation algorithms that identify individual images, e.g. in the form of [label images](#label-image) segment instances.

## Intensity image

Intensity images are typically produced by microscopes, cameras and medical tomography devices. The intensity in the pixels of the image describe a physical measurement, e.g. of the number of photons that hit the detector during acquisition.

## Kernel

A filter kernel describes how local pixel intensities around a given pixel need to be combined using a weighted sum to [convolve](#convolution) an input image.

## Label image

A label image is an image where the pixel intensity expresses to which object the pixel belongs. 
E.g. if a pixel has intensity 1, it belongs to object 1. If a pixel has intensity 3, it belongs to object 3.
The maximum intensity in a [sequentially labeled](#sequential-labeling) image corresponds to the number of objects in the image.

## Labeling

Labeling algorithms take typically images as input and produce [label images](#label-image). In that way pixels are associated with object identities. 

## List

Lists are data structures, e.g. in Python programming, that can be changed. It is possible to add, remove and change items in the list.

## Machine learning

Machine learning is a category of algorithms that base on statistical methods for deriving models from data. 
For example an algorithm that takes manually generated image annotations from humans and manages to _learn_ from the annotations how to annotate other images is a learning machine.

## Matrix

Multi-dimensional array of values. Two-dimensional matrices can be interpreted as images. Three dimensional matrices are commonly called image stacks. Matrices of higher dimensionality are also called hyperstacks. 

## Parametric image

Parametric images, or parametric maps, are images where a given pixel intensity expresses a measurement of a given object.
For example, a pixel with value 2 in an `aspect-ratio-image` belongs to an object that is twice as long as it is wide. See also [parametric maps](data_visualization.parametric_maps).

## Pixel classification

Pixel classification is the process of categorizing pixels into multiple classes. Typically, pixel classification leads to an image expressing a [semantic segmentation](#semantic-segmentation) or to [probability maps](#probability-maps).

## Probability maps

A probability map is an image where the pixel intensity expressed the probability of the pixel belonging to a specific class or category. These images are common intermediate results of [pixel classification](#pixel-classification) algorithms.

## Random forest classifier

Supervised machine learning algorithm, commonly used for [pixel classification](pixel_classification.apoc) and [object classification](pixel_classification.apoc) in microscopy image data.

## Regionalization

Subdividing an image into multiple regions. See als [Labeling](#labeling).

## Regression

Regression in the context of machine learning is a category of algorithms attempt to reduce an observed system, e.g. a video of moving cells, to numeric values, e.g. average speed of moving cells. 
See also [regression analysis (Wikipedia)](https://en.wikipedia.org/wiki/Regression_analysis).

## Semantic segmentation

Associating pixels with a category such as "cytoplasm" or "nucleus" but not specifying which cell or nucleus. 

## Sequential labeling

Sequential labeling is a processing step that takes any [label image](#label-image) and produces another label image which fulfills a condition: Every integer pixel intensity between 0 and the maximum intensity exists.
Thus, if the image contains value 4, it is garanteed that also pixel values 1, 2 and 3 exist.
There are algorithms which only work with sequentially labeled input images.

## String

String variables in common programming languages are variables that hold text. Technically variable is an [array](#array) or characters.

## Tuple

Data structure in python containing multiple values that cannot be changed (immutable).
