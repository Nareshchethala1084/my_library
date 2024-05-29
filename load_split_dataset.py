from sklearn.preprocessing import LabelEncoder
import tensorflow as tf

# Convert labels to numeric values
label_encoder = LabelEncoder()
filtered_data['Numeric Label'] = label_encoder.fit_transform(filtered_data['Label'])

# Define a function to load and preprocess images
def load_and_preprocess_image(file_path, label):
    img = tf.io.read_file(file_path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, [256, 256])  # Resize images to 256x256
    img = img / 255.0  # Normalize pixel values
    return img, label

# Create a TensorFlow dataset
paths = filtered_data['File Path'].values
labels = filtered_data['Numeric Label'].values
dataset = tf.data.Dataset.from_tensor_slices((paths, labels))
dataset = dataset.map(load_and_preprocess_image)  # Apply the preprocessing function

# Split the dataset into train, validation, and test sets
#here we have split the data in 70:20:10 for the train:validation:test data
def split_dataset(dataset, train_split=0.7, val_split=0.2, test_split=0.1):
    dataset_size = len(paths)
    train_size = int(train_split * dataset_size)
    val_size = int(val_split * dataset_size)

    train_dataset = dataset.take(train_size)
    val_dataset = dataset.skip(train_size).take(val_size)
    test_dataset = dataset.skip(train_size + val_size)

    return train_dataset, val_dataset, test_dataset

train_dataset, val_dataset, test_dataset = split_dataset(dataset)

# Display example data structure
train_dataset.element_spec
