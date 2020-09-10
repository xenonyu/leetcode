import numpy as np



A = np.array([[1, 0], [0, 1]])
# print(A.shape)
b = np.array([2, 3])
x = np.zeros(A.shape[1])

for i in range(len(x)):
    x[i] = sum(A[:, i]) - b[i]
print(x)