import tkinter as tk
from tkinter import *
from tkinter import ttk

class MyFirstGUI:
    def __init__(self):
        
        win = Tk()
        
    # 1. Create it, specify parent
    # hello_btn = ttk.Button(win, text="Hello")
        
        self._name_lbl = ttk.Label(win, text="Name:")
        self._name_ety = ttk.Entry(win, width=18)
        self._hello_btn = ttk.Button(win)
        self._output_lbl = ttk.Label(win)

    # 2. Configure it
    # hello_btn.configure(text="Hello")
    
        self._hello_btn.configure(text="Hello")
    
    # 3. Position it in container
    # hello_btn.pack(side = LEFT)
    
        self._name_lbl.pack(side = LEFT)
        self._name_ety.pack(side = LEFT)
        self._hello_btn.pack(side = LEFT)
        self._output_lbl.pack(side = LEFT)

    # 4. Listen to it
    # Events: callback function
    
        self._hello_btn.configure(command=self.sayHello)
        
        win.title('Hello World')
        win.geometry('500x50')
        win.resizable(False, False)
        win.mainloop()
        
    def sayHello(self):
        self._output_lbl.configure(text = 'Hello ' + self._name_ety.get())
        
if __name__ == "__main__":
    
    gui = MyFirstGUI()
    