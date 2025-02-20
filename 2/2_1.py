import numpy as np
import sys

def isSafe(report):
    increasing = all(report[i] < report[i+1] and 
                     report[i+1] - report[i] <= 3 
                     for i in range(len(report)-1))
    decreasing = all(report[i] > report[i+1] and 
                     report[i] - report[i+1] <= 3 
                     for i in range(len(report)-1))
    return increasing or decreasing

#Lists input
print("Paste your reports (finish input with Ctrl+Z + enter on Windows or Ctrl+D + enter on Linux/macOS):")
reports_list = [np.fromstring(line.strip(), dtype=int, sep=' ') for line in sys.stdin]

reports_safe = [isSafe(report) for report in reports_list]
safe_count = sum(reports_safe)

print(safe_count, " reports are safe!")