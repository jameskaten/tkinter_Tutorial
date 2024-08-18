# Reference: https://076923.github.io/posts/Python-tkinter-3/

import tkinter

window=tkinter.Tk()
window.title("JAMES")
window.geometry("640x400+100+100")
window.resizable(False, False)

count=0

def countUP():
    global count
    count += 1
    label.config(text=str(count))

label = tkinter.Label(window, text="0")
label.pack()

button = tkinter.Button(window, overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()


# tkinter.Button(윈도우 창, 매개변수1, 매개변수2, 매개변수3, ...)을 사용하여 해당 윈도우 창에 표시할 버튼의 속성을 설정
#
# 매개변수를 사용하여 버튼의 속성을 설정합니다.
#
# 매개변수 중 command를 이용하여 사용자 정의 함수 : countUP을 실행시킬 수 있습니다.