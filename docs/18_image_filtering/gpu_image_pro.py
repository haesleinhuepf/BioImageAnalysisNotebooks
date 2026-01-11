from stackview import jupyter_displayable_output

@jupyter_displayable_output
def kuwahara(input_image, kernel_size:int=2):
    import pyclesperanto_prototype as cle

    sigma = kernel_size / 6

    input_image_cl = cle.push(input_image)
    output_image_cl = cle.create(input_image_cl)

    cle.execute(
        anchor=None,
        opencl_kernel_filename="kuwahara_2d.cl",
        kernel_name="kuwahara_2d",
        global_size=input_image_cl.shape,
        parameters={
            "src": input_image_cl,
            "dst": output_image_cl,
            "kernel_size": int(kernel_size),
            "sigma": float(sigma)
        }
    )

    return cle.pull(output_image_cl).astype(input_image.dtype)

@jupyter_displayable_output
def bilateral(input_image, sigma_color:float=0.2, sigma_spatial:float=2):
    import pyclesperanto_prototype as cle

    input_image_cl = cle.push(input_image)
    output_image_cl = cle.create(input_image_cl)

    cle.execute(
        anchor=None,
        opencl_kernel_filename="denoise_bilateral_2d.cl",
        kernel_name="denoise_bilateral_2d",
        global_size=input_image_cl.shape,
        parameters={
            "src": input_image_cl,
            "dst": output_image_cl,
            "sigma_color": float(sigma_color),
            "sigma_spatial": float(sigma_spatial)
        }
    )

    return cle.pull(output_image_cl).astype(input_image.dtype)
