from tkinter import *
import os

class LucineSlider:
    def __init__(self, parent):

        self.scale_var = DoubleVar()
        self.scale_var.set(10)
        self.w = Scale(parent, from_=1, to=10, orient=HORIZONTAL, command=self.setBrightness, width=80, sliderlength=80, variable=self.scale_var, length=800, bd=8, bg="#269")
        self.w.pack(anchor= CENTER)

    def setBrightness(self, num):
        value = self.w.get()/10
        lucineStr = "xrandr --output eDP-1 --brightness " + str(value)
        os.system(lucineStr)

finestrella = Tk()
finestrella.geometry("800x150")
finestrella.title("Screen brightness")

myFinestrella=LucineSlider(finestrella)
finestrella.mainloop()
