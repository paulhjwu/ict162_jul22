from timecheck import validateTime

from tkinter import *
from tkinter.scrolledtext import *

class GuiDemo:
    def __init__(self):
        self._win = Tk()
        self._win.title("GUI Timecheck")
        self._win.geometry('300x200')
        self.createWidgets()
        self._win.mainloop() 
    
    def createWidgets(self):
        self._txtName = Entry(width=15)
        self._lblName = Label(text="Enter Time (Hint hh:mm) ")
        self._btnCheck = Button(text="Check", command=self.btnClick)
        self._sclOutput = ScrolledText(width=35, height=5, state=DISABLED)

        self._txtName.grid(row=0, column=1)
        self._lblName.grid(row=0, column=0)

        self._btnCheck.grid(row=1, columnspan = 2)
        self._sclOutput.grid(row=2, columnspan = 2)

    def displayOutput(self, message):
        self._sclOutput.configure(state=NORMAL)
        self._sclOutput.insert(END, message+'\n')
        self._sclOutput.configure(state=DISABLED)

    def btnClick(self):
        timeStr = self._txtName.get()

        try:
            validateTime(timeStr)
            self.displayOutput("The format is valid")
        except Exception as e:
            self.displayOutput(f'{e}')

if __name__ == "__main__":
    GuiDemo()




