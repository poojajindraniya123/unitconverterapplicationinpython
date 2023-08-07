import tkinter as tk
from tkinter import ttk

# Create the main application window
app = tk.Tk()
app.title("Unit Converter")
app.geometry("300x200")

# Entry widget for user input
input_entry = tk.Entry(app, width=10)
input_entry.pack(pady=10)

# Dropdown menus for source and target units
source_unit_var = tk.StringVar()
source_unit_var.set("cm")
source_unit_dropdown = ttk.Combobox(app, textvariable=source_unit_var, values=["cm", "m", "g", "kg"])
source_unit_dropdown.pack(pady=5)

target_unit_var = tk.StringVar()
target_unit_var.set("m")
target_unit_dropdown = ttk.Combobox(app, textvariable=target_unit_var, values=["cm", "m", "g", "kg"])
target_unit_dropdown.pack(pady=5)

# Label to display the converted result
result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Function to perform the conversion
def convert():
    try:
        value = float(input_entry.get())
        source_unit = source_unit_var.get()
        target_unit = target_unit_var.get()

        if source_unit == "cm" and target_unit == "m":
            result = value / 100.0
        elif source_unit == "m" and target_unit == "cm":
            result = value * 100.0
        elif source_unit == "g" and target_unit == "kg":
            result = value / 1000.0
        elif source_unit == "kg" and target_unit == "g":
            result = value * 1000.0
        else:
            result = value

        result_label.config(text=f"Result: {result} {target_unit}")
    except ValueError:
        result_label.config(text="Invalid input")

# Button to initiate the conversion
convert_button = tk.Button(app, text="Convert", command=convert)
convert_button.pack(pady=10)

app.mainloop()
