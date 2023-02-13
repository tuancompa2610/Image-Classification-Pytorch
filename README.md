<h1 align="center"> Image Classification Pytorch  </h1>

<br>

## 📃 Table of Contents:
  - [About Repository](#-about-repository)
  - [Installation](#-installation)
  - [Useage](#-useage)
  - [Contribution](#-contribution)
  
## About Repository
In this Repository I will give an indepth look at how to work with several modern CNN architectures to classify image by using Pytorch.
## Usage
You have to clone this repo to your local

`$ git clone https://github.com/tuancompa2610/Image-Classification-Pytorch.git`

Then make sure you are in right directory

`$ cd Image-Classification-Pytorch`

Install all requirement package

`$ pip install -r requirements.txt`

Finally run model

`$ python train.py -net vgg16`

## Model using
* ResNet [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
* VGG [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556)
* DenseNet [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993)
* SqueezeNet [SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size](https://arxiv.org/abs/1602.07360)
* AlexNet [ImageNet Classification with Deep Convolutional Neural Networks](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)

## Report

| Model | Train loss | Train accuracy | Val loss | Val accuracy |
| ----- | ---------- | -------------- | -------- | ------------ |
| ResNet | 0.1141 | 0.9426 | 0.1927 | 0.9477|
| DenseNet | 0.8208 | 0.4877 | 0.7878 | 0.5686
| VGG |
| AlexNet |
| SqueezeNet | 0.2667 | 0.8770 | 0.3546 | 0.9020 |
