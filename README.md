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

## Output
1. Console Output :
   - Displays the first few rows of the dataset.
   - Prints the calculated mean, median, and mode for each numeric column.

   Example console output:

### First few rows of the dataset:

   ![Screenshot 2024-11-21 170518](https://github.com/user-attachments/assets/080332c4-c937-44d3-84f9-950477ece44e)




### Basic Analysis:

#### Column: Age
- Mean: 25.67
- Median: 25.0
- Mode: 22

#### Column: Height
- Mean: 173.33
- Median: 175.0
- Mode: 165

#### Column: Weight
- Mean: 68.33
- Median: 70.0
- Mode: 55


2. Visualization :
   
   - Displays a histogram for all numeric columns, showing the distribution of data values.
   Example visualization :

   - Histograms for Age, Height, and Weight with distinct colors for each column.

---

### Requirements

- Python 3.x
- Libraries:
   - pandas
   - numpy
   -matplotlib

- To install the required libraries, run:

   - pip install pandas numpy matplotlib

---

### Usage

1. Place your CSV file in the same directory as the script or provide its path.
2. Update the file_path variable in the script to point to your CSV file.
3. Run the script :

   python script_name.py

---

### Output Interpretation


- Mean: The average value of the column.
- Median: The middle value when the column is sorted.
- Mode: The most frequently occurring value in the column.
- Histograms: Help visualize how values in each numeric column are distributed.



![Output_img](https://github.com/user-attachments/assets/c450d24f-b3f8-4742-a71a-5a4b2413f96f)
