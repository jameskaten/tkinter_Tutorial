import tkinter

window=tkinter.Tk()
window.title("James Yu")
window.geometry("640x480+100+100")
window.resizable(False, False)

def flash():
    checkbutton1.flash()

CheckVariety_1=tkinter.IntVar()
CheckVariety_2=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(window, text="O", variable=CheckVariety_1, activebackground="blue")
checkbutton2=tkinter.Checkbutton(window, text="△", variable=CheckVariety_2)
checkbutton3=tkinter.Checkbutton(window, text="X", variable=CheckVariety_2, command=flash)

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

window.mainloop()

# tkinter.Checkbutton(윈도우 창, 매개변수1, 매개변수2, 매개변수3, ...)을 사용하여 해당 윈도우 창에 표시할 체크버튼의 속성을 설정할 수 있습니다.
#
# 매개변수를 사용하여 체크버튼의 속성을 설정합니다.
#
# 매개변수 중 command를 이용하여 사용자 정의 함수 : flash()을 실행시킬 수 있습니다.
