import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        result_label.config(text="Result: " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Invalid input!")

def show_about():
    messagebox.showinfo("About Calculator", "Basic Calculator App\nVersion 1.0")

# Main window
window = tk.Tk()
window.title("Basic Calculator")

# Menu bar
menubar = tk.Menu(window)

# File menu (you can add more options later)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

# Help menu with About
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_about)  # Add About command
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)  # Attach the menu bar to the window

# Input fields
label_num1 = tk.Label(window, text="First Number:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Second Number:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Operation selection
operation_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/']
for op in operations:
    radio_op = tk.Radiobutton(window, text=op, variable=operation_var, value=op)
    radio_op.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Result label
result_label = tk.Label(window, text="Result: ")
result_label.pack()

window.mainloop()