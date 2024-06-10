import tkinter as tk

def calculate_pay():
    # Get inputs
    hours_worked = float(hours_entry.get())
    hourly_rate = float(rate_entry.get())

    # Calculate gross pay
    gross_pay = hours_worked * hourly_rate

    # Calculate deductions (assuming 20% tax rate)
    tax_deduction = gross_pay * 0.2
    net_pay = gross_pay - tax_deduction

    # Update labels
    gross_label.config(text="Gross Pay: $" + str(round(gross_pay, 2)))
    tax_label.config(text="Tax Deduction: $" + str(round(tax_deduction, 2)))
    net_label.config(text="Net Pay: $" + str(round(net_pay, 2)))

# Create the main window
root = tk.Tk()
root.title("Pay Slip Calculator")

# Create labels and entry fields
hours_label = tk.Label(root, text="Hours Worked:")
hours_label.grid(row=0, column=0, padx=5, pady=5)
hours_entry = tk.Entry(root)
hours_entry.grid(row=0, column=1, padx=5, pady=5)

rate_label = tk.Label(root, text="Hourly Rate ($):")
rate_label.grid(row=1, column=0, padx=5, pady=5)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1, padx=5, pady=5)

gross_label = tk.Label(root, text="Gross Pay:")
gross_label.grid(row=2, column=0, padx=5, pady=5)

tax_label = tk.Label(root, text="Tax Deduction:")
tax_label.grid(row=3, column=0, padx=5, pady=5)

net_label = tk.Label(root, text="Net Pay:")
net_label.grid(row=4, column=0, padx=5, pady=5)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_pay)
calculate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()