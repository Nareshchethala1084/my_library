import tensorflow as tf

# Prepare file paths and labels
file_paths = data_df_filtered['File Path'].values
labels = data_df_filtered['Encoded Label'].values

# Create a TensorFlow dataset from file paths and labels
def parse_image(file_path, label):
    # Load the raw data from the file as a string
    image = tf.io.read_file(file_path)
    # Convert the compressed string to a 3D uint8 tensor
    image = tf.image.decode_png(image, channels=3)
    # Resize the image to the expected size
    image = tf.image.resize(image, [256, 256])
    # Normalize image
    image = image / 255.0
    return image, label

# Create a dataset returning slices of `file_paths` and `labels`
dataset = tf.data.Dataset.from_tensor_slices((file_paths, labels))
dataset = dataset.map(parse_image)

# Split the dataset into training, validation, and test sets
train_size = int(0.7 * len(dataset))
val_size = int(0.2 * len(dataset))
test_size = len(dataset) - train_size - val_size
train_dataset = dataset.take(train_size)
validation_dataset = dataset.skip(train_size).take(val_size)
test_dataset = dataset.skip(train_size + val_size)

