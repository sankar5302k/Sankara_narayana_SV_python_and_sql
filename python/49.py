import tkinter as tk
from tkinter import messagebox
from tabulate import tabulate

class TemperatureConverter:
    @staticmethod
    def c_to_f(c): return c * 9/5 + 32
    
    @staticmethod
    def f_to_c(f): return (f - 32) * 5/9
    
    @staticmethod
    def c_to_k(c): return c + 273.15
    
    @staticmethod
    def k_to_c(k): return k - 273.15

class ConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("300x320")
        
        self.temp_var = tk.StringVar()
        
        tk.Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=15)
        tk.Entry(root, textvariable=self.temp_var, width=15).grid(row=0, column=1, padx=10, pady=15)
        
        btn_frame = tk.Frame(root)
        btn_frame.grid(row=1, column=0, columnspan=2)
        
        tk.Button(btn_frame, text="°C to °F", width=10, command=lambda: self.convert("CtoF")).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="°F to °C", width=10, command=lambda: self.convert("FtoC")).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="°C to K", width=10, command=lambda: self.convert("CtoK")).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="K to °C", width=10, command=lambda: self.convert("KtoC")).grid(row=1, column=1, padx=5, pady=5)
        
        self.result_label = tk.Label(root, text="", font=("Courier", 10), justify="left")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=15)

    def convert(self, mode):
        try:
            val = float(self.temp_var.get())
            if mode == "CtoF":
                res = TemperatureConverter.c_to_f(val)
                data = [["Celsius", f"{val:.2f} °C"], ["Fahrenheit", f"{res:.2f} °F"]]
            elif mode == "FtoC":
                res = TemperatureConverter.f_to_c(val)
                data = [["Fahrenheit", f"{val:.2f} °F"], ["Celsius", f"{res:.2f} °C"]]
            elif mode == "CtoK":
                res = TemperatureConverter.c_to_k(val)
                data = [["Celsius", f"{val:.2f} °C"], ["Kelvin", f"{res:.2f} K"]]
            elif mode == "KtoC":
                res = TemperatureConverter.k_to_c(val)
                data = [["Kelvin", f"{val:.2f} K"], ["Celsius", f"{res:.2f} °C"]]
            
            table = tabulate(data, headers=["Scale", "Value"], tablefmt="grid")
            self.result_label.config(text=table)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric temperature.")

root = tk.Tk()
app = ConverterGUI(root)
root.mainloop()
