# Un-Official implementation of clcNet

This is an unofficial implementation of clcNet in Keras and Tensorflow.
The goal of this project is to replicate the following paper on clcNet architecture.
>[LINK](https://arxiv.org/abs/1712.06145v2)

Following the implementation and hyper-parameter search, benchmarking will be done with respect to
* MobileNet
* ShuffleNet
* SqueezeNet

Disclaimer: The views expressed and/or work on this project done are of my own and do not necessarily 
represents any of my employeer, organisation, publishing committe or individual related to this research.

## Breif overview of architecture
### Channel Local Convolutions
A channel local convolution represents a local receptive field for a several channels in the input.
Locality of convolution is ensured by application of convolution to a part of input channel to clc block.

### Brief summary
The paper proposes a structured way of composing group convolution such that full channel receptive field
in a given block is 100 percent. This introduces the idea of more generalized channel local convolution and
acyclic graph called channel dependency graph that connects output channel to input channel in a 
convolution block and measure channel receptive field of that convolution block.

### Novelty
* Observation such as having full channel receptive field in a convolution block is required to have efficient information flow for better representational power in a CNN.
* Interlaced group convolution, one of the two building block for cnc net is developed which with group convolution completes a convolution block.
* Determination of block parameters such as number of groups in IGC and GC is done through minimizing a developed cost function per convolution block remaining under the full channel receptive field constraints.

![clc_net][clc_net]

## Keras implementation
```
TO BE UPDATED
```

## Tensorflow implementation
```
TO BE UPDATED
```

## Contribution
Contribution for this project is currently not acceptable.
Notification for any open contribution will be updated here.

[clc_net]:res/clc_net.jpg
