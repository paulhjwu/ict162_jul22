import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import *

class InvalidDataError(Exception):
    '''Raised when data is out of range'''
    
class BMICalculator:
    @classmethod
    def heightInRange(cls, height):
        if height < 0.5: 
            raise InvalidDataError("Height must be at least 0.5 meters")
        if height > 2.6:
            raise InvalidDataError("Height must be less than 2.6 meters")
        return True
    
    @classmethod
    def weightInRange(cls, weight):
        if weight < 10: 
            raise InvalidDataError("Weight must be at least 10 kg")
        if weight > 150:
            raise InvalidDataError("Weight must be less than 150 kg")
        return True
    
    @classmethod
    def bmi(cls, h, w):
        if cls.heightInRange(h) and cls.weightInRange(w):
            return w/(h * h)
    
class BMIGui:
    def __init__(self):
        self._win = Tk()
        # self._win.resizable(False, False)
        self._win.title("BMI Calculator")
        self.create_widgets()
        self._win.mainloop()
        
    def create_widgets(self):
        
        dataFrame = Frame(self._win)
        dataFrame.grid(row = 0, column = 0)
        
        self._wt_lbl = Label(dataFrame, text = "Weight (kilogram):")
        self._wt_lbl.grid(row=0, column=0, sticky="W")
        self._weight = StringVar()
        self._wt_Ety = Entry(dataFrame, width=18, textvariable=self._weight)
        self._wt_Ety.grid(row=0, column=1)
        
        self._ht_lbl = Label(dataFrame, text = "Height :")
        self._ht_lbl.grid(row=1, column=0, sticky="W")
        self._height = StringVar()
        self._ht_Ety = Entry(dataFrame, width=18, textvariable=self._height)
        self._ht_Ety.grid(row=1, column=1)
        
        radioFrame = Frame(dataFrame)
        radioFrame.grid(row = 2, column=1)
        self._radValue = IntVar()
        self._ht_m_rdbtn = Radiobutton(radioFrame, text="m", variable = self._radValue, value = 0)
        self._ht_cm_rdbtn = Radiobutton(radioFrame, text="cm", variable = self._radValue, value = 1)
        self._ht_m_rdbtn.grid(column=0, row=0, sticky=W)
        self._ht_cm_rdbtn.grid(column=1, row=0, sticky=W)
        
        actionFrame = Frame(dataFrame)
        actionFrame.grid(row=3, column=1)
        
        self._calc_btn = Button(actionFrame, text="Calculate", command=self.calcBMI)
        self._calc_btn.pack(side = LEFT)
        
        self._clear_btn = Button(actionFrame, text="Clear", command=self.clear)
        self._clear_btn.config(state = DISABLED)
        self._clear_btn.pack(side = LEFT)
        
        outputFrame = Frame(self._win)
        outputFrame.grid(column=0, row=1, padx=0, pady=4, columnspan = 2)
        self._scrol_stxt = ScrolledText(outputFrame, width= 50, height = 5, wrap=WORD)
        self._scrol_stxt.grid(column=0, row=0, columnspan = 2)
        self._scrol_stxt.config(state = DISABLED)
        
    def calcBMI(self):
        
        self._scrol_stxt.config(state = NORMAL)
        try: 
            h = float(self._height.get())
            if self._radValue.get() == 1:
                h = h/100
            w = float(self._weight.get())
            result = BMICalculator.bmi(h, w)
        except Exception as e:
            self._scrol_stxt.insert(END, str(e) + '\n')
        else:
            print(f'Weight {w:.1f}kg, Height {h:.2f}m, BMI = {result:.2f}\n')
            self._scrol_stxt.insert(END, f'Weight {w:.1f}kg, Height {h:.2f}m, BMI = {result:.2f}\n')
        finally:
            # self._scrol_stxt.see(END)
            self._scrol_stxt.config(state = DISABLED)
            self._height.set("")
            self._weight.set("")
            self._clear_btn.config(state = NORMAL)
    
    def clear(self):
        self._scrol_stxt.config(state = NORMAL)
        self._scrol_stxt.delete(1.0,END)
        self._scrol_stxt.config(state = DISABLED)
        self._clear_btn.config(state = DISABLED)
            
if __name__ == "__main__":
    BMIGui()
    
