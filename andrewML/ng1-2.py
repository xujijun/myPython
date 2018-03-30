import numpy as np


def sigmoid(x):
    """
    计算x的sigmoid：σ(x)
    :param x: 一个数、向量、或矩阵
    :return s: sigmoid(x)
    """

    s = 1.0/(1 + 1/np.exp(x))
    return s

x = np.array([1, 2, 3])
print("σ(x): " + str(sigmoid(x)))


def sigmoid_derivative(x):
    """
    计算sigmoid的导数（梯度函数）：sigmoid_derivative(x)=σ′(x)=σ(x)(1−σ(x))
    :param x: 一个数、向量、或矩阵
    :return:
    """

    s = sigmoid(x)
    ds = s*(1-s)
    return ds

print("σ'(x): " + str(sigmoid_derivative(x)))


def normalize_rows(x):
    """
    对x矩阵每一行进行标准化（分别除以该行所有数的平方和的开方，即“长度”）
    :param x: 矩阵
    :return x: 覆盖掉原来的矩阵x
    """

    x_norm = np.linalg.norm(x, axis=1, keepdims=True)
    x = x/x_norm
    return x

x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
print("normalize_rows(x) = " + str(normalize_rows(x)))
