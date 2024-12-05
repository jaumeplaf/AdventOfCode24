import numpy as np
import sys

print("Paste your numbers (finish input with Ctrl+Z + enter on Windows or Ctrl+D + enter on Linux/macOS):")
nums = np.fromstring(sys.stdin.read(), dtype=int, sep=' ')

list1 = nums[::2]
list2 = nums[1::2]

if list1.size != list2.size:
    raise ValueError(f"List elements mismatch, provide even number of elements!")

sorted_list1 = np.sort(list1)
sorted_list2 = np.sort(list2)

total_distance = np.sum(np.abs(sorted_list2 - sorted_list1))

print("List 1:", sorted_list1)
print("List 2:", sorted_list2)
print("Total distance: ", total_distance)