import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])
print(A)

cal = A.sum(axis=0)  # axis=0：竖向求和，axis=1：横向求和
print(cal)

percentage = 100*A/cal.reshape(1, 4)  # reshape(1, 4) 变成1*4的矩阵，本来就是1*4，多余的操作。 broadcasting，自动把cal变成3*4的矩阵和A匹配
print(percentage)

a = np.random.randn(5, 1)
print(a)
print(a.T)  # 转置
print(np.dot(a, a.T))  # 矩阵相乘

