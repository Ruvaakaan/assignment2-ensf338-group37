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

'''
def quicksort_iterative(array):
  stack = [(0, len(array) - 1)]
  while stack:
    low, high = stack.pop()
    if low < high:
      pivot = partition(array, low, high)
      stack.append((low, pivot - 1))
      stack.append((pivot + 1, high))

def partition(array, low, high):
  pivot = array[random.randint(low, high)]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
    array[i], array[j] = array[j], array[i]
  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1
'''

def quicksort_iterative1(array):
  stack1 = [(0, len(array) - 1)]
  while stack1:
    low, high = stack1.pop()
    if low < high:
      pivot = partition1(array, low, high)
      stack1.append((low, pivot - 1))
      stack1.append((pivot + 1, high))

def partition1(array, low, high):
  pivot = array[low]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
    array[i], array[j] = array[j], array[i]
  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1


with open("ex2.json","r") as infile:
  json_obj = json.load(infile)

results1 = []
for i in range(len(json_obj)):
  start = time.time()
  func1(json_obj[i], 0, len(json_obj[i])-1)
  stop = time.time()
  print(f"recursive: {stop-start}\n")

  start = time.time()
  quicksort_iterative1(json_obj[i])
  stop = time.time()
  print(f"iterative: {stop-start}\n")

  results1.append((len(json_obj[i]), stop-start))

print(results1)
x1 = [i for i, t in results1]
y1 = [t for i, t in results1]

plt.plot(x1, y1, 'b')
plt.xlabel("Size of Input Array, n")
plt.ylabel("Time, seconds")
plt.show()


