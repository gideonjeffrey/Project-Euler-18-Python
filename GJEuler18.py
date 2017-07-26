# Project-Euler-18-Python

from math import floor, sqrt

def first_tri_after(n):
  # returns the first triangular number greater than n.
  if n < 0:
    n == 0
  start = 1
  to_add = 2
  while start <= n:
    start += to_add
    to_add += 1
  return start
  
def last_tri_before(n):
  # returns the last triangular number less than n.
  if n < 2:
    return "No triangular numbers less than 1 exist."
  start = 1
  to_add = 2
  while start < n:
    start += to_add
    to_add += 1
  return start - to_add + 1
  
triangle_array = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

def triangle_maximum_sum_path(array):
  # finds the maximum path sum down a triangular array from top to bottom.
  initial = last_tri_before(len(array))
  for i in range(initial - 1, -1, -1):
    step = floor(sqrt(2 * first_tri_after(i)))
    if array[i + step] >= array[i + step + 1]:
      array[i] = array[i] + array[i + step]
    else:
      array[i] = array[i] + array[i + step + 1]
  return array[0]

print(triangle_maximum_sum_path(triangle_array))

#answer: 1074
