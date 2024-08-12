# Reference: https://076923.github.io/posts/Python-tkinter-2/

import tkinter

window=tkinter.Tk()
window.title("James Yu")
window.geometry("640x400+100+100")
window.resizable(False, False)

label=tkinter.Label(window, text="Python", width=10, height=5, fg="red", relief="solid")
label.pack()

window.mainloop()

# tkinter.Label(윈도우 창, 매개변수1, 매개변수2, 매개변수3, ...)을 사용하여 해당 윈도우 창에 표시할 라벨의 속성을
# 설정할 수 있습니다.
# 매개변수를 사용하여 라벨의 속성을 설정합니다.