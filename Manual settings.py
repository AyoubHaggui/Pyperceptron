import numpy as np
from matplotlib import pyplot as plt


def sig(x):
    return 1/(1 + np.exp(-x))


def dsig(x):
    return sig(x)*(1-sig(x))


def perceptron(W, b, X):
    return sig(np.dot(X, W))

np.random.seed(0)
# create the training set
leng = 100
train = np.empty((leng, 3))
train[:leng//2, 0] = np.linspace(0, 0.4, leng//2)
train[:, 1] = np.random.random(leng)
train[leng//2:, 0] = np.linspace(0.6, 0.9, leng//2)
train[:leng//2, 2] = 0
train[leng//2:, 2] = 1
