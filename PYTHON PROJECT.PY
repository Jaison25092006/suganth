import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        self.expression = ""  # Stores the current equation
        self.input_text = tk.StringVar()  # Variable to update Entry widget

        # Entry field
        self.entry = tk.Entry(root, textvariable=self.input_text, font=('Arial', 18), bd=10, relief="ridge", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, font=('Arial', 16), bd=5, width=5, height=2, 
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""  # Clear input
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))  # Evaluate expression
            except:
                self.expression = "Error"  # Handle errors
        else:
            self.expression += char  # Append character to expression
        
        self.input_text.set(self.expression)  # Update display

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
#write a python program to print 10 except 7 natural number using control structure using for loop