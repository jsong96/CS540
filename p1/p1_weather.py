####################################
# Name: Jiwon Song
# Class: Spring 2020 CS 540
# Instructor: Jerry Zhu
####################################

import math

#  return the Euclidean distance between two dictionary data points from the data set.
def euclidean_distance(data_point1, data_point2):
    # (x1 - x2)
    e1 = data_point1['PRCP'] - data_point2['PRCP']
    # (y1 - y2)
    e2 = data_point1['TMIN'] - data_point2['TMIN']
    # (z1- z2)
    e3 = data_point1['TMAX'] - data_point2['TMAX']

    # sqrt of (e1 + e2 +e3 )
    e_distance = math.sqrt((e1 ** 2) + (e2 ** 2) + (e3 ** 2))

    return e_distance


#  return a list of data point dictionaries read from the specified file.
def read_dataset(filename):
    # a list of data point to return
    data_point = []

    # open file and iterate line by line
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            data = {}
            # strip and split each element in each line of the file
            tmp = line.strip().split(' ')
            data['DATE'] = tmp[0]
            data['TMAX'] = float(tmp[2])
            data['PRCP'] = float(tmp[1])
            data['TMIN'] = float(tmp[3])
            data['RAIN'] = tmp[4]
            # add the elements to the list
            data_point.append(data)

    return data_point


# return a prediction of whether it is raining or not based on a majority vote of the list of neighbors.
def majority_vote(nearest_neighbors):

    # temporal variables for true and false count
    ycount = 0
    ncount = 0

    # iterate through the list and count the number of true and false
    for neighbors in nearest_neighbors:
        if neighbors['RAIN'] == 'TRUE':
            ycount += 1
        else:
            ncount += 1

    # return the result of majority vote
    if ycount >= ncount:
        return 'TRUE'
    else:
        return 'FALSE'


# using the majority vote function,
# return the majority vote prediction for whether it's raining or not on the provided test point.
def k_nearest_neighbors(filename, test_point, k):

    # extract the data from the file
    data = read_dataset(filename)

    # initializing variables
    close_neighbors = []
    distances = []
    i = 0

    # iterate through data to find each its distance from the test_point and save it as a tuple with its index
    for d in data:
        distances += [(euclidean_distance(d, test_point), i)]
        i += 1
    # sort them in ascending order
    distances.sort()

    # extract k number of data and save them in a list
    for i in range(k):
        idx = distances[i][1]
        close_neighbors += [data[idx]]

    # run majority vote and return the result
    return majority_vote(close_neighbors)

