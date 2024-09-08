# Reference: https://076923.github.io/posts/Python-tkinter-9/

import tkinter

window=tkinter.Tk()
window.title("James Yu")
window.geometry("640x480+100+100")
window.resizable(False, False)

menubutton=tkinter.Menubutton(window,text="Menu Button", relief="raised", direction="right")
menubutton.pack()

menu=tkinter.Menu(menubutton, tearoff=0)
menu.add_command(label="Lower menu-1")
menu.add_separator()
menu.add_command(label="Lower menu-2")
menu.add_command(label="Lower menu-3")


menubutton["menu"]=menu

window.mainloop()

# Menubutton을 이용하여 메뉴기능을 가진 단추를 생성

# tkinter.Menubutton(윈도우 창, 매개변수1, 매개변수2, 매개변수3, ...)을 사용하여
# 해당 윈도우 창에 표시할 메뉴 버튼의 속성을 설정

# 매개변수를 사용하여 메뉴 버튼의 속성을 설정합니다.
#
# 이 후, tkinter.Menu(메뉴 버튼 이름, 매개변수1, 매개변수2, 매개변수3, ...)을 사용하여 메뉴의 속성을 설정할 수 있습니다.
#
# 마지막으로 메뉴 버튼의 매개변수 중 menu를 마지막에 사용하여 메뉴 버튼과 메뉴를 연결