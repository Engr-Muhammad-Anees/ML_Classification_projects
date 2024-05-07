
# 120 Dog Breeds Classification

This project demonstrates the classification of 120 dog breeds using transfer learning with VGG16 architecture.

## Dataset

The dataset consists of 120 different dog breeds with 100 images for each breed. The images are resized to 200x200 pixels.

## Model

The model used for classification is VGG16, which is a pre-trained convolutional neural network. The top layer of the VGG16 model is replaced with a new fully connected layer with 120 outputs, corresponding to the 120 dog breeds.

## Training

The model is trained for 15 epochs with early stopping to prevent overfitting. The training data is augmented with random shearing, zooming, and horizontal flipping to improve the generalization of the model.

## Evaluation

The model is evaluated on a separate validation set of 20 images per breed. The accuracy on the validation set is 95%.

## Conclusion

This project demonstrates the effectiveness of using transfer learning with VGG16 architecture for classifying 120 dog breeds with high accuracy.

## Usage

The model can be used to classify images of dogs into their respective breeds. To use the model, simply load an image of a dog and pass it to the `predict` method of the model. The model will return the predicted breed of the dog.

## Contributing

Contributions to this project are welcome. Please submit a pull request with your changes.

## License

This project is licensed under the MIT License.
  