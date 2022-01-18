#!/usr/bin/env python
# coding: utf-8

# ## Interoperability with NetworkX and iGraph
# The graph / network analysis libraries [networkx](https://networkx.org/) and [igraph](https://igraph.org/) offer powerful tools for analysing graph data structures. To process pyclesperanto neighborhood adjacency graphs in these libraries, we can convert those matrixes using the two clesperanto functions `to_networkx` and `to_igraph`.

# In[1]:


import pyclesperanto_prototype as cle
import igraph
import networkx
from skimage.io import imread, imsave, imshow
import numpy as np
import matplotlib.pyplot as plt

cle.select_device("amd")


# We start by labeling an image...

# In[2]:


blobs = cle.imread('https://samples.fiji.sc/blobs.png')
labels = cle.voronoi_otsu_labeling(blobs, spot_sigma=4)
cle.imshow(labels, labels=True)


# ... and visualizing a graph of proximal objects which have a maximum centroid distance of 50 pixels.

# In[3]:


mesh = cle.draw_mesh_between_proximal_labels(labels, maximum_distance=50)
cle.imshow(mesh)


# ## igraph
# We can also retrieve an analogous igraph graph directly from the label image

# In[4]:


igraph_graph = cle.proximal_labels_to_igraph(labels, maximum_distance=50)

fig, ax = plt.subplots()
igraph.plot(igraph_graph, target=ax)


# Note: The visualization is flipped because the origin of the coordinate system is on the bottom left, while in clesperanto it's on the top left, because clesperanto uses community standards from the image processing field.

# ## networkx
# The same also works with networkx.

# In[5]:


networkx_graph = cle.proximal_labels_to_networkx(labels, maximum_distance=50)

pos = networkx.get_node_attributes(networkx_graph,'pos')

networkx.draw(networkx_graph, pos)


# ## n-nearest neighbors
# We can alternatively also create networks between n-nearest neighbors for all

# In[6]:


igraph_graph = cle.n_nearest_labels_to_igraph(labels, n=3)

fig, ax = plt.subplots()
igraph.plot(igraph_graph, target=ax)


# In[7]:


networkx_graph = cle.n_nearest_labels_to_networkx(labels, n=3)

pos = networkx.get_node_attributes(networkx_graph,'pos')

networkx.draw(networkx_graph, pos)


# ## touching neighbors
# Starting from a label image where neighbors touch, we can also generate graphs between those.

# In[8]:


touching_labels = cle.dilate_labels(labels, radius=5)

cle.imshow(touching_labels, labels=True)


# In[9]:


igraph_graph = cle.touching_labels_to_igraph(touching_labels)

fig, ax = plt.subplots()
igraph.plot(igraph_graph, target=ax)


# In[10]:


networkx_graph = cle.touching_labels_to_networkx(touching_labels)

pos = networkx.get_node_attributes(networkx_graph,'pos')

networkx.draw(networkx_graph, pos)


# # How it works
# The process under the hood involves the following steps:

# In[11]:


# extract centroid positions
centroids = cle.centroids_of_labels(labels)

# determine a distance matrix
distance_matrix = cle.generate_distance_matrix(centroids, centroids)

# threshold the distance matrix
adjacency_matrix = cle.generate_proximal_neighbors_matrix(distance_matrix, max_distance=50)

# generate a mesh from centroid positions and the adjacency matrix
mesh = cle.touch_matrix_to_mesh(centroids, adjacency_matrix, cle.create_like(blobs))

cle.imshow(mesh)


# The key data structure for interoperating with NetworkX and iGraph is the `adjacency_matrix`, a square matrix where all labels are represented on the X and Y axis. If there is a white pixel in this matrix, that means that these two labels are connected in the graph. Note: Also connections to background are part of this matrix, and per definition, no label is _proximal_ to the background, because the centroid of background is not determined. Also important are the `centroids`, an 2D array with positions of the centroids of the labels in 2D or 3D coordinates.

# In[12]:


cle.imshow(adjacency_matrix)


# In[13]:


print(centroids.shape)


# In[14]:


print(centroids)


# # NetworkX
# The [networkx](https://networkx.org/) library has support for [reading graphs from adjacency matrices](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_numpy_matrix.html) and for  [drawing graphs](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.nx_pylab).

# In[15]:


networkx_graph = cle.to_networkx(adjacency_matrix, centroids)

pos = networkx.get_node_attributes(networkx_graph,'pos')

networkx.draw(networkx_graph, pos)


# Note: The visualization is flipped because the origin of the coordinate system is on the bottom left, while in clesperanto it's on the top left, because clesperanto uses community standards from the image processing field.

# # igraph
# The [igraph](https://igraph.org/) library also has support for [converying graphs from adjacency matrices and for [drawing graphs](https://igraph.org/python/tutorial/0.9.7/visualisation.html) 

# In[16]:


igraph_graph = cle.to_igraph(adjacency_matrix, centroids)


# In[17]:


fig, ax = plt.subplots()
igraph.plot(igraph_graph, target=ax)


# As you can see, the igraph is directed. To make it direct in both direction along all edges, you can convert the adjacency matrix before passing it to `to_igraph`:

# In[18]:


bidirectional_matrix = cle.touch_matrix_to_adjacency_matrix(adjacency_matrix)
cle.set_where_x_equals_y(bidirectional_matrix, 0)

igraph_graph = cle.to_igraph(bidirectional_matrix, centroids)
fig, ax = plt.subplots()
igraph.plot(igraph_graph, target=ax)


# # Documentation

# In[19]:


print(cle.to_networkx.__doc__)


# In[20]:


print(cle.to_igraph.__doc__)


# In[ ]:




