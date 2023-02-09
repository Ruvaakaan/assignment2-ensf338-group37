import time
from matplotlib import pyplot as plt

cache = {}

def func_new(n):
  if n == 0 or n == 1:
    return n
  elif n in cache:
    return cache[n]
  else:
    cache[n] = func_new(n-1) + func_new(n-2)
    return cache[n]

def func_old(n):
  if n == 0 or n == 1:
    return n
  else:
    return func_old(n-1) + func_old(n-2)

results1 = []
for i in range(36):
  start = time.time()
  func_old(i)
  stop = time.time()
  results1.append((i, stop-start))

x1 = [i for i, t in results1]
y1 = [t for i, t in results1]

results2 = []
for i in range(36):
  start = time.time()
  func_new(i)
  stop = time.time()
  results2.append((i, stop-start))

x2 = [i for i, t in results2]
y2 = [t for i, t in results2]    

plt.plot(x1, y1, 'b', label = "Original Function")
plt.plot(x2, y2, 'g', label = "Improved Function")
plt.xlabel("Number of Inputs, n")
plt.ylabel("Time, seconds")
plt.legend()
plt.show()
