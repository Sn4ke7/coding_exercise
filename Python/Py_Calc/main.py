from tkinter import *
from tkinter import ttk

class Calculator:
    calc_value = 0.0
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0,"end")
        self.number_entrt.insert(0, entry_val)

if __name__ == '__main__':
    calcGUI = Tk()
    calcGUI.geometry("500x500")
    calcGUI.title("Calc")
    l1 = Label(calcGUI, text="Calculate:").pack()
    entry1 = Entry(calcGUI).pack()
    B = Button(calcGUI, text="Sum").pack()
    # mainloop at the end
    calcGUI.mainloop()
    pass


