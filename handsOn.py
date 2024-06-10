import tkinter as tk
from tkinter import messagebox

# Constants
DEDUCTION = 500  # Example deduction value

def calculate_net_pay():
    try:
        hours = float(hours_entry.get())
        rate = float(rate_entry.get())
        
        gross = hours * rate
        net_pay = gross - DEDUCTION
        
        messagebox.showinfo("Net Pay", f"Net Pay: ${net_pay:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for hours and rate.")

# Create the main window
root = tk.Tk()
root.title("Net Pay Calculator")

# Number of Hours Entry
hours_label = tk.Label(root, text="Number of Hours:")
hours_label.pack(pady=5)
hours_entry = tk.Entry(root)
hours_entry.pack(pady=5)

# Rate per Hour or Daily Rate Entry
rate_label = tk.Label(root, text="Rate per Hour or Daily Rate:")
rate_label.pack(pady=5)
rate_entry = tk.Entry(root)
rate_entry.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Net Pay", command=calculate_net_pay)
calculate_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
