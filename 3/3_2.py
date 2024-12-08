import sys
import re


def parse_and_split(data):
    # Split the data into segments based on "do()" or "don't()"
    segments = re.split(r"(do\(\)|don't\(\))", data)
    parsed_segments = []

    # Iterate through the segments and tag them with their state
    current_state = True  # Default state is enabled
    for segment in segments:
        if segment == "do()":
            current_state = True
        elif segment == "don't()":
            current_state = False
        else:
            # Non-state segment: Add it with the current state
            parsed_segments.append((segment, current_state))
    
    return parsed_segments

def compute_data(parsed_segments, mul_pattern):
    total = 0

    for segment, enabled in parsed_segments:
        if enabled:
            # Find all mul instructions in the enabled segment
            matches = re.findall(mul_pattern, segment)
            total += sum(int(x) * int(y) for x, y in matches)
    
    return total

pattern_mul = r"mul\((\d{1,3}),(\d{1,3})\)"

#Data input
print("Paste your data (finish input with Ctrl+Z + enter on Windows or Ctrl+D + enter on Linux/macOS):")
input_data = sys.stdin.read().strip()

# Parse and compute
parsed_segments = parse_and_split(input_data)
result = compute_data(parsed_segments, pattern_mul)

print(result)