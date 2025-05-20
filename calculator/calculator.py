import tkinter as tk
from tkinter import font as tkfont

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Initialize variables
        self.current_input = "0"
        self.stored_value = None
        self.operation = None
        self.reset_input = False
        
        # Create custom font
        button_font = tkfont.Font(size=12, weight='bold')
        display_font = tkfont.Font(size=18)
        
        # Display
        self.display_var = tk.StringVar()
        self.display_var.set(self.current_input)
        self.display = tk.Label(
            root, 
            textvariable=self.display_var, 
            font=display_font, 
            anchor="e", 
            bg="white", 
            padx=10,
            pady=20
        )
        self.display.pack(fill=tk.X)
        
        # Button frame
        button_frame = tk.Frame(root)
        button_frame.pack(expand=True, fill=tk.BOTH)
        
        # Button layout (matches your image)
        buttons = [
            ['AC', 'C', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['MR', '0', '.', '=']
        ]
        
        # Create buttons
        for i, row in enumerate(buttons):
            button_frame.rowconfigure(i, weight=1)
            for j, btn_text in enumerate(row):
                button_frame.columnconfigure(j, weight=1)
                btn = tk.Button(
                    button_frame, 
                    text=btn_text, 
                    font=button_font,
                    command=lambda text=btn_text: self.on_button_click(text)
                )
                btn.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
                
                # Color special buttons
                if btn_text in ['AC', 'C', '%', '/', '*', '-', '+', '=']:
                    btn.config(bg='#f0a830', fg='white')
                elif btn_text == 'MR':
                    btn.config(bg='#a0a0a0', fg='white')
        
    def on_button_click(self, button_text):
        if button_text.isdigit():
            self.handle_digit(button_text)
        elif button_text == '.':
            self.handle_decimal()
        elif button_text in ['+', '-', '*', '/', '%']:
            self.handle_operation(button_text)
        elif button_text == '=':
            self.handle_equals()
        elif button_text == 'AC':
            self.handle_all_clear()
        elif button_text == 'C':
            self.handle_clear()
        elif button_text == 'MR':
            self.handle_memory_recall()
        
        self.update_display()
    
    def handle_digit(self, digit):
        if self.current_input == "0" or self.reset_input:
            self.current_input = digit
            self.reset_input = False
        else:
            self.current_input += digit
    
    def handle_decimal(self):
        if '.' not in self.current_input:
            self.current_input += '.'
    
    def handle_operation(self, op):
        if self.operation and not self.reset_input:
            self.calculate_result()
        self.stored_value = float(self.current_input)
        self.operation = op
        self.reset_input = True
    
    def handle_equals(self):
        if self.operation and not self.reset_input:
            self.calculate_result()
            self.operation = None
    
    def calculate_result(self):
        try:
            current_value = float(self.current_input)
            if self.operation == '+':
                result = self.stored_value + current_value
            elif self.operation == '-':
                result = self.stored_value - current_value
            elif self.operation == '*':
                result = self.stored_value * current_value
            elif self.operation == '/':
                result = self.stored_value / current_value
            elif self.operation == '%':
                result = self.stored_value % current_value
            
            self.current_input = str(result)
            self.stored_value = result
            self.reset_input = True
        except ZeroDivisionError:
            self.current_input = "Error"
            self.reset_input = True
    
    def handle_all_clear(self):
        self.current_input = "0"
        self.stored_value = None
        self.operation = None
        self.reset_input = False
    
    def handle_clear(self):
        self.current_input = "0"
        self.reset_input = False
    
    def handle_memory_recall(self):
        if self.stored_value is not None:
            self.current_input = str(self.stored_value)
            self.reset_input = False
    
    def update_display(self):
        if len(self.current_input) > 12:
            self.display_var.set(self.current_input[:12])
        else:
            self.display_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()