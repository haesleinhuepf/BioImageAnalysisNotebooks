# Processor Chipset Architecture
Modern days computer processors often integrate various computing units including CPU, GPU, NPU and RAM. These components often cause significant performance difference in bioimage analysis.

The processors may still classified by the CPUs instruction sets, mainly x86 and ARM. Python libraries natively built on one of the architecture may not be directly runnable on the other, unless with OS layer translation or code compilation from source. i.e. Legacy x86 Python libraries may not be runnable on ARM computers. For power performance reason we see computer manufacturers are releasing new laptop in ARM architecture, yet most of the existing bioimage analysis software are pre-compiled in x86. With the effort of Apple Rosetta 2, the issue is more relieved yet not 100% compatible. So bare in mind in choosing the adequate CPU for your analysis work.

When necessary, consult the code developer for the support to the CPU platforms. Following is a summary for the CPUs architectures:

| Feature                          | Apple Silicon      | Intel               | AMD               | Qualcomm   | NVIDIA            |
|----------------------------------|--------------------|---------------------|-------------------|--------------------|--------------------|
| **Architecture**                 | ARM-based          | x86/x86-64          | x86/x86-64        | ARM-based          | ARM-based (Grace CPU) |
| **Notable Series**               | M1, M2             | Core, Xeon          | Ryzen, EPYC       | Snapdragon X Elite     | Grace CPU          |
| **Big-Small Cores**             | Yes    | Yes        | Not typical       | Yes    | Not typical        |
| **Integrated Graphics**          | Apple GPU   | Intel Iris, UHD, Arc | Radeon Graphics | Adreno GPU   | NVIDIA GPU   |
| **Thermal Design Power (TDP)**   | Low to moderate    | Moderate to high    | Moderate to high  | Low                | Moderate to high   |
| **Primary Use Cases**            | Laptops, Desktops  | Laptops, Desktops, Servers | Laptops, Desktops, Servers | Laptops, Mobile Devices | HPC, AI, Data Centers |
| **OS**                | macOS              | Windows, Linux | Windows, Linux   | Windows, Linux   | Linux              |
| **OpenCL Support**                | Yes              | Yes | Yes   | Not Mentioned  | Yes              |
| **AI Support**                | Yes              | Yes | Yes   | Yes  | Best compatibility with CUDA |