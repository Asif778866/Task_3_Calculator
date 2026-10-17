import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Error: Cannot divide by zero")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Error: Enter valid numbers")


# Main Window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x350")

# Heading
title_label = tk.Label(
    window,
    text="Calculator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)

# First Number
tk.Label(window, text="Enter First Number:").pack()
entry1 = tk.Entry(window)
entry1.pack(pady=5)

# Second Number
tk.Label(window, text="Enter Second Number:").pack()
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="+",
    width=8,
    command=lambda: calculate("+")
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="-",
    width=8,
    command=lambda: calculate("-")
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="×",
    width=8,
    command=lambda: calculate("*")
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="÷",
    width=8,
    command=lambda: calculate("/")
).grid(row=0, column=3, padx=5)

# Result
result_label = tk.Label(
    window,
    text="Result: ",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=20)

# Run Application
window.mainloop()