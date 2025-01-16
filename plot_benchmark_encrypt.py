import json
import matplotlib.pyplot as plt
import numpy as np
import math


"""
1. Generate data
pytest --benchmark-json=benchmark_data.json --benchmark-only

2. Show the plot
python plot_benchmark_encrypt.py
"""

with open('./benchmark_data.json') as f:
    data = json.load(f)

# Extract the sizes and times
sizes = []
times = []
for benchmark in data['benchmarks']:
    sizes.append(int(benchmark['params']['size']))
    times.append(benchmark['stats']['mean'])

# Convert sizes and times to numpy arrays for plotting
sizes = np.array(sizes)
times = np.array(times)

# Scale the times to a more readable range
times = times * 1e6  # Scale times to microseconds

# Plot the benchmark data
plt.plot(sizes, times, marker='o', label='Benchmark Data')

# Plot common Big O complexity lines for comparison
plt.plot(sizes, np.ones_like(sizes) * times[0], label='O(1), O(log n)')
# plt.plot(sizes, np.log(sizes), label='O(log n)')
plt.plot(sizes, sizes, label='O(n)')
plt.plot(sizes, sizes * np.log(sizes), label='O(n log n)')

# Add labels and title
plt.xlabel('Input Size')
plt.ylabel('Time (microseconds)')
plt.title('Big O Plot of AES Encryption')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()