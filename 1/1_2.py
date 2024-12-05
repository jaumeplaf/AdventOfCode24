import numpy as np
import sys

def getDistance(list1, list2):
    
    sorted_list1 = np.sort(list1)
    sorted_list2 = np.sort(list2)
    total_distance = np.sum(np.abs(sorted_list2 - sorted_list1))
    return total_distance

def getSimilarityScore(list1, list2):
    counts = np.array([np.sum(list2 == elem) for elem in list1])
    similarity_score = np.sum(list1 * counts)
    return similarity_score

#Lists input
print("Paste your numbers (finish input with Ctrl+Z + enter on Windows or Ctrl+D + enter on Linux/macOS):")
nums = np.fromstring(sys.stdin.read(), dtype=int, sep=' ')
if nums.size % 2 != 0:
        raise ValueError(f"List elements mismatch, provide even number of elements!")

#Separate lists
list1 = nums[::2]
list2 = nums[1::2]

print("Total distance: ", getDistance(list1, list2))
print("Similarity score: ", getSimilarityScore(list1, list2))