# ShuffleNet Documented

* ShuffleNet is a family of architecture with faster inference on embedded systems
such as mobile devices.
* It proposes a bottleneck structure similar to ResNeXt, but with the introduction
of point-wise group convolution with channel shuffling.

  * Point-wise group convolution - Input channels are grouped into several specified
    number of groups, on which point-wise convolution is applied (on each group separately).
  * Channel shuffling - After point-wise group convolution and before depth wise
  convolution, channel are shuffled. Channel shuffling and applying point-wise group
  convolution after depth-wise convolution retains the representation strength of network by restricting it from flowing channel information on one part of output.


* Average pooling(with stride 2) is applied in residual connection along with concatenation to increase the width of network across layers depth.
* To control the complexity of network, a simple scaling factor denoting factor of channels across layer (as compared to proposed base ShuffleNet) is provided.
* Batch normalization and RELU is applied on the first block of a given Shuffle stage
  while only batch normalization is applied on other blocks (depth wise and point-wise
  group convolution)

![shufflenet][shufflenet]

[Paper Link](https://arxiv.org/pdf/1707.01083.pdf)

## Benchmarks
To be updated

[shufflenet]: ../../res/shufflenet.jpg
