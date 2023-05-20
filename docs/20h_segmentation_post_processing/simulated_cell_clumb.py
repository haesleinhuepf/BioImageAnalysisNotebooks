def simulate_data():
    """
    Simulates a 2D clumb of cells and returns a label image of them.
    """
    import pyclesperanto_prototype as cle
    
    # create a simulated more or less regular tissue
    cells = cle.artificial_tissue_2d(width=200, height=200)

    # create circle in the middle of the image
    circle = cle.create_like(cells)
    cle.set(circle, 0)
    half_size = cells.shape[-1] / 2
    cle.draw_sphere(circle, 
                    x=half_size,
                    y=half_size,
                    radius_x=half_size - 30,
                    radius_y=half_size - 30
                   )

    # keep only centroids within the circle
    centroids = cle.reduce_labels_to_centroids(cells) > 0
    constrained_centroids = cle.mask(centroids, circle)

    # increase centroids to become cell-like again
    labeled_centroids = cle.label_spots(constrained_centroids)
    clumb_of_cells = cle.dilate_labels(labeled_centroids, radius=15)

    return clumb_of_cells