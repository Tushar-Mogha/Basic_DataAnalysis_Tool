# Basic Data Analysis and Visualization Tool

This project is a Python script that performs basic data analysis and visualization using `pandas` and `numpy`. It allows users to load a CSV file, calculate key statistical metrics (mean, median, and mode), and visualize the results using histograms.

---

## Features
1. **Load a CSV File**:
   - The script reads a CSV file into a pandas DataFrame using `pandas.read_csv`.

2. **Basic Statistical Analysis**:
   - Calculates the **mean**, **median**, and **mode** for each numeric column in the dataset.
   - Outputs these metrics to the console for quick reference.

3. **Visualization**:
   - Generates histograms for all numeric columns to visualize the data distribution.
   - Uses `matplotlib` for plotting.

---

## How It Works
### Input
- A CSV file containing numeric and non-numeric data. Ensure that the file is correctly formatted and accessible to the script.
- Example input format (data.csv):
  
  Age,Height,Weight
  25,175,70
  30,180,80
  22,165,55
