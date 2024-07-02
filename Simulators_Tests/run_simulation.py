import os
import subprocess

# Define the path to the circuit file
circuit_file = "NeurX_hybrid_system_v002.cir"

# Extract the version from the circuit file name
basename = os.path.basename(circuit_file)
version = ''.join(filter(str.isdigit, basename))

# Define the output directory
output_dir = "Simulation_Data"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define the output file name
output_file = os.path.join(output_dir, f"output_NeurX_hybrid_system_v{version}.txt")

# Create the Ngspice script content
ngspice_script_content = f"""
source {circuit_file}
tran 1n 100n
print all
quit
"""

# Debug: Print the paths and script content
print(f"Circuit file: {circuit_file}")
print(f"Output file: {output_file}")
print(f"Ngspice script content:\n{ngspice_script_content}")

# Write the Ngspice script to a temporary file
ngspice_script_file = "/tmp/run_simulation.scr"
with open(ngspice_script_file, "w") as f:
    f.write(ngspice_script_content)

# Debug: Print the path of the temporary Ngspice script file
print(f"Ngspice script file created at: {ngspice_script_file}")

# Run Ngspice with the script and capture output
result = subprocess.run(["ngspice", "-b", ngspice_script_file], capture_output=True, text=True)

# Check for errors in Ngspice output
if "error" in result.stderr.lower():
    print("Error occurred during simulation:")
    print(result.stderr)
else:
    # Write the standard output to the output file
    with open(output_file, "w") as f:
        f.write(result.stdout)
    print("Simulation completed successfully.")
    print(f"Output saved to {output_file}")

# Debug: Print Ngspice command output
print("Ngspice command output:")
print(result.stdout)
print(result.stderr)