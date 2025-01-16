import json
import numpy as np

with open('./benchmark/benchmark_data.json') as f:
    data = json.load(f)

# Extract the sizes and times
sizes = []
times = []
for benchmark in data['benchmarks']:
    sizes.append(int(benchmark['params']['size']))
    times.append(benchmark['stats']['mean'])

# Convert sizes and times to numpy arrays for plotting
sizes = np.array(sizes)
times = np.array(times) * 1000  # Convert times to milliseconds

# Generate Markdown table
markdown_table = "| Input Size | Time (milliseconds) |\n"
markdown_table += "|------------|---------------------|\n"
for size, time in zip(sizes, times):
    markdown_table += f"| {size} | {time:.6f} |\n"

print(markdown_table)