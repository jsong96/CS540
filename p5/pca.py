'''
    Name: Jiwon Song
    Student ID: 9074018707
    NetID: jsong99
    Class: Spring 2020 CS540
    Project: p5
    Filename: pca.py
'''
import scipy
from scipy import linalg
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt


def load_and_center_dataset(filename):
    """
    This function loads the dataset from a provided .mat file, re-center it around the origin and return it as a
    NumPy array of floats
    :param filename: matlab file with face representation data
    :return: Numpy array of floats
    """
    # load data from matlab file
    dataset = loadmat(filename)
    x = dataset['fea']
    n = len(x)
    d = len(x[0])
    # recenter each vector towards center
    recenter = x - np.mean(x, axis=0)
    # cast the value type to float
    recenter.astype(float)

    return recenter


def get_covariance(dataset):
    """
    This function calculates and return the covariance matrix of the dataset as a NumPy matrix (d x d array)
    :param dataset:
    :return: convariance matrix of the dataset as a Numpy matrix ( n x n array)
    """
    return (1 / (len(dataset) - 1)) * np.dot(np.transpose(dataset), dataset)


def get_eig(S, m):
    """
    This function performs eigen decomposition on the covariance matrix S and return a diagonal matrix (NumPy array)
    with the largest m eigenvalues on the diagonal, and a matrix (NumPy array) with the corresponding eigenvectors as
    columns
    :param S: a covariance matrix
    :param m: largest m eigenvalues
    :return: a diagonal matrix with the largest m eigenvalues on the diagonal
    :return: a matrix (NumPy array) with the corresponding eignvectors as columns
    """
    # get eigen vectors and eigen values
    Lambda, U = scipy.linalg.eigh(S)
    # extract the largest m eigevalues of S
    tmp = Lambda[-m:]
    pair = []
    # extract corresponding eigen vectors of S
    for row in U:
        raw = list(row[-m:])
        raw = raw[::-1]
        pair += [raw]
    pair = np.array(pair)
    # put eigen vectors into a diagonal matrix
    tmp[::-1].sort()
    eigenvalue = np.diag(tmp)

    return eigenvalue, pair


def project_image(image, U):
    """
    This function project each image into your m-dimensional space and return the new representation as a d x 1 NumPy
    array
    :param image:
    :param U: eigenvectors
    :return: alphas for the image
    """
    result = np.dot(np.dot(np.transpose(image), U), np.transpose(U))
    return result


def display_image(orig, proj):
    """
    This function uses matplotlib to display a visual representation of the original image and the projected image
    side-by-side
    :param orig:
    :param proj:
    :return:
    """
    # reshape the orig image to be 32 x 32
    orig = np.reshape(orig, [32, 32])
    orig_plt = np.transpose(orig)
    # reshape the proj image to be 32 x 32
    proj = np.reshape(proj, [32, 32])
    proj_plt = np.transpose(proj)

    # create a figure with two subplots
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.title.set_text('Original')
    pos = ax1.imshow(orig_plt, aspect='equal')
    fig.colorbar(pos, fraction=0.046, pad=0.04, ax=ax1)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.title.set_text('Projection')
    neg = ax2.imshow(proj_plt, aspect='equal')
    fig.colorbar(neg, fraction=0.046, pad=0.04, ax=ax2)
    fig.tight_layout(pad=3.0)
    # show the images
    plt.show()
