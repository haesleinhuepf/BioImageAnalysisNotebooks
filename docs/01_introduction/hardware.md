# Choosing the Optimal Computer and Operating System

Though Python is runnable on most of modern operating systems (OS) including Windows, MacOS and Linux, it is beneficial to keep scripting under *nix environment. Here we provide a guide for beginners to choose your computing hardwares.

This guide is intentionally written for programming beginners to code locally. For advance research units equip with python servers, we will cover a series of remote coding techniques to unleash more complex bioimage analysis.

## Shell Scripting
For historical reason the command line (CLI) batch scripting is divided into unix-like bash (MacOS, Linux) and DOS-like Powershell (Windows). For Windows users it is always recommended to run Python alongside with Git bash (https://git-scm.com/downloads) that maximally mimic the running *nix running environment.

With the seamless integration of bash terminal, remote SSH and Jupyter extension in VSCode, the experience of different operating systems does not differ very much. But under certain special occasions like 2FA security login to computing clusters, Linux or MacOS can retain a better experience with *nix specialised functions like SSH sockets for connection persistence.

| Operating System | Terminal Emulator            | Default Shell    | Additional Shells                   | Pros                                                                         | Cons                                                               |
|------------------|------------------------------|------------------|-------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Linux            | GNOME Terminal, Konsole      | Bash             | Zsh, Fish, Ksh, Tcsh, Dash          | Highly customizable, vast array of tools, strong community support, open-source | Fragmentation in terminal emulators, varying default configurations|
| macOS            | Terminal, iTerm2             | Zsh (since 10.15) | Bash, Fish, Ksh, Tcsh               | User-friendly, well-integrated with macOS, iTerm2 offers advanced features    | Terminal app is less feature-rich compared to iTerm2              |
| Windows          | Command Prompt, PowerShell, Windows Terminal | PowerShell       | Bash (via WSL), Git Bash, Cygwin    | Powerful scripting capabilities in PowerShell, WSL brings Linux compatibility | Command Prompt is limited, PowerShell syntax can be complex       |

## Processor Chipset Architecture
<div style="text-align: center;">
  <img src="./Apple-M1-Chip.jpg" alt="Placeholder Image" style="width:50%;">
  <p><em>Architecture of Apple Silcon M1 SoC</em></p>
</div>

Modern days computer CPUs are more lean to a System-on-a-Chip (SoC) that integrates all major components of a computing device including CPU, GPU, NPU and RAM. The physically compactness brings shorter communication route among each computing units, hence facilitate computing performance.

However the SoCs may still classified by the CPUs instruction sets, mainly x86 and ARM. Python libraries natively built on one of the architecture may not be directly runnable on the other, unless with OS layer translation or code compilation from source. i.e. Legacy x86 Python libraries may not be runnable on ARM computers. For power performance reason we see chipset manufacturers are releasing new SoCs in ARM architecture, yet most of the existing bioimage analysis software are pre-compiled in x86. With the effort of Apple Rosetta 2, the issue is more relieved yet not 100% compatible. So bare in mind in choosing the adequate CPU for your analysis work.

When necessary, consult the code developer for the support to the CPU platforms. Following is a summary for the CPUs architectures:

| Feature                          | Apple Silicon      | Intel               | AMD               | Snapdragon Xlite   | NVIDIA            |
|----------------------------------|--------------------|---------------------|-------------------|--------------------|--------------------|
| **Architecture**                 | ARM-based          | x86/x86-64          | x86/x86-64        | ARM-based          | ARM-based (Grace CPU) |
| **Notable Series**               | M1, M2             | Core, Xeon          | Ryzen, EPYC       | Snapdragon 8cx     | Grace CPU          |
| **Manufacturing Process**        | 5nm (TSMC)         | 10nm, 7nm, 14nm     | 7nm, 6nm, 5nm     | 7nm (TSMC)         | 5nm (TSMC)         |
| **Performance Cores**            | High-performance   | High-performance    | High-performance  | High-performance   | High-performance   |
| **Efficiency Cores**             | High-efficiency    | Not typical         | Not typical       | High-efficiency    | Not typical        |
| **Integrated Graphics**          | Yes (Apple GPU)    | Yes (Intel Iris, UHD) | Yes (Radeon Graphics) | Yes (Adreno GPU)   | Yes (NVIDIA GPU)   |
| **Thermal Design Power (TDP)**   | Low to moderate    | Moderate to high    | Moderate to high  | Low                | Moderate to high   |
| **Primary Use Cases**            | Laptops, Desktops  | Laptops, Desktops, Servers | Laptops, Desktops, Servers | Laptops, Mobile Devices | HPC, AI, Data Centers |
| **Special Features**             | Unified Memory     | Hyper-Threading, vPro | Simultaneous Multithreading (SMT) | AI Engine, 5G      | AI Acceleration, NVLink |
| **Compatibility**                | macOS              | Windows, Linux, macOS | Windows, Linux   | Windows, Android   | Linux              |

## GPU Support
### AI Training
Though all SoC manufacturers embeds GPU in the chipset, the AI based analysis is largely relies on NVidia CUDA as the base software stack. Common neural network libraries in Python (pyTorch and Tensorflow) are the foundation stone of popular models like UNet, Cellpose and Stardist. Yet we are seeing a recent support to pyTorch AMD ROCm and Intel OneAPI AI acceleration, the community support is fairly limited when comparing to CUDA. Considering the training scalability and infrastructure support across major GPU farms/research clusters, NVidia is still the sole runner when consider new model training.

### AI Inference
Machine learning algorithms consists of two parts: model training and inference. The computation resources for a fixed AI model to be implemented in new data are much smaller than training from scratch. On smaller AI tasks non-CUDA chipsets bring larger options for bioimage analysis. The inference of neural network based AI can be physically accelerated with specifically designed circuits. Such designs are often referred as neural processing units (NPU). NVidia, specifically added Tensor Core in bundle with optimised packages like cuDNN and Transformer Engine, to their later GPU products. We will cover this topic on the later of the article.

<div style="text-align: center;">
  <img src="./tensor_core.gif" alt="Placeholder Image" style="width:50%;">
  <p><em>NVidia Tensor Core for neural network acceleration</em></p>
</div>

### GPGPU Acceleration
Apart from AI applications, bioimage analysis tasks like single plane illumination fluorescent correlation spectroscopy (SPIM-FCS) performs [pixelwise fitting of the autocorrelation function](https://github.com/bpi-oxford/Gpufit/blob/master/Gpufit/models/spim_acfN.cuh). In quantitative imaging one may be interested in photon counting or camera calibrated denoising, that largely relies on the [pixel-by-pixel gain fitting](https://github.com/jackyko1991/sCMOS-Denoise/blob/main/notebooks/camera_calibration.ipynb). Such image analysis can utilise the parallelisation power of GPU to accelerate the research.

One high level analysis package [py-clesperanto](https://github.com/clEsperanto/pyclesperanto_prototype) attempts GPU acceleration based on OpenCL. Such computing process allows bioimage analysis not bound to graphic processing, but to more generic calculations. From this the GPU is often referred as general purpose GPU (GPGPU). Vendors like AMD and Intel are alternatives to NVidia in this sense.

## Neural Processing Unit (NPU)
<div style="text-align: center;">
  <img src="./tpu.png" alt="Placeholder Image" style="width:50%;">
  <p><em>Google Carol TPU AI  chipset on Raspberry Pi. Enables edge computing acceleration like smart microscopy that requires automated bioimage analysis during image acquisition.</em></p>
</div>

A Neural Processing Unit (NPU) is a specialized hardware accelerator designed to efficiently handle the computational demands of AI and machine learning tasks, particularly neural network inference and training. NPUs are optimized for the types of operations commonly used in deep learning, such as matrix multiplications, convolutions, and activation functions. In mid-2024 the NPUs are embedded in various SoCs, allowing a wider choice in AI applications.

| Feature                          | Google TPU (USB/M.2)      | Apple Silicon      | AMD                      | Intel (after Meteor Lake)       | NVIDIA (Grace Hopper)     | NVIDIA (Jetson)           | Snapdragon Xlite          |
|----------------------------------|---------------------------|--------------------|--------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| **Product Name**                 | Edge TPU                  | Apple Neural Engine| 3rd Gen Ryzen AI| VPU, GNA, AI Engine       | TensorRT, DLA, Grace Hopper| Jetson Xavier, Nano, TX2  | Qualcomm AI Engine        |
| **Primary Use Case**             | Edge AI, Low Power Devices| Mobile, Desktop    | GPUs with AI Capabilities| Mobile, Desktop, Edge AI  | Data Center, HPC, Embedded | Embedded AI     | Mobile, Edge Computing    |
| **Performance**                  | Moderate                  | High               | Moderate to High         | Moderate to High          | Very High                 | Moderate to High          | Moderate                  |
| **Efficiency**                   | High                      | High               | Moderate                 | High                      | Moderate to High          | High                      | High                      |
| **Special Features**             | Google Cloud Compatible, Tensor Operations| Unified Memory, Tight OS Integration | APUs, ROCm | Low Power, Vision Processing, Integrated AI | CUDA Integration, Tensor Cores | Low Power, Integrated AI | Integrated 5G, AI on Device |
| **Flexibility**                  | Specialized for TensorFlow| General Purpose    | AI with General Compute  | Specialized for AI and Vision| Highly Specialized        | General Purpose           | General Purpose           |
| **Compatibility**                | TensorFlow Lite           | macOS              | Windows, Linux           | Windows, Linux            | Windows, Linux            | Linux                     | Android, Windows          |
| **Scalability**                  | High                      | Moderate           | Moderate                 | Moderate                  | High                      | Moderate                  | Moderate                  |
| **Integration**                  | Edge Devices              | Mobile, Desktop    | GPUs                     | Mobile, Desktop, Edge Devices | HPC, Cloud, Embedded      | Embedded Systems| Mobile SoCs               |
| **Availability**                 | USB, M.2 Modules          | Built-in (A-series, M-series)| Radeon Instinct GPUs | Integrated in Meteor Lake CPUs | Available in GPUs, Servers | Available in Embedded Modules | Snapdragon SoCs           |