# Tensor Core

A **Tensor Core** is a computing unit in Nvidia GPUs that multiplies two matrices, and then adds a third matrix to the result to accomplish hardware accelerated **General Matrix Multiplication** (GEMM). To leverage Tensor Cores in TensorFlow and PyTorch, you need to ensure that you're using the right hardware, software versions, and configurations. Tensor Cores are specialised processing units available in after NVIDIA's Volta architectures. For further details check [hardware/Neural Processing Unit](../80_hardware/gpu.md)

Here's a step-by-step guide to enabling Tensor Cores for TensorFlow and PyTorch:

## Prerequisites
1. **Hardware**: Ensure you have an NVIDIA GPU that supports Tensor Cores (Volta, Turing, or Ampere architectures).
2. **CUDA Toolkit**: Install the CUDA toolkit version supported by your GPU.
3. **cuDNN Library**: Install the corresponding cuDNN library version.

## TensorFlow
1. Install TensorFlow with GPU support:

    ```bash
    pip install tensorflow-gpu
    ```
2. Enable Mixed Precision Training:
    TensorFlow provides an easy way to use mixed precision by using the `tf.keras.mixed_precision` API.

    ```python
    import tensorflow as tf
    from tensorflow.keras import mixed_precision

    # Enable mixed precision
    mixed_precision.set_global_policy('mixed_float16')
    ```
3. Ensure Optimizers are Compatible:

    Some optimizers may need adjustments for mixed precision. TensorFlow's built-in optimizers are already compatible.

4. Model Building:

    When building your model, ensure that layers are using the `float16` data type where appropriate. TensorFlow automatically casts variables to `float32` to maintain numerical stability.

5. Training:
    Train your model as usual. TensorFlow will use Tensor Cores automatically during the mixed-precision operations.

Tensorflow also allow environmental variable control of Tensor Core. Check the setting from official documentation: https://docs.nvidia.com/deeplearning/frameworks/tensorflow-user-guide/index.html#tf_disable_tensor_op_math


## PyTorch
1. Install PyTorch with GPU support:

    ```bash
    pip install torch torchvision
    ```

2. Enable AMP (Automatic Mixed Precision):

    PyTorch provides AMP through the torch.cuda.amp module.

    ```python
    import torch
    from torch.cuda.amp import autocast, GradScaler

    model = YourModel().cuda()
    optimizer = torch.optim.Adam(model.parameters())
    scaler = GradScaler()  # For scaling the gradients

    for epoch in range(num_epochs):
        for data, target in train_loader:
            data, target = data.cuda(), target.cuda()

            optimizer.zero_grad()
            
            with autocast():  # Enables mixed precision
                output = model(data)
                loss = criterion(output, target)

            scaler.scale(loss).backward()  # Scales the loss
            scaler.step(optimizer)  # Updates the optimizer
            scaler.update()  # Updates the scaler
    ```
3. Ensure the model is on GPU:
    
    Make sure your model and data are on the GPU by using `.cuda()`.

## Additional Tips
- **Performance Monitoring**: Use NVIDIA’s nvprof, nsight, or nvidia-smi tools to monitor GPU usage and ensure Tensor Cores are being utilised.
- **Profile Your Code**: Use TensorFlow's or PyTorch's built-in profilers to understand where your model spends most of its time and ensure mixed precision is being applied correctly.

By following these steps, you should be able to take advantage of Tensor Cores in both TensorFlow and PyTorch, significantly accelerating the training process for deep learning models.






