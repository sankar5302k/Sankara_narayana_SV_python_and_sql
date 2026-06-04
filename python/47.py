import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        self.result_var = tk.StringVar()
        self.result_var.set("")
        
        entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), bg="#eee", bd=10, justify="right")
        entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            tk.Button(root, text=text, font=("Arial", 18), width=4, height=2,
                      command=lambda t=text: self.on_click(t)).grid(row=row, column=col, padx=5, pady=5)
                      
    def on_click(self, char):
        current = self.result_var.get()
        
        if char == 'C':
            self.result_var.set("")
        elif char == '=':
            try:
                # evaluate the expression safely
                result = str(eval(current))
                self.result_var.set(result)
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.result_var.set("")
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.result_var.set("")
        else:
            self.result_var.set(current + char)

root = tk.Tk()
app = CalculatorGUI(root)
root.mainloop()
