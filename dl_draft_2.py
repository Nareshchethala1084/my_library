import pandas as pd
import numpy as np
from PIL import Image
import tensorflow.keras as keras
from sklearn.model_selection import train_test_split

# Load your dataset from Excel
dataset = pd.read_excel("your_dataset.xlsx")

# Define function to load images from file paths
def load_image(file_path, target_size):
    image = Image.open(file_path)
    image = image.resize(target_size)
    image = np.array(image)
    # Normalize the image data
    image = image / 255.0
    return image

# Load images and labels from dataset
images = []
labels = dataset['image_description']  # Assuming 'image_description' column contains the class labels
for file_path in dataset['image_location']:
    # Assuming 'image_location' column contains the file paths to images
    image = load_image(file_path, (28, 28))  # Adjust target_size as needed
    images.append(image)

# Convert images and labels to numpy arrays
images = np.array(images)
labels = np.array(labels)

# Split data into training and validation sets
x_train, x_valid, y_train, y_valid = train_test_split(images, labels, test_size=0.2, random_state=42)

# Define the number of classes
num_classes = len(np.unique(labels))

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

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_valid, y_valid))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_valid, y_valid, verbose=2)
print('\nTest accuracy:', test_acc)

