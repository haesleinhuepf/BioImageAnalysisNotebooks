import numpy as np


def add_background(image):
    # Create coordinates
    x_grid, y_grid = np.meshgrid(np.linspace(0, 1, 60), np.linspace(0, 1, 60))
    
    # Create image gradient and normalize to max intensity range 
    gradient_image = (x_grid + y_grid) * image.max() / 2

    return image + gradient_image

def apply_threshold_range(image, step=5):
    # Get min and max values (rounded to integers)
    min_val = int(np.floor(image.min()))
    max_val = int(np.ceil(image.max()))
    
    # Create binary masks for each threshold
    binary_masks = []
    for threshold in range(min_val, max_val + 1, step):
        binary_mask = image > threshold
        binary_masks.append(binary_mask)

    return np.asarray(binary_masks)

def generate_feature_stack(image, feature_names):
    from skimage import filters
    from skimage.morphology import white_tophat
    from skimage.morphology import disk
    import warnings

    # collect features in a stack
    feature_stack = []
    for fn in feature_names:
        fn = fn.replace(")","")
        numeric_parameter = float(fn.split("(")[-1]) if "(" in fn else 0
        if fn == "original":
            feature_stack.append(image)
        elif fn == "sobel":
            feature_stack.append(filters.sobel(image))
        elif fn == "laplace":
            feature_stack.append(filters.laplace(image))
        elif fn.startswith("top_hat"):
            feature_stack.append(white_tophat(image, disk(numeric_parameter)))
        elif fn.startswith("gaussian_sobel"):
            feature_stack.append(filters.sobel(filters.gaussian(image, sigma=numeric_parameter)))
        elif fn.startswith("gaussian_laplace"):
            feature_stack.append(filters.laplace(filters.gaussian(image, sigma=numeric_parameter)))
        elif fn.startswith("gaussian"):
            feature_stack.append(filters.gaussian(image, sigma=numeric_parameter))
        elif fn == "random":
            feature_stack.append(np.random.random(image.shape))
        else:
            warnings.warn(f"Feature unknown: {fn}")
    
    # The ravel() function turns a nD image into a 1-D image.
    # We need to use it because scikit-learn expects values in a 1-D format here. 
    return np.asarray(feature_stack)

def visualize_image_list(images, titles=None):
    image = images[0]
    
    # show feature images
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, len(images), figsize=(10, 10))
    
    for i in range(len(images)):
        # reshape(image.shape) is the opposite of ravel() here. We just need it for visualization.
        axes[i].imshow(images[i].reshape(image.shape), cmap=plt.cm.gray)
        axes[i].set_axis_off()
        if titles is not None:
            axes[i].set_title(titles[i])


def get_plt_figure():
    from stackview._static_view import _plt_to_png
    import matplotlib.pyplot as plt
    from io import BytesIO
    from PIL import Image

    with BytesIO() as file_obj:
        plt.savefig(file_obj, format='png', bbox_inches='tight')
        plt.close() # supress plot output
        file_obj.seek(0)

        image = Image.open(file_obj)

        # Convert to RGB if image is in RGBA mode
        if image.mode == 'RGBA':
            image = image.convert('RGB')

    # Convert to NumPy array
    array = np.array(image)
    
    return array
    

def format_data(feature_stack, annotation):

    feature_stack = np.asarray([f.ravel() for f in feature_stack])
    
    # reformat the data to match what scikit-learn expects
    # transpose the feature stack
    X = feature_stack.T
    # make the annotation 1-dimensional
    y = annotation.ravel()
    
    # remove all pixels from the feature and annotations which have not been annotated
    mask = y > 0
    X = X[mask]
    y = y[mask]

    return X, y

