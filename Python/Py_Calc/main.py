from tkinter import *
from tkinter import ttk

class Calculator:
    print("Test")

    def __init__(self, root):
        self.entry_value = StringVar(root, value="")
        root = Tk()
        root.geometry("1000x1000")
        root.title("Calculator")
        calc = Calculator(root)
        root.mainloop()
# TODO : Create and functionality for buttons

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    top = Tk()
    top.mainloop()
    top.geometry("1000x1000")
    top.title("Calc")
    pass


