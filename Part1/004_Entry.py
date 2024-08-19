# Reference: https://076923.github.io/posts/Python-tkinter-4/
# Entry을 이용하여 텍스트를 입력받거나 출력하기 위한 기입창을 생성할 수 있습니다

import tkinter
from math import *

window=tkinter.Tk()
window.title("James Yu")
window.geometry("640x480+100+100")
window.resizable(False, False)

def calc(event):
    label.config(text="The result is = "+str(eval(entry.get())))

entry=tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()

label=tkinter.Label(window)
label.pack()

window.mainloop()

# 매개변수를 사용하여 기입창의 속성을 설정합니다.
#
# Entry.bind()를 이용하여 key나 mouse 등의 event를 처리하여 메서드나 함수를 실행시킬 수 있습니다.
#
# 기입창에 간단한 수학함수 등을 작성 후 Enter 키를 입력시, 라벨에 결과가 표시됩니다.
#
# Tip : 4+4*cos(0.5)을 입력시 결과=7.51033...이 반환됩니다.