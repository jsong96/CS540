'''
    Name: Jiwon Song
    Student ID: 9074018707
    NetID: jsong99
    Class: Spring 2020 CS540
    Project: p4
    Filename: classify.py
'''

import os
import math


def create_vocabulary(training_directory, cutoff):
    """
    This function creates and returns a vocabulary as a list of word types with counts => cutoff in the
    training directory
        :param training_directory: a directory path
        :param cutoff: a number of times each word should appear
        :return: a list of word vocabulary
    """
    # word type list to return
    word_type = []
    # find the list of working directory
    dir_list = os.listdir(training_directory)
    word_dictionary = {}
    # traverse each subdirectories and count the number of times a word type appears in any file in either directory
    for directory in dir_list:
        path = os.path.join(training_directory, directory)
        # find file names in each subdirectories
        file_list = os.listdir(path)
        # for each file, open and get data
        for file in file_list:
            with open(os.path.join(path, file), 'r', encoding='UTF-8') as f:
                # words = f.read()
                words = f.readlines()
                # words = words.split('\n')
                for word in words:
                    if word.strip() not in word_dictionary.keys():
                        word_dictionary[word.strip()] = 1
                    else:
                        word_dictionary[word.strip()] += 1

    for key in word_dictionary.keys():
        if word_dictionary[key] >= cutoff:
            word_type += [key]

    word_type = sorted(word_type)
    return word_type


def create_bow(vocab, filepath):
    """
    This function creates and returns a bag of words Python dictionary from a single document
        :param vocab: a list of vocabulary
        :param filepath: a file path to read in
        :return: the-bag-of-words representation
    """
    # bag of word container
    bow = {}
    # open the file and extract each line
    with open(filepath, 'r', encoding='UTF-8') as f:
        words = f.readlines()
    # for every word, count how many times it appears in the file
    for word in words:
        if word.strip() in vocab:
            if word.strip() in bow.keys():
                bow[word.strip()] += 1
            else:
                bow[word.strip()] = 1
        else:
            if None in bow.keys():
                bow[None] += 1
            else:
                bow[None] = 1

    return bow


def load_training_data(vocab, directory):
    """
    This function creates and returns training set (bag of words Python dictionary + label) from the files in
    a working directory
        :param vocab: a list of vocabulary
        :param directory: a working directory
        :return: a dictionary with labels corresponding to its subdirectory
    """
    result = []
    sub_directs = os.listdir(directory)
    # 'corpus/training/'
    # 'corpus/training/', 2016, 2020
    for sub in sub_directs:
        sub_path = os.path.join(directory, sub)
        file_list = os.listdir(sub_path)
        for file in file_list:
            file_path = os.path.join(sub_path, file)
            label = {'label': sub, 'bow': create_bow(vocab, file_path)}
            result += [label]

    return result


def prior(training_data, label_list):
    """
    This function gives a training set, estimates and returns the prior probability p(label) of each label
        :param training_data: a list of data
        :param label_list: list with labels
        :return: the log probability of the labels in the training set
    """
    result = {}
    # for each label
    for label in label_list:
        label_count = 0
        for data in training_data:
            if data['label'] == label:
                label_count += 1
        # count the number of times each label appear in the training data and tak the log of it.
        result[label] = math.log(label_count / len(training_data))
    # return the result
    return result


def p_word_given_label(vocab, training_data, label):
    """
    This function estimates and returns the class conditional distribution P (word|label) over all words for the given
    label using smoothing
        :param vocab: a list of words
        :param training_data: a list of data with labels
        :param label: to determine which label to compare
        :return: a dictionary filled with words: probability
    """
    size_vocab = len(vocab)
    count = {}
    bow = []
    for data in training_data:
        if data['label'] == label:
            bow += [data['bow']]
    # {'a': 2, 'dog': 1, 'chases': 1, 'cat': 1, '.': 1}
    total = 0
    for words in bow:
        for key in words.keys():
            total += words[key]
            if key in vocab:
                if key not in count.keys():
                    count[key] = words[key]
                else:
                    count[key] += words[key]
            else:
                if None not in count.keys():
                    count[None] = words[key]
                else:
                    count[None] += words[key]
    smoothing = {}
    for key in count:
        smoothing[key] = math.log((count[key] + 1) / (total + len(count)))
    # smoothing = sorted(smoothing)
    return smoothing


def train(training_directory, cutoff):
    """
    This function loads the training data, estimates the prior distribution P(label) and class conditional distributions
    P( word|label)
        :param training_directory: the training file directory
        :param cutoff: cutoff
        :return: the trained model
    """
    # get vocabulary
    vocab = create_vocabulary(training_directory, cutoff)
    # get training data
    training_data = load_training_data(vocab, training_directory)
    # get prior probability of each label
    p = prior(training_data, ['2016', '2020'])
    # get log probability of each word
    pl_one = p_word_given_label(vocab, training_data, '2016')
    pl_two = p_word_given_label(vocab, training_data, '2020')
    # format for model
    model = {'vocabulary': vocab, 'log prior': p, 'log p(w|y=2016)': pl_one, 'log p(w|y=2020)': pl_two}

    return model


def classify(model, filepath):
    """
    This function predicts the label for the test document and returns the result of prediction
        :param model: a given train model
        :param filepath: a filename of the single test document
        :return: a python dictionary
    """

    bow = create_bow(model['vocabulary'], filepath)

    p1 = model['log p(w|y=2016)']
    p2 = model['log p(w|y=2020)']

    total_one = 0
    total_two = 0

    pr_one = model['log prior']['2016']
    pr_two = model['log prior']['2020']

    for key in p1:
        if key in bow.keys():
            total_one += (p1[key] * bow[key])

    for key in p2:
        if key in bow.keys():
            total_two += (p2[key] * bow[key])

    total_one += pr_one
    total_two += pr_two

    result = {
        'log p(y=2016|x)': total_one,
        'log p(y=2020|x)': total_two
    }

    if total_one < total_two:
        result['predicted y'] = '2020'
    else:
        result['predicted y'] = '2016'

    return result
