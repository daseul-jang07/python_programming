from tkinter import *
from time import *

## 전역 변수 선언 부분 ##
fnameList = [
    "C:/Users/ds271/OneDrive/바탕 화면/python.ex.gif", "C:/Users/ds271/OneDrive/바탕 화면/python.ex2.gif",
    "C:/Users/ds271/OneDrive/바탕 화면/python.ex3.gif", "C:/Users/ds271/OneDrive/바탕 화면/python.ex4.gif",
    "C:/Users/ds271/OneDrive/바탕 화면/python.ex5.gif", "C:/Users/ds271/OneDrive/바탕 화면/python.ex6.gif",
    "C:/Users/ds271/OneDrive/바탕 화면/python.ex7.gif", "C:/Users/ds271/OneDrive/바탕 화면/python.ex8.gif",
    "C:/Users/ds271/OneDrive/바탕 화면/python.ex9.gif"]
photoList = [None]*9
num = 0

## 함수 선언 부분 ##
def get_filename(path):
    return path.split('/')[-1]  # 슬래시로 나눠서 마지막 항목(파일명) 반환

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file = "" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    fileLabel.config(text=get_filename(fnameList[num]))

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file = "" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    fileLabel.config(text=get_filename(fnameList[num]))

def updateImage():
    global photo, fileLabel
    photo = PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    fileLabel.config(text=get_filename(fnameList[num]))  # 파일명만 표시

## 메인 코드 부분 ##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)

fileLabel = Label(window, text=get_filename(fnameList[num]))  # 시작 시 파일명만 표시

photo = PhotoImage(file = "" + fnameList[0])
pLabel = Label(window, image = photo)

# 배치
btnPrev.place(x=250, y=10)
fileLabel.place(x=310, y=12)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
