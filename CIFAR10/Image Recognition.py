import matplotlib
from keras.preprocessing import image
from PIL import Image, ImageChops
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras import backend as K
import numpy as np
import matplotlib.pyplot as plt


# This will work for the models if you download them from the links above.
# If you want to export your own models, use the name of them here instead.
model_1 = tf.keras.models.load_model('CIFAR10_imagerecognition.h5')


# model_2 = tf.keras.models.load_model('cnn_model.h5')
labelnames = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
labelnamestitle = "airplane    automobile     bird    cat          deer      dog      frog      horse      ship      truck      "

def plot_image(array, i, labels):
    plt.imshow(np.squeeze(array[i]))
    plt.title(labelnames(labels[i]))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def predict_image(model, x):
    x = x.astype('float32')
    x = x / 255.0

    x = np.expand_dims(x, axis=0)

    image_predict = model.predict(x, verbose=0)
    print("Predicted Label: " + labelnames[np.argmax(image_predict)])

    plt.imshow(np.squeeze(x))
    plt.title("Predicted Label: " + labelnames[np.argmax(image_predict)])
    plt.xticks([])
    plt.yticks([])
    plt.show()

    # uncomment this like if you want to see the array of predictions
    # print(image_predict)
    return image_predict


def plot_value_array(predictions_array, true_label, h):
    plt.grid(axis="x")
    plt.title(labelnamestitle, fontsize=8)
    plt.xticks(range(10))
    #plt.axes().set_xticklabels(labelnames)
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array[0], color="#777777")
    plt.ylim([(-1 * h), h])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')
    plt.show()

path = "photo.jpg"
img = image.load_img(path, target_size=(32, 32), color_mode="rgb")
img_arr = image.img_to_array(img)
arr = predict_image(model_1,  img_arr)
plot_value_array(arr, 3, 1)
