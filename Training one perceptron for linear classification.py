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
# Plot data points
# plt.scatter(train[:, 0], train[:, 1])
# plt.show()
np.random.shuffle(train)
# Initial weights and bias randomly
W = np.random.rand(2)
Wupdates = np.empty((2, leng))
results = np.zeros((leng, 1))
col = np.zeros((leng, 1))
b = 1
# Training
for (X, y) in zip(train[:, 0:2], train[:, 2]):
    # Foreword pass
    Out = perceptron(W, b, X)
    # Backward pass
    # print(W)
    W[0] += 0.2 * ((Out - y) * dsig(W[1] * X[0]) * X[0])
    W[1] += W[1] - 0.2 * ((Out - y) * dsig(W[1] * X[1]) * X[1])
    np.append(Wupdates, W)
    # np.append(results, perceptron(W, train[:, 0:2], b))
    for (Y, i) in zip(train[:, :2], range(leng)):
        col[i]=perceptron(W, b, Y)
    results = np.append(col, results, axis=1)
    # np.append(results, )





    # W[0] = W[0] - 0.1*((Out - y)*dsig(W[0]*X[0])*X[0])
    # W[1] = W[1] - 0.1*((Out - y)*dsig(W[1]*X[1])*X[1])

res = np.empty(leng)
for (X, y) in zip(train[:,0:2], train[:,2]):
    # Foreword pass
    np.append(res, perceptron(W, b, X))

loss = (res - train[:, 2])
rmse = 0
for value in loss:
    rmse += value**2
print(rmse)
print(results)








# print("success")
# plt.scatter(train[:,0], train[:,1])
#
# plt.show()
