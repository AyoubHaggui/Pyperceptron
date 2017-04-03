import numpy as np
import this

print(this)
def sig(x):
    return 1/(1 + np.exp(-x))


def dsig(x):
    return sig(x)*(1-sig(x))


def perceptron(W, b, X):
    return sig(np.dot(X, W)+b)

np.random.seed(0)
# Data size
data_length = 1000
# Creating data
data = np.empty((data_length, 3))
data[:data_length//2, 0] = np.linspace(0, 0.4, data_length//2)
data[data_length//2:, 0] = np.linspace(0.6, 0.9, data_length//2)
data[:, 1] = np.random.normal(0, 0.1, data_length)
data[:data_length//2, 2] = 0
data[data_length//2:, 2] = 1
# data[:, :2] -= 0.5
# Separate the training data from validation data
length = int(0.8 * data_length)
np.random.shuffle(data)
train = data[:length, :]
validate = data[length:, :]
# Randomly initialize the perceptron weight and input biases
W = np.random.random(2)
b = np.random.random(1)
# Setting batch size of 10th the training data
batch_size = length//10
# Start the training
for _ in range(batch_size):
        # Pick the first batch_size data points at random
        np.random.shuffle(train)
        batch = train[:batch_size, :]
        # Train the perceptron on the batch data
        for (X, y) in zip(batch[:, :2], batch[:, 2]):  # X is a tuple of data point coordinates y is the response
            # Update the weights and bias using gradient decent
            W -= 0.5 * (perceptron(W, b, X) - y) * dsig(np.dot(X, W)+b) * X
            b -= 0.5 * (perceptron(W, b, X) - y) * dsig(np.dot(X, W)+b)
        # Print RMSE for training and RMSE for validation set
        rmse_training = np.sum(np.power(perceptron(W, b, batch[:, :2]) - batch[:, 2], 2))
        rmse_validation = np.sum(np.power(perceptron(W, b, validate[:, :2]) - validate[:, 2], 2))
        print("rmse_training = {}, rmse_validation = {}".format(rmse_training, rmse_validation))



