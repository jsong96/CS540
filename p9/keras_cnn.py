# Name: Jiwon Song
# NetID: jsong99
# WiscID: 9074018707
# Class: Spring 2020 CS 540


import tensorflow as tf
from tensorflow import keras
import numpy as np


def get_dataset(training=True):
    #— takes an optional boolean argument and returns the data as described below
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    
    
    if training:
        train_images = np.expand_dims(train_images, axis = -1)
        return train_images, train_labels
    
    test_images = np.expand_dims(test_images, axis=-1)
    return test_images, test_labels

def build_model():
    #— takes no arguments and returns an untrained neural network as specified below
    model = keras.Sequential([ keras.layers.Conv2D(64, kernel_size = 3, activation = 'relu', input_shape=(28,28,1)),
                              keras.layers.Conv2D(32, kernel_size = 3, activation = 'relu'),
                              keras.layers.Flatten(),
                              keras.layers.Dense(10, activation = 'softmax')
    ])
    
    model.compile(loss = 'categorical_crossentropy', 
                  optimizer = 'adam', 
                  metrics=['accuracy'])
    return model

def train_model(model, train_img, train_lab, test_img, test_lab, T):
    #— takes the model produced by the previous function and the images and labels produced by the first function and trains the data for T epochs; does not return anything
    train_labs = keras.utils.to_categorical(train_lab)
    test_labs = keras.utils.to_categorical(test_lab)

    model.fit(train_img, train_labs, batch_size = 64, epochs= T, validation_data=(test_img, test_labs))
    
    
def predict_label(model, images, index):
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    probs = model.predict(images)[index]
    
    third = first = second = -1
      
    for i in range(len(probs)): 
      
        # If current element is greater 
        # than first 
        if (probs[i] > first): 
          
            third = second 
            second = first 
            first = probs[i] 
          
  
        # If arr[i] is in between first 
        # and second then update second  
        elif (probs[i] > second): 
          
            third = second 
            second = probs[i] 
          
        elif (probs[i] > third): 
            third = probs[i] 
    
    top_3 = {}
    probs = list(probs)
    top_3[class_names[probs.index(first)]] = first
    top_3[class_names[probs.index(second)]] = second
    top_3[class_names[probs.index(third)]] = third
        
    for key in top_3.keys():
        print("{}:".format(key),  "{:.2f}%".format(top_3[key]*100))
    