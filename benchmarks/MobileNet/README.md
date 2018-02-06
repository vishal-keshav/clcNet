# MobileNet Documented

* MobileNet is a family of architecture with faster inference on embedded systems
such as mobile devices for computer vision task.
* Basic convolution block consists of depth-wise convolution followed by point-wise
convolution. Each types of convolution is proceeded by RELU activation and batch normalization.

  * Depth wise convolution - To an input image of *M* channels, depth wise convolution consists
  of *M* kernels with depth of 1. Number of output channels is *M*. This extracts spatial features.
  * Point wise convolution - To an input of depth *M*, point wise convolution applies *N* kernels
  of shape depth *M* and *1 X 1* spatial dimensions. Number of output channels are *N*. This finds
  relation between input maps.


* MobileNet utilizes the efficiency of GEMM for dense matrix multiplication present in point wise
convolution operation. Point wise convolution operation consumes 95% of total processing of
network. Moreover, for GEMM to be applicable, *1 X 1* does not require re-ordering on inputs in memory.

* Two hyper-parameter has been introduced to control the computation complexity and model size of the
network.
  - Width multiplier - This has an effect of reducing the channel width of each layer uniformly for
  each layer. For example, *0.5* width multiplier reduces each input and output channel to Depth
  wise separable convolution (except convolution to input) to half.
  - Resolution multiplier - This has an effect of reducing the height and width dimension of each
  channels by factor of multiplier at each layer. **(Internal Keras implementation did it wrong, which
  they called depth-multiplier)**

[Paper link](https://arxiv.org/pdf/1704.04861.pdf)

## Benchmarks

To be updated soon.
