import sys
import re


def parse_input(data, pattern):
    matches = re.findall(pattern, data)
    matches_list = [(int(x), int(y)) for x, y in matches]

    return matches_list

def compute_data(data_list, operation):
    if operation == "mul":
        total = sum([(x * y) for x, y in data_list])
    else:
        total = None

    return total

pattern_mul = r"mul\((\d{1,3}),(\d{1,3})\)"

#Data input
print("Paste your data (finish input with Ctrl+Z + enter on Windows or Ctrl+D + enter on Linux/macOS):")
input_data = sys.stdin.read().strip()
data_list = parse_input(input_data, pattern_mul)

print(compute_data(data_list, "mul"))