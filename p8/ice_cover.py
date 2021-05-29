# Name: Jiwon Song
# NetID: jsong99
# WiscID: 9074018707
# Class: Spring 2020 CS 540


import numpy as np
import math
import random


def get_dataset():
    # — takes no arguments and returns the data as described below in an n-by-2 array
    data = [[1855, 118],
            [1856, 151],
            [1857, 121],
            [1858, 96],
            [1859, 110],
            [1860, 117],
            [1861, 132],
            [1862, 104],
            [1863, 125],
            [1864, 118],
            [1865, 125],
            [1866, 123],
            [1867, 110],
            [1868, 127],
            [1869, 131],
            [1870, 99],
            [1871, 126],
            [1872, 144],
            [1873, 136],
            [1874, 126],
            [1875, 91],
            [1876, 130],
            [1877, 62],
            [1878, 112],
            [1879, 99],
            [1880, 161],
            [1881, 78],
            [1882, 124],
            [1883, 119],
            [1884, 124],
            [1885, 128],
            [1886, 131],
            [1887, 113],
            [1888, 88],
            [1889, 75],
            [1890, 111],
            [1891, 97],
            [1892, 112],
            [1893, 101],
            [1894, 101],
            [1895, 91],
            [1896, 110],
            [1897, 100],
            [1898, 130],
            [1899, 111],
            [1900, 107],
            [1901, 105],
            [1902, 89],
            [1903, 126],
            [1904, 108],
            [1905, 97],
            [1906, 94],
            [1907, 83],
            [1908, 106],
            [1909, 98],
            [1910, 101],
            [1911, 108],
            [1912, 99],
            [1913, 88],
            [1914, 115],
            [1915, 102],
            [1916, 116],
            [1917, 115],
            [1918, 82],
            [1919, 110],
            [1920, 81],
            [1921, 96],
            [1922, 125],
            [1923, 104],
            [1924, 105],
            [1925, 124],
            [1926, 103],
            [1927, 106],
            [1928, 96],
            [1929, 107],
            [1930, 98],
            [1931, 65],
            [1932, 115],
            [1933, 91],
            [1934, 94],
            [1935, 101],
            [1936, 121],
            [1937, 105],
            [1938, 97],
            [1939, 105],
            [1940, 96],
            [1941, 82],
            [1942, 116],
            [1943, 114],
            [1944, 92],
            [1945, 98],
            [1946, 101],
            [1947, 104],
            [1948, 96],
            [1949, 109],
            [1950, 122],
            [1951, 114],
            [1952, 81],
            [1953, 85],
            [1954, 92],
            [1955, 114],
            [1956, 111],
            [1957, 95],
            [1958, 126],
            [1959, 105],
            [1960, 108],
            [1961, 117],
            [1962, 112],
            [1963, 113],
            [1964, 120],
            [1965, 65],
            [1966, 98],
            [1967, 91],
            [1968, 108],
            [1969, 113],
            [1970, 110],
            [1971, 105],
            [1972, 97],
            [1973, 105],
            [1974, 107],
            [1975, 88],
            [1976, 115],
            [1977, 123],
            [1978, 118],
            [1979, 99],
            [1980, 93],
            [1981, 96],
            [1982, 54],
            [1983, 111],
            [1984, 85],
            [1985, 107],
            [1986, 89],
            [1987, 87],
            [1988, 97],
            [1989, 93],
            [1990, 88],
            [1991, 99],
            [1992, 108],
            [1993, 94],
            [1994, 74],
            [1995, 119],
            [1996, 102],
            [1997, 47],
            [1998, 82],
            [1999, 53],
            [2000, 115],
            [2001, 21],
            [2002, 89],
            [2003, 80],
            [2004, 101],
            [2005, 95],
            [2006, 66],
            [2007, 106],
            [2008, 97],
            [2009, 87],
            [2010, 109],
            [2011, 57],
            [2012, 87],
            [2013, 117],
            [2014, 91],
            [2015, 62],
            [2016, 65],
            [2017, 94],
            [2018, 86],
            [2019, 70]]

    return data


def print_stats(dataset):
    # — takes the dataset as produced by the previous function and prints several statistics about the data; does not return anything
    print(len(dataset))

    total = 0
    for data in dataset:
        total += data[1]

    mean = total / len(dataset)

    print("{:.2f}".format(mean))

    sd = 0
    for data in dataset:
        sd += (data[1] - mean) ** 2
    sd = sd / len(dataset)

    sd = math.sqrt(sd)
    print("{:.2f}".format(sd))


def regression(beta_0, beta_1):
    dataset = get_dataset()
    err = 0
    # — calculates and returns the mean squared error on the dataset given fixed betas
    for data in dataset:
        x = data[0]
        y = data[1]
        new_y = beta_0 + beta_1 * x
        err += (y - new_y) ** 2

    return err / len(dataset)  # 1/n
    # y = beta_0 + beta_1 * x


def gradient_descent(beta_0, beta_1):
    # — performs a single step of gradient descent on the MSE and returns the derivative values as a tuple
    dataset = get_dataset()

    err = 0
    err_b = 0
    for data in dataset:
        x = data[0]
        y = data[1]
        new_y = beta_0 + beta_1 * x
        err += (y - new_y)
        err_b += (y - new_y) * x

    first = -(err * 2 / len(dataset))

    second = -(err_b * 2 / len(dataset))

    return first, second


