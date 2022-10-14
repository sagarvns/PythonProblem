import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([[1,2,3],[4,5,6]])
print(b)

a1=np.zeros((5,5))
print(a1)

# 2 largest number
x=np.array([12,4,43,100,54,68])
print(x[np.argsort(x)[-2:][::-1]])


