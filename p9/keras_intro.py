# Name: Jiwon Song
# NetID: jsong99
# WiscID: 9074018707
# Class: Spring 2020 CS 540


import tensorflow as tf
import numpy as np
from tensorflow import keras
from collections import defaultdict
import matplotlib.pyplot as plt


def get_dataset(training=True):
    #— takes an optional boolean argument and returns the data as described below.
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    
    if training:
        return (train_images, train_labels)
    
    return (test_images, test_labels)

def print_stats(images, labels):
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    #— takes the dataset and labels produced by the previous function and prints several statistics about the data; does not return anything.
    
    print(images.shape[0])
    print("{}x{}".format(images.shape[1], images.shape[2]))
    
    tmp_dict = {}
    for name in class_names:
        tmp_dict[name] = 0
    
    for label in labels:
        tmp_dict[class_names[label]] += 1
    
    num = 0
    for key in tmp_dict.keys():
        print("{}.".format(num), key, "-",tmp_dict[key])
        num += 1
        
    
    
    

def view_image(image, label):
    #— takes a single image as an array of pixels and displays an image; does not return anything.
    fig, ax = plt.subplots()
    ax.title.set_text(label)
    img = ax.imshow(image)
    fig.colorbar(img, fraction=0.046, pad=0.04, ax=ax)
    
    
def build_model():
    #— takes no arguments and returns an untrained neural network as specified below
    model = keras.Sequential([keras.layers.Flatten(input_shape=(28,28)),
                              keras.layers.Dense(128, activation='relu',),
                              keras.layers.Dense(10)
                             ])
    model.compile(loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True), 
                  optimizer = 'adam', 
                  metrics=['accuracy'])
    return model

    

    
def train_model(model, images, labels, T):
    #— takes the model produced by the previous function and the images and labels produced by the first function and trains the data for T epochs; does not return anything
    model.fit(images, labels, epochs=10, batch_size=T)
    return model
    
def evaluate_model(model, images, labels, show_loss=True):
    #— takes the trained model produced by the previous function and the test image/labels, and prints the evaluation statistics as described below (displaying the loss metric value if and only if the optional parameter has not been set to False)
    
    test_loss, test_accuracy = model.evaluate(images, labels)
    
    if show_loss:
        print('Loss:',"{:.2f}".format(test_loss))
        
    print('Accuracy:', '{:.2f}%'.format(test_accuracy * 100))
    
    

def predict_label(model, images, index):

    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    #— takes the trained model and test images, and prints the top 3 most likely labels for the image at the given index, along with their probabilities
    model.add(keras.layers.Softmax())
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
    
   