import pandas as pd
import numpy as np
from PIL import Image
import os
import tensorflow.keras as keras
from sklearn.model_selection import train_test_split

# Load your dataset
dataset = pd.read_csv("your_dataset.csv")

# Define function to load images from file paths
def load_image(file_path, target_size):
    image = Image.open(file_path)
    image = image.resize(target_size)
    image = np.array(image)
    # Normalize the image data
    image = image / 255.0
    return image

# Example usage of load_image function
# image = load_image("file_path_to_image.jpg", (28, 28))

# Load images and labels from dataset
images = []
labels = dataset['type']  # Assuming 'label' column contains the class labels
for file_path in dataset['file_path']:
    # Adjust file_path extraction based on your dataset structure
    # Assuming 'file_path' column contains the file paths to images
    image = load_image(file_path, (28, 28))  # Adjust target_size as needed
    images.append(image)

# Convert images and labels to numpy arrays
images = np.array(images)
labels = np.array(labels)

# Split data into training and validation sets
x_train, x_valid, y_train, y_valid = train_test_split(images, labels, test_size=0.2, random_state=42)

# Define your CNN model
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 3)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(num_classes, activation='softmax')
])

# Compile your model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train your model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_valid, y_valid))

