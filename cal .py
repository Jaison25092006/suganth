import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("400x600")
window.title("Simple Calculator")

# Display for the input and result
entry = tk.Entry(window, font=("Arial", 20), bd=10, relief="sunken", width=15, justify="right")
entry.pack()

# Creating buttons for the calculator
button_frame = tk.Frame(window)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 0
col = 0

# String to store the current expression
expression = ""

for button in buttons:
    def btn_click(b=button):
        
        if b == "=":
            try:
                expression = str(eval(expression))
            except:
                expression = "Error"
        else:
            expression += b
        entry.delete(0, tk.END)
        entry.insert(0, expression)
    
    b = tk.Button(button_frame, text=button, font=("Arial", 20), width=4, height=2, command=btn_click)
    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear Button
clear_button = tk.Button(window, text="Clear", font=("Arial", 20), width=15, height=2, command=lambda: entry.delete(0, tk.END))
clear_button.pack()

# Start the GUI loop
window.mainloop()
