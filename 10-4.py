from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def keyEvent(event):
    direction = ""

    if event.state & 0x0001:  # Shift 키가 눌렸는지 확인 (state 플래그 체크)
        if event.keycode == 37:
            direction = "왼쪽 화살표"
        elif event.keycode == 38:
            direction = "위쪽 화살표"
        elif event.keycode == 39:
            direction = "오른쪽 화살표"
        elif event.keycode == 40:
            direction = "아래쪽 화살표"

        if direction != "":
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + " + direction)

## 메인 코드 부분 ##
window = Tk()
window.title("키보드 이벤트")
window.geometry("300x100")

window.bind("<Key>", keyEvent)

window.mainloop()
