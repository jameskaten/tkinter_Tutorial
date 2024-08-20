# Reference: https://076923.github.io/posts/Python-tkinter-5/#google_vignette

# Listbox

import tkinter

window=tkinter.Tk()
window.title("James Yu")
window.geometry("640x480+100+100")
window.resizable(False, False)

listbox = tkinter.Listbox(window, selectmode='extended', height=0)
listbox.insert(0, "#1")
listbox.insert(1, "#2")
listbox.insert(2, "#2")
listbox.insert(3, "#2")
listbox.insert(4, "#3")
listbox.delete(1, 2)
listbox.pack()

window.mainloop()

# tkinter.Listbox(윈도우 창, 매개변수1, 매개변수2, 매개변수3, ...)을 사용하여
# 해당 윈도우 창에 표시할 리스트박스의 속성을 설정할 수 있습니다.
#
# 매개변수를 사용하여 리스트박스의 속성을 설정합니다.
#
# 리스트박스.insert(index, "항목")을 통하여 항목을 추가할 수 있습니다.

# 리스트박스.delete(start_index, end_index)를 통하여 항목을 삭제할 수 있습니다.
#
# Tip : 리스트박스.delete(index)를 통하여 단일 항목만 삭제할 수 있습니다.