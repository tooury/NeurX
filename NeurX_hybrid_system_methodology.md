# NeurX Hybrid Memristor-Spintronics System Test Procedure

## Version Information

- **Current Version:** v0.02
- **Previous Version:** v0.01

## Introduction

This document outlines the steps to verify the functionality of the NeurX hybrid memristor-spintronics system using Ngspice. It includes instructions for running simulations, inspecting results, and ensuring the system operates as intended.

___

## Manual Procedure for Creating Output with Ngspice

### Step 1: Open Ngspice
Open the terminal and start Ngspice by typing:
```sh
ngspice
```

### Step 2: Load the Circuit File

In the Ngspice interactive shell, load the circuit file:

```sh
source /Users/tomoury/Desktop/NeurX/NeurX_hybrid_system_v0.02.cir
```

You should see the following output:

```sh
Note: No compatibility mode selected!

Circuit: * neurx hybrid memristor-spintronics system v0.02
```

### Step 3: Run the Transient Analysis

Run the transient analysis with the following command:

```sh
tran 1n 100n
```

You should see output indicating the analysis is being performed:

```sh
Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Initial Transient Solution
--------------------------

Node                                   Voltage
----                                   -------
vdd                                        1.8
s1                                           0
s3                                           0
s4                                           0
c1                                           0
c3                                           0
c4                                           0
n5                                           0
n6                                           0
vspin2#branch                                0
vspin1#branch                                0
vcomp1#branch                                0
vstore1#branch                               0
vdd#branch                                   0

No. of Data Rows : 299
```

### Step 4: Print All Data to a File

Redirect the output to a file with the following command:

```sh
print all > /Users/tomoury/Desktop/NeurX/Simulation_Data/output_NeurX_hybrid_system_v0.02.txt
```

This command saves the output data to the specified file.

### Step 5: Verify the Output

Check the specified directory for the output file:

```sh
/Users/tomoury/Desktop/NeurX/Simulation_Data/output_NeurX_hybrid_system_v0.02.txt
```

Open the file to ensure the data has been correctly saved.


### Notes:
- Ensure that the file paths are correct and that the directories exist.
- Adjust the circuit file path and output file name as needed for different versions or scenarios.

This procedure allows you to manually perform the simulation and save the output data using Ngspice.

___

## Analysis

### Set up a virtual environment

Set up a virtual Python environment for running the analysis. Below are the steps to create and activate a virtual environment, and then install the necessary packages for data analysis and plotting.

#### Step-by-Step Guide

