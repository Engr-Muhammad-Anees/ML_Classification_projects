# Cat Breed Classification Model

This repository contains a Python script for training a convolutional neural network (CNN) model to classify images of cats into 50 different breeds.

## Model Architecture

The model is based on the VGG16 architecture, which is pre-trained on the ImageNet dataset. The model consists of the following layers:

* VGG16 base model with weights loaded from ImageNet
* Global average pooling layer
* Dense layer with 128 units and ReLU activation
* Dense layer with 50 units and softmax activation

## Dataset

The model was trained on a dataset of 12,000 images of cats, with 240 images per breed. The dataset was split into a training set (80%) and a validation set (20%).

## Training

The model was trained for 20 epochs using the Adam optimizer and the categorical cross-entropy loss function. Early stopping was used to prevent overfitting.

## Evaluation

The model achieved an accuracy of 95% on the validation set.

## Usage

To use the model, first load the model weights from the file `50_cat_breeds_vgg16.h5`. Then, you can use the model to predict the breed of a cat image by calling the `predict` method.

