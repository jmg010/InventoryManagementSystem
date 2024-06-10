import tkinter as tk
from tkinter import messagebox

gross_entry = None
hours_entry = None
rate_entry = None
root = None

philHealth = 50
pagIbig = 50
tax = 55
loan = 100

DEDUCTION = philHealth + pagIbig + tax + loan

def select_contractual():
    root.withdraw() 
    open_contractual_window()

def select_regular():
    root.withdraw()
    open_regular_window()

def calculate_net_pay_regular():
    global gross_entry
    
    try:
        regular_gross = float(gross_entry.get())        
        net_pay = regular_gross - DEDUCTION
        
        messagebox.showinfo("Net Pay", f"Net Pay: ${net_pay:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for the Gross.")

def calculate_net_pay_contractual():
    global hours_entry, rate_entry
    
    try:
        hours = float(hours_entry.get())
        rate = float(rate_entry.get())
        
        gross = hours * rate
        net_pay = gross - DEDUCTION
        
        messagebox.showinfo("Net Pay", f"Net Pay: ${net_pay:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for hours and rate.")

def open_contractual_window():
    global hours_entry, rate_entry, root
    
    contractual_window = tk.Toplevel() 
    contractual_window.title("Contractual Window")
    contractual_window.geometry("400x400") 

    label = tk.Label(contractual_window, text="You selected Contractual!")
    label.grid(row=0, column=0, columnspan=2, pady=10)


    hours_label = tk.Label(contractual_window, text="Number of Hours:")
    hours_label.grid(row=1, column=0, pady=5)
    hours_entry = tk.Entry(contractual_window)
    hours_entry.grid(row=1, column=1, pady=5)

    rate_label = tk.Label(contractual_window, text="Rate per Hour or Daily Rate:")
    rate_label.grid(row=2, column=0, pady=5)
    rate_entry = tk.Entry(contractual_window)
    rate_entry.grid(row=2, column=1, pady=5)

    PHealth_label = tk.Label(contractual_window, text="PhilHealth: $50")
    PHealth_label.grid(row=3, column=0, padx=5, pady=5)

    PI_label = tk.Label(contractual_window, text="Pag-Ibig: $50")
    PI_label.grid(row=4, column=0, padx=5, pady=5)

    tax_label = tk.Label(contractual_window, text="Tax: $55")
    tax_label.grid(row=5, column=0, padx=5, pady=5)

    loan_label = tk.Label(contractual_window, text="Loan: $100")
    loan_label.grid(row=6, column=0, padx=5, pady=5)


    calculate_button = tk.Button(contractual_window, text="Calculate Net Pay", command=calculate_net_pay_contractual)
    calculate_button.grid(row=7, column=0, columnspan=2, pady=10)

    back_button = tk.Button(contractual_window, text="Back", command=lambda: go_back(contractual_window))
    back_button.grid(row=8, column=0, columnspan=2, pady=5)

def open_regular_window():
    global root, gross_entry
    
    regular_window = tk.Toplevel()  
    regular_window.title("Regular Window")
    regular_window.geometry("400x400")

    label = tk.Label(regular_window, text="You selected Regular!")
    label.grid(row=0, column=0, columnspan=2, pady=10)

    gross_label = tk.Label(regular_window, text="Gross:")
    gross_label.grid(row=1, column=0, pady=5)
    gross_entry = tk.Entry(regular_window)
    gross_entry.grid(row=1, column=1, pady=5)

    PHealth_label = tk.Label(regular_window, text="PhilHealth: $50")
    PHealth_label.grid(row=2, column=0, padx=5, pady=5)

    PI_label = tk.Label(regular_window, text="Pag-Ibig: $50")
    PI_label.grid(row=3, column=0, padx=5, pady=5)

    tax_label = tk.Label(regular_window, text="Tax: $55")
    tax_label.grid(row=4, column=0, padx=5, pady=5)

    loan_label = tk.Label(regular_window, text="Loan: $100")
    loan_label.grid(row=5, column=0, padx=5, pady=5)

    calculate_button = tk.Button(regular_window, text="Calculate Net Pay", command=calculate_net_pay_regular)
    calculate_button.grid(row=6, column=0, pady=10)

    back_button = tk.Button(regular_window, text="Back", command=lambda: go_back(regular_window))
    back_button.grid(row=6, column=1, pady=5)

def go_back(window):
    window.destroy() 
    root.deiconify() 

def open_main_window():
    global root
    

    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x200") 


    label = tk.Label(root, text="Select Employment Type")
    label.grid(row=0, column=0, columnspan=2, pady=10)

 
    contractual_button = tk.Button(root, text="Contractual", command=select_contractual)
    contractual_button.grid(row=1, column=0, pady=5)

    regular_button = tk.Button(root, text="Regular", command=select_regular)
    regular_button.grid(row=1, column=1, pady=5)


    root.mainloop()


open_main_window()