1. **Install Python (if not already installed)**:
   - Verify Python installation:
     ```sh
     python --version
     ```
   - If Python is not installed, you can download and install it from [python.org](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment**:
   - Navigate to your project directory:
     ```sh
     cd /path/to/your/project
     ```
   - Create a virtual environment named `venv`:
     ```sh
     python -m venv venv
     ```

3. **Activate the Virtual Environment**:
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```

4. **Install Required Packages**:
   - While the virtual environment is activated, install `pandas` and `matplotlib`:
     ```sh
     pip install pandas matplotlib
     ```

5. **Create the Python Script for Analysis**:
   - Create a new Python script file named `analyze_output.py`:
     ```sh
     touch analyze_output.py
     ```
   - Open the file in your preferred text editor and add the following content:

     ```python
     import pandas as pd
     import matplotlib.pyplot as plt

     # Load the data
     data = pd.read_csv('/Users/tomoury/Desktop/NeurX/Simulation_Data/output_NeurX_hybrid_system_v0.02.txt', delim_whitespace=True)

     # Display the first few rows to understand the structure
     print(data.head())

     # Plot the data
     plt.figure(figsize=(10, 6))

     # Plot voltage at node c1 over time
     plt.plot(data['time'], data['c1'], label='c1')
     plt.plot(data['time'], data['c3'], label='c3')
     plt.plot(data['time'], data['c4'], label='c4')
     plt.plot(data['time'], data['s1'], label='s1')
     plt.plot(data['time'], data['n5'], label='n5')
     plt.plot(data['time'], data['n6'], label='n6')

     # Add labels and legend
     plt.xlabel('Time (s)')
     plt.ylabel('Voltage (V)')
     plt.title('Transient Analysis of NeurX Hybrid System')
     plt.legend()
     plt.grid(True)

     # Show the plot
     plt.show()
     ```

6. **Run the Analysis Script**:
   - Ensure the virtual environment is activated:
     ```sh
     source venv/bin/activate
     ```
   - Run the Python analysis script:
     ```sh
     python analyze_output.py
     ```

#### Summary of Commands

```sh
# Navigate to project directory
cd /path/to/your/project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # macOS/Linux
# .\venv\Scripts\activate  # Windows

# Install required packages
pip install pandas matplotlib

# Create and edit the analysis script
touch analyze_output.py
nano analyze_output.py  # Use any text editor to add the script content

# Run the analysis script
python analyze_output.py
```

By following these steps, you will have a virtual environment set up and ready to run your analysis script, allowing you to visualize and analyze the simulation data from your Ngspice output file.

___


## Plot Simulation Data using Matplotlib

It sounds like you have found a version of the script that meets your needs, with good control over the plot presentation using the built-in Matplotlib tools. Here’s the final version of your script for documentation and reference:

### Python Script for Plotting with Matplotlib (analyze_output.py)

```python
# analyze_output.py

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

# Show the plot
plt.show()
```

### Explanation

1. **Read and Parse Data**:
   - The script reads the content of the specified file and extracts the header and data lines.

2. **Create DataFrame**:
   - The data is cleaned, preprocessed, and converted into a Pandas DataFrame with appropriate data types.

3. **Plot Data**:
   - The script plots the voltages at nodes `c1`, `c3`, and `c4` over time.

4. **Improve Axis Labeling**:
   - The axis labels are improved using `MaxNLocator` for better readability.

5. **Save and Show Plot**:
   - The plot is saved as an SVG file for better scalability and then displayed.

This script should meet needs for visualizing the transient analysis of the NeurX hybrid system, with good control over the plot presentation.


___

## Simulation Steps

### 1. Verify Transient Analysis Output

- **Objective:** Ensure all signals are as expected.
- Ngspice provides a plot of voltages and currents over time for the defined components.

### 2. Inspect Specific Nodes and Currents

- **Plot Voltage at Node `S1`:**

  ```

  plot v(S1)

  ```

- **Plot Current Through Voltage Source `Vstore1`:**

  ```

  plot i(Vstore1)

  ```

### 3. Check Device Behavior

- **Memristors:**
  - Verify if their resistance is changing according to expectations.
- **Spintronic Elements:**
  - Check control signals and their responses.

### 4. Refine Simulation Parameters

- Adjust pulse widths, amplitudes, and the duration of the simulation if results are not as expected.

### 5. Capture and Analyze Data

- Export data from Ngspice for detailed analysis.

## Example Commands for Data Inspection

### Plotting Voltages

```

plot v(S1) v(S3) v(C1) v(C3)

```

### Plotting Currents

```

plot i(Vstore1) i(Vcomp1)

```

### Plotting Memristor Behavior

```

plot v(S1) v(S3)  ; Plot voltage across memristor MS1

```

### Checking Spintronic Elements

```

plot v(N5) v(N6)  ; Check control signals for spintronic elements

```

## Example Session Commands

### Start Ngspice and Load Netlist

```

ngspice NeurX_hybrid_system_v0.02.cir

```

### Plot Specific Node Voltages

```

plot v(S1) v(S3) v(C1) v(C3)

```

### Plot Currents Through Voltage Sources

```

plot i(Vstore1) i(Vcomp1)

```

### Zoom in on Specific Time Frame

- Use the cursor or commands to zoom in on specific regions of interest in your plot to get more detailed views of signal transitions.

### Export Data for Further Analysis

```

write output.dat all

```

## Analyzing and Validating Results

### Check for Expected Memristor Switching

- Verify if the memristor is switching between high and low resistance states by examining the voltages across and currents through the memristor nodes.

### Validate Spintronic Control Signals

- Ensure that the spintronic control signals are generating the expected responses and that the elements are behaving correctly.

### Refine and Iterate

- Based on initial findings, refine the netlist parameters and iterate to improve the accuracy and performance of the simulation.

## Scripting Tests for Repeatability

### Create a Sidecar File (e.g., `NeurX_hybrid_system_v0.02.scr`)

```

* Load the circuit
source NeurX_hybrid_system_v0.02.cir

- Plot Specific Node Voltages
plot v(S1) v(S3) v(C1) v(C3)

- Plot Currents Through Voltage Sources
plot i(Vstore1) i(Vcomp1)

- Export Data
write output_v0.02.dat all

- End the script
quit

```

### Run the Script with Ngspice

```

ngspice -b -r rawfile.raw NeurX_hybrid_system_v0.02.scr

```

This command runs Ngspice in batch mode, executing the commands in the sidecar file and saving the results in `rawfile.raw`.

## Conclusion

Follow these steps to validate and refine the NeurX hybrid memristor-spintronics system. Document any changes and updates to maintain a thorough version history and ensure repeatability in your simulations.
"""

with open("/mnt/data/NeurX_hybrid_system_test_procedure.md", "w") as file:
    file.write(test_procedure_content)
```