def iterate_gradient(T, eta):
    # — performs T iterations of gradient descent starting at LaTeX: (\beta_0, \beta_1) = (0,0)( β 0 , β 1 ) = ( 0 , 0 ) with the given parameter and prints the results; does not return anything
    dataset = get_dataset()

    beta_0 = 0
    beta_1 = 0

    #  beta_0 =  beta_0 -  eta* gradient_descent(beta_0, beta_1)

    for i in range(T):
        beta_0 = beta_0 - eta * gradient_descent(beta_0, beta_1)[0]
        beta_1 = beta_1 - eta * gradient_descent(beta_0, beta_1)[1]
        print(i + 1, round(beta_0, 2), round(beta_1, 2), round(regression(beta_0, beta_1), 2))


def compute_betas():
    # — using the closed-form solution, calculates and returns the values of LaTeX: \beta_0β 0 and LaTeX: \beta_1β 1 and the corresponding MSE as a three-element tuple
    dataset = get_dataset()

    mx = 0
    my = 0
    for data in dataset:
        x = data[0]
        y = data[1]

        mx += x
        my += y

    mx = mx / len(dataset)
    my = my / len(dataset)

    numerator = denominator = 0
    for data in dataset:
        x = data[0]
        y = data[1]

        numerator += (x - mx) * (y - my)
        denominator += (x - mx) ** 2

    beta_1 = numerator / denominator
    beta_0 = my - beta_1 * mx
    mse = regression(beta_0, beta_1)

    return beta_0, beta_1, mse


def predict(year):
    # — using the closed-form solution betas, return the predicted number of ice days for that year

    beta_0, beta_1, mse = compute_betas()

    snow_day = beta_0 + beta_1 * year

    return snow_day


def iterate_normalized_helper(beta_0, beta_1):
    # — performs a single step of gradient descent on the MSE and returns the derivative values as a tuple
    dataset = get_dataset()

    normal_x = 0
    for data in dataset:
        x = data[0]
        y = data[1]

        normal_x += x

    normal_x = normal_x / len(dataset)

    std_x = 0

    for data in dataset:
        x = data[0]
        std_x += (x - normal_x) ** 2

    std_x = math.sqrt(std_x / (len(dataset) - 1))

    err = 0
    err_b = 0
    for data in dataset:
        x = (data[0] - normal_x) / std_x
        y = data[1]
        new_y = beta_0 + beta_1 * x
        err += (y - new_y)
        err_b += (y - new_y) * x

    first = -(err * 2 / len(dataset))

    second = -(err_b * 2 / len(dataset))

    return first, second


def normalized_regression(beta_0, beta_1):
    dataset = get_dataset()

    normal_x = 0
    for data in dataset:
        x = data[0]
        y = data[1]

        normal_x += x

    normal_x = normal_x / len(dataset)

    std_x = 0

    for data in dataset:
        x = data[0]
        std_x += (x - normal_x) ** 2

    std_x = math.sqrt(std_x / (len(dataset) - 1))

    err = 0
    # — calculates and returns the mean squared error on the dataset given fixed betas
    for data in dataset:
        x = (data[0] - normal_x) / std_x
        y = data[1]
        new_y = beta_0 + beta_1 * x
        err += (y - new_y) ** 2

    return err / len(dataset)  # 1/n


def iterate_normalized(T, eta):
    # — normalizes the data before performing gradient descent, prints results as in function 5
    dataset = get_dataset()

    beta_0 = 0
    beta_1 = 0

    #  beta_0 =  beta_0 -  eta* gradient_descent(beta_0, beta_1)

    for i in range(T):
        beta_0 = beta_0 - eta * iterate_normalized_helper(beta_0, beta_1)[0]
        beta_1 = beta_1 - eta * iterate_normalized_helper(beta_0, beta_1)[1]
        print(i + 1, round(beta_0, 2), round(beta_1, 2), round(normalized_regression(beta_0, beta_1), 2))


def sgd_helper(beta_0, beta_1):
    # — performs a single step of gradient descent on the MSE and returns the derivative values as a tuple
    dataset = get_dataset()
    random_idx = random.randint(1, len(dataset) - 1)

    normal_x = 0
    for data in dataset:
        x = data[0]
        y = data[1]

        normal_x += x

    normal_x = normal_x / len(dataset)

    std_x = 0

    for data in dataset:
        x = data[0]
        std_x += (x - normal_x) ** 2

    std_x = math.sqrt(std_x / (len(dataset) - 1))

    err = 0
    err_b = 0
    try:
        data = dataset[random_idx]

    except:
        print('random number is wrong: ', random_idx)

    x = (data[0] - normal_x) / std_x
    y = data[1]
    new_y = beta_0 + beta_1 * x
    err += (y - new_y)
    err_b += (y - new_y) * x

    first = -(err * 2 / len(dataset))

    second = -(err_b * 2 / len(dataset))

    return first, second


def sgd(T, eta):
    # — performs stochastic gradient descent, prints results as in function 5

    dataset = get_dataset()

    beta_0 = 0
    beta_1 = 0

    #  beta_0 =  beta_0 -  eta* gradient_descent(beta_0, beta_1)

    for i in range(T):
        beta_0 = beta_0 - eta * sgd_helper(beta_0, beta_1)[0]
        beta_1 = beta_1 - eta * sgd_helper(beta_0, beta_1)[1]
        print(i + 1, round(beta_0, 2), round(beta_1, 2), round(normalized_regression(beta_0, beta_1), 2))











