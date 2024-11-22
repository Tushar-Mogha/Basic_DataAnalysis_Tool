import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, Button, Label, Text, END, messagebox

# Function to browse and load CSV file
def browse_csv():
    file_path = filedialog.askopenfilename(
        title="Select a CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )
    if file_path:
        analyze_csv(file_path)

# Function to analyze and visualize CSV data
def analyze_csv(file_path):
    try:
        # Load the CSV file
        data = pd.read_csv(file_path)

        # Display first few rows in the text area
        result_text.delete(1.0, END)
        result_text.insert(END, "First few rows of the dataset:\n")
        result_text.insert(END, data.head().to_string())
        result_text.insert(END, "\n\nBasic Analysis:\n")

        # Perform basic analysis
        for column in data.select_dtypes(include=np.number):
            mean = np.mean(data[column])
            median = np.median(data[column])
            mode = data[column].mode()[0]

            result_text.insert(
                END,
                f"\nColumn: {column}\nMean: {mean}\nMedian: {median}\nMode: {mode}\n"
            )

        # Create visualizations
        plt.figure(figsize=(10, 6))
        for column in data.select_dtypes(include=np.number):
            plt.hist(data[column], bins=15, alpha=0.5, label=column)

        plt.title("Histogram of Numeric Columns")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create GUI
root = Tk()
root.title("CSV Analyzer")
root.geometry("700x500")
root.configure(bg="#f7f7f7")

# Instructions
Label(root, text="Click the button below to browse and analyze a CSV file.", bg="#f7f7f7", font=("Arial", 12)).pack(pady=10)

# Browse Button
Button(
    root,
    text="Browse CSV File",
    command=browse_csv,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    width=20
).pack(pady=10)

# Text Area for Displaying Results
result_text = Text(root, wrap="word", font=("Courier", 10), height=20, width=80, bg="#ffffff")
result_text.pack(pady=10, padx=20)

# Run the GUI loop
root.mainloop()
