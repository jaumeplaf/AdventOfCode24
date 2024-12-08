import numpy as np
import sys

def is_safe(report): #Check if the report is increasing/decreasing && contiguous elements have a distance <= 3
    increasing = all(report[i] < report[i+1] and 
                     report[i+1] - report[i] <= 3 
                     for i in range(len(report)-1))
    decreasing = all(report[i] > report[i+1] and 
                     report[i] - report[i+1] <= 3 
                     for i in range(len(report)-1))
    return increasing or decreasing

def is_safe_with_dampener(report): #Allow for one element of the report to be "bad"
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = np.concatenate((report[:i], report[i+1:]))
        if is_safe(modified_report):
            return True
    
    return False

#Reports input
print("Paste your reports (finish input with Ctrl+Z + enter on Windows or Ctrl+D + enter on Linux/macOS):")
reports_list = [np.fromstring(line.strip(), dtype=int, sep=' ') for line in sys.stdin]

#Check if it's safe
reports_safe = [is_safe_with_dampener(report) for report in reports_list]
safe_count = sum(reports_safe)

#Output
print(safe_count, " reports are safe!")