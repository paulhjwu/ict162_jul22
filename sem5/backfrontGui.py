import tkinter as tk
from tkinter import *
from tkinter import ttk

from tkinter.scrolledtext import *

class DemoGUI:
    
    def __init__(self):
        
        win = Tk()
        
        top = Frame(win)
        self._back, self._front = 0, 0
        scrol_w, scrol_h = 30, 3
        self.scrol_stxt = ScrolledText(top, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrol_stxt.grid(column=0, row=0, sticky= NSEW)
        self.scrol_stxt.config(state = tk.DISABLED)
        self.scrol_stxt.grid(row = 0, column = 0, sticky =NSEW)
        top.grid(row = 0, column = 0)
        
        middle = Frame(win)
        self._top_btn = ttk.Button(middle, text="< to Front")
        self._top_btn.bind('<Button-1>', self.printSymbol)
        self._bottom_btn = ttk.Button(middle, text="> to Back")
        self._bottom_btn.bind('<Button-1>', self.printSymbol)
        self._clear_btn = ttk.Button(middle, text="Clear")
        self._clear_btn.bind('<Button-1>', self.clearSymbol)
        self._top_btn.pack(side=LEFT)
        self._bottom_btn.pack(side=LEFT)
        self._clear_btn.pack(side=LEFT)
        middle.grid(row=1, column=0)
        
        
        win.title('ScroledText World')
        win.geometry('500x250')
        win.resizable(False, False)
        win.mainloop()
            
    def printSymbol(self, evt):
        
        self.scrol_stxt.config(state = tk.NORMAL)
        if evt.widget == self._top_btn:
            self._front += 1
            self.scrol_stxt.insert(1.0, str(self._front) + '<')
        elif evt.widget == self._bottom_btn:
            self._back += 1
            self.scrol_stxt.insert(tk.END, '>' + str(self._back))
        self.scrol_stxt.see(tk.END)
        self.scrol_stxt.config(state = tk.DISABLED)
        
    def clearSymbol(self, evt):
        self.scrol_stxt.config(state = tk.NORMAL)
        self.scrol_stxt.delete(1.0,tk.END)
        self.scrol_stxt.config(state = tk.DISABLED)
        

    
if __name__ == "__main__":
    
    gui = DemoGUI()