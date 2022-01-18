# Image segmentation

Image analysist refer to image segmentation when subdividing an image into multiple groups of pixels having different characteristics. 

## Binary images
The most basic way of that is binarization, turning the image into a "positive" and a "negative" region. Typically, binary images are used for that, which could for example contain two different pixel values `True` and `False` representing "positive" and "negative", respectively. Technically, every image can be interpreted as a binary image using the rationale "Every pixel is considered positive that is neither `False` nor `0`."

## Label images and regions of interest
Conceptionally, label images are an extension of binary images. In a label image, all pixels with value 0 correspond to background, a special region which is not considered as any object. Pixels with a value larger than 0 denote that the pixel belongs to an object and identifies that object with the given number. A pixel with value `1` belongs to  first object and pixels with value `2` belongs to a second object and so on. Ideally, objects are labeled subsequently, because then, the maximum intensity in a label image corresponds to the number of labeled objects in this image.
