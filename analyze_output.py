import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend to avoid CoreGraphics PDF errors
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Specify the file path
file_path = '/Users/tomoury/Desktop/NeurX/Simulation_Data/output_NeurX_hybrid_system_v0.02.txt'

# Read the file content
with open(file_path, 'r') as file:
    lines = file.readlines()

# Find the line where the actual data starts
for i, line in enumerate(lines):
    if line.strip().startswith('Index'):
        start_idx = i + 1
        break

# Extract the header and data lines
header = lines[start_idx - 1].strip().split()
data_lines = lines[start_idx:]

# Clean and preprocess the data
data = []
for line in data_lines:
    # Remove any extra spaces and split the line into fields
    fields = line.strip().split()
    if len(fields) == len(header):
        data.append(fields)

# Create a DataFrame
df = pd.DataFrame(data, columns=header)

# Convert columns to appropriate data types
df = df.apply(pd.to_numeric, errors='ignore')

# Display the first few rows to understand the structure
print(df.head())

# Plot the data
plt.figure(figsize=(10, 6))

# Plot voltage at node c1 over time
plt.plot(df['time'], df['c1'], label='c1')
plt.plot(df['time'], df['c3'], label='c3')
plt.plot(df['time'], df['c4'], label='c4')

# Add labels, title, and legend
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Transient Analysis of NeurX Hybrid System')
plt.legend()

# Improve axis labeling with MaxNLocator
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.gca().xaxis.set_major_locator(MaxNLocator(prune='both'))
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.gca().yaxis.set_major_locator(MaxNLocator(prune='both'))

# Grid and show the plot
plt.grid(True)
plt.tight_layout()

# Save the plot as an SVG file for better scalability
plt.savefig('/Users/tomoury/Desktop/NeurX/Simulation_Data/output_NeurX_hybrid_system_v0.02_transient_analysis.svg')

# Show the plot
plt.show()