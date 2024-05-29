import tensorflow as tf
import os

# Avoid OOM errors by setting GPU Memory Consumption Growth
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus: 
    tf.config.experimental.set_memory_growth(gpu, True)

tf.config.list_physical_devices('GPU')

# 2. Remove dodgy images

import cv2
import imghdr

pwd

data_dir = '/Users/nareshchethala/Desktop/AQG/Data'

image_exts = ['jpeg','jpg', 'bmp', 'png']

# Iterate through each class directory in the data directory
for image_class in os.listdir(data_dir):
    class_dir = os.path.join(data_dir, image_class)
    
    # Check if the item is a directory, skip if not
    if not os.path.isdir(class_dir):
        continue
    
    # Iterate through each image file in the class directory
    for image in os.listdir(class_dir):
        image_path = os.path.join(class_dir, image)
        
        # Skip processing if the current item is not a file
        if not os.path.isfile(image_path):
            continue
        
        try:
            # Read the image using OpenCV
            img = cv2.imread(image_path)
            # Get the file type using imghdr
            tip = imghdr.what(image_path)
            # Check if the file type is not in the allowed extensions list
            if tip not in image_exts:
                print(f'Removing {image_path} (not in ext list)')
                # Uncomment the line below to remove images not in the ext list
                # os.remove(image_path)
        except Exception as e:
            # Handle any exceptions that occur during image processing
            print(f'Issue with image {image_path}: {e}')
            # Uncomment the line below to remove problematic images
            # os.remove(image_path)

# 3. Load Data

import numpy as np
from matplotlib import pyplot as plt

data = tf.keras.utils.image_dataset_from_directory(data_dir)

data_iterator = data.as_numpy_iterator()

batch = data_iterator.next()

fig, ax = plt.subplots(ncols=4, figsize=(20,20))
for idx, img in enumerate(batch[0][:4]):
    ax[idx].imshow(img.astype(int))
    ax[idx].title.set_text(batch[1][idx])

# 4. Scale Data

data = data.map(lambda x,y: (x/255, y))

data.as_numpy_iterator().next()

# 5. Split Data

train_size = int(len(data)*.7)
val_size = int(len(data)*.2)
test_size = int(len(data)*.1)

train_size

train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size+val_size).take(test_size)

# 6. Build Deep Learning Model

train

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout

model = Sequential()

model.add(Conv2D(16, (3,3), 1, activation='relu', input_shape=(256,256,3)))
model.add(MaxPooling2D())
model.add(Conv2D(32, (3,3), 1, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(16, (3,3), 1, activation='relu'))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])

model.summary()

# 7. Train

logdir='logs'

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)

hist = model.fit(train, epochs=20, validation_data=val, callbacks=[tensorboard_callback])

# 8. Plot Performance

fig = plt.figure()
plt.plot(hist.history['loss'], color='teal', label='loss')
plt.plot(hist.history['val_loss'], color='orange', label='val_loss')
fig.suptitle('Loss', fontsize=20)
plt.legend(loc="upper left")
plt.show()

fig = plt.figure()
plt.plot(hist.history['accuracy'], color='teal', label='accuracy')
plt.plot(hist.history['val_accuracy'], color='orange', label='val_accuracy')
fig.suptitle('Accuracy', fontsize=20)
plt.legend(loc="upper left")
plt.show()

# 9. Evaluate

from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy

pre = Precision()
re = Recall()
acc = BinaryAccuracy()

for batch in test.as_numpy_iterator(): 
    X, y = batch
    yhat = model.predict(X)
    pre.update_state(y, yhat)
    re.update_state(y, yhat)
    acc.update_state(y, yhat)

print(pre.result(), re.result(), acc.result())

# 10. Test

import cv2

img = cv2.imread('/Users/nareshchethala/Desktop/AQG/Data/attribute/attribute_Address.pdf_page_1.png')
plt.imshow(img)
plt.show()

resize = tf.image.resize(img, (256,256))
plt.imshow(resize.numpy().astype(int))
plt.show()

yhat = model.predict(np.expand_dims(resize/255, 0))

yhat

if yhat > 0.5: 
    print(f'Predicted class is Sad')
else:
    print(f'Predicted class is Happy')

# 11. Save the Model

from tensorflow.keras.models import load_model

model.save(os.path.join('models','imageclassifier.h5'))

new_model = load_model('imageclassifier.h5')

new_model.predict(np.expand_dims(resize/255, 0))
