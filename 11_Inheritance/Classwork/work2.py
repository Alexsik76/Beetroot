import numpy as np

a = np.random.randint(0, 100, (3, 3))
b = np.random.randint(0, 100, (3, 3))

c = a + b
print(c)
print('=' * 80)
print(a)
print('=' * 80)
c = a * 3
print(c)
print('=' * 80)
c = a * b
print(c)
print('=' * 80)
c = a.transpose()
print(c)
print('=' * 80)
c = np.linalg.inv(a)
print(c)