# -*- coding: utf-8 -*-
"""120_dog_breeds_vgg16.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rpdEBFA4MM2yVWzkaMfpGhjWjSV5s5nJ
"""

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d amandam1/120-dog-breeds-breed-classification
!unzip /content/120-dog-breeds-breed-classification

import os
import numpy as np
import cv2
import shutil
import random
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping

main_dir = '/content/Images'

train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

test_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    main_dir,
    target_size=(200, 200),
    batch_size=200,
    class_mode='categorical',
    subset='training'
)

validation_generator = test_datagen.flow_from_directory(
    main_dir,
    target_size=(200, 200),
    batch_size=200,
    class_mode='categorical',
    subset='validation'
)

print(f"Shape of labels: {train_generator.labels.shape}")
print(f"Shape of labels: {validation_generator.labels.shape}")

total_train_images = train_generator.samples
print(f"Number of images in train_generator: {total_train_images}")

labels = (validation_generator.class_indices)

base_model = tf.keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(200, 200, 3))
base_model.trainable = False

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(120, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss="categorical_crossentropy", metrics=["accuracy"])

early_stopping = EarlyStopping(monitor='val_loss', patience=3)

history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=15,
    callbacks=[early_stopping]
)

#model.save('/content/drive/MyDrive/save_models/120_dog_breeds_TL_vgg16.h5')

labels = dict((v, k) for k, v in train_generator.class_indices.items())
labels

import tensorflow as tf

model= tf.keras.models.load_model("/content/drive/MyDrive/save_models/120_dog_breeds_TL_vgg16.h5")

img = tf.keras.preprocessing.image.load_img(
    '/content/drive/MyDrive/dog_images/9.jpg', target_size=(200, 200)
)

import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

predictions = model.predict(img_array)
predicted_class = labels[np.argmax(predictions)]
print("Predicted class:", predicted_class)