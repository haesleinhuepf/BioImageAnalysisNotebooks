def branchoid(size:int = 100, sigma:float = 1, threshold:float = 0.5):
    """
    Creates a synthetical binary image dataset of a sphere that has other sphere-, cone- and cylinder-like structures growing out of it.
    
    Parameters
    ----------
    size:int, optional
        Width/height/depth of the resulting binary image dataset
    sigma:float, optional
        after creating the dataset, it will be blurred to potentially smooth the surface
    threshold: float, optional
        by increasing the threshold, the object volume will become larger
        
    Returns
    -------
    ndarray
    """
    import pyclesperanto_prototype as cle
    import stackview

    image = cle.create([size, size, size])
    cle.set(image, 0)
    
    cle.draw_sphere(image, size*0.5, size*0.5, size*0.5, radius_x=size*0.25, radius_y=size*0.25, radius_z=size*0.25)
    
    
    for i in range(0, 10):
    
        radius = size * (0.25 - i*0.01)

        cle.draw_sphere(image, 
                        size*0.5 + i * size * 0.02, 
                        size*0.5, 
                        size*0.5, 
                        radius_x=radius, 
                        radius_y=radius, 
                        radius_z=radius)


    for i in range(0, 10):

        radius = size * (0.15 - i*0.01)

        cle.draw_sphere(image, 
                        size*0.5, 
                        size*0.65 + i * size * 0.02, 
                        size*0.5, 
                        radius_x=radius, 
                        radius_y=radius, 
                        radius_z=radius)

    for i in range(0, 10):

        radius = size * (0.12 - i*0.01)

        cle.draw_sphere(image, 
                        size*0.35 - i * size * 0.02, 
                        size*0.65 + i * size * 0.02, 
                        size*0.5, 
                        radius_x=radius, 
                        radius_y=radius, 
                        radius_z=radius)

    for i in range(0, 10):

        radius = size * (0.05)

        cle.draw_sphere(image, 
                        size*0.35 - i * size * 0.02, 
                        size*0.5, 
                        size*0.5, 
                        radius_x=radius, 
                        radius_y=radius, 
                        radius_z=radius)

    for i in range(0, 20):

        if i < 10:
            radius = size * (0.05)
        else:
            radius = size * (0.05 + (i-10)*0.01)

        cle.draw_sphere(image, 
                        size*0.35 - i * size * 0.01, 
                        size*0.35 - i * size * 0.01, 
                        size*0.5, 
                        radius_x=radius, 
                        radius_y=radius, 
                        radius_z=radius)

    smoothed_branchoid = cle.gaussian_blur(image, sigma_x = sigma, sigma_y = sigma, sigma_z = sigma)
    return stackview.insight(cle.pull(smoothed_branchoid > 0.5))
