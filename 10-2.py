from tkinter import *
import random

## 전역 변수 선언 부분 ##
btnList = [None] * 9
fnameList = [
    "C:/Users/ds271/OneDrive/바탕 화면/python.ex.gif", "C:/Users/ds271/OneDrive/바탕 화면/python.ex2.gif",
    "C:/Users/ds271/OneDrive/바탕 화면/python.ex3.gif", "C:/Users/ds271/OneDrive/바탕 화면/python.ex4.gif",
    "C:/Users/ds271/OneDrive/바탕 화면/python.ex5.gif", "C:/Users/ds271/OneDrive/바탕 화면/python.ex6.gif",
    "C:/Users/ds271/OneDrive/바탕 화면/python.ex7.gif", "C:/Users/ds271/OneDrive/바탕 화면/python.ex8.gif",
    "C:/Users/ds271/OneDrive/바탕 화면/python.ex9.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

random.shuffle(fnameList)

for i in range(0, 9):
    photoList[i] = PhotoImage(file = "" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])
for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()