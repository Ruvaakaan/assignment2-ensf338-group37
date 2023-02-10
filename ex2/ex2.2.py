import json
import sys
import matplotlib.pyplot as plt
import time

sys.setrecursionlimit(200000)

def func1(arr, low, high):
  if low < high:
    pi = func2(arr, low, high)
    func1(arr, low, pi-1)
    func1(arr, pi + 1, high)

def func2(array, start, end):
  p = array[start]
  low = start + 1
  high = end
  while True:
    while low <= high and array[high] >= p:
      high = high - 1
    while low <= high and array[low] <= p:
      low = low + 1
    if low <= high:
      array[low], array[high] = array[high], array[low]
    else:
      break
  array[start], array[high] = array[high], array[start]
  return high


with open("ex2.json","r") as infile:
  json_obj = json.load(infile)

results1 = []
for i in range(len(json_obj)):
  start = time.time()
  func1(json_obj[i], 0, len(json_obj[i])-1)
  stop = time.time()
  print(f"recursive: {stop-start}\n")
  results1.append((len(json_obj[i]), stop-start))

print(results1)
x1 = [i for i, t in results1]
y1 = [t for i, t in results1]

plt.plot(x1, y1, 'b')
plt.xlabel("Size of Input Array, n")
plt.ylabel("Time, seconds")
plt.show()


