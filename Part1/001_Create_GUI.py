# install tkinter
# pip install tk
# Reference: https://076923.github.io/posts/Python-tkinter-1/

import tkinter

window=tkinter.Tk()

window.title("James")
window.geometry("640x400+100+100")
window.resizable(False, False)

label=tkinter.Label(window, text="Hello World.")
label.pack()

window.mainloop()


# 윈도우이름.geometry("너비x높이+x좌표+y좌표")를 이용하여 윈도우 창의 너비와 높이, 초기 화면 위치의
# x좌표와 y좌표를 설정할 수있습니다.

# 윈도우이름.resizeable(상하, 좌우)을 이용하여 윈도우 창의 창 크기 조절 가능 여부를 설정할 수 있습니다.
# True로 설정할 경우 윈도우 창의 크기를 조절할 수 있습니다.

# 위젯이름=tkinter.Label(윈도우창, text="내용")을 사용하여 윈도우 창에 Label 위젯을 설정할 수 있습니다.
# 위젯이름.pack()을 사용하여 위젯을 배치할 수 있습니다.