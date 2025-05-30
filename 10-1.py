from tkinter import *
window = Tk()

Photo1 = PhotoImage(file = "C:/Users/ds271/OneDrive/바탕 화면/python.ex.gif")
Photo2 = PhotoImage(file = "C:/Users/ds271/OneDrive/바탕 화면/python.ex2.gif")
label1 = Label(window, image = Photo1)
label2 = Label(window, image = Photo2)

label1.pack(side=LEFT)
label2.pack(side=RIGHT)

window.mainloop()