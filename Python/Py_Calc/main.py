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

    def is_float(self,str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False
    def math_button_press(self,value):
        if self.is_float(str(self.number_entry.get())):
            self.add_trigger = False
            self.sub_trigger = False
            self.mult_trigger = False
            self.div_trigger = False
            self.calc_value = float(self.entry_value.get())
            if value == "/":
                print("/ Pressed")
                self.div_trigger = True
            elif value == "*":
                print("* Pressed")
                self.div_trigger = True
            elif value == "+":
                print("+ Pressed")
                self.add_trigger = True
            else:
                print("- Pressed")
                self.sub_trigger = True
            self.number_entry.delete(0,"end")

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


