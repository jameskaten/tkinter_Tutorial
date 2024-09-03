# Reference: https://076923.github.io/posts/Python-tkinter-8/

import tkinter

window=tkinter.Tk()
window.title("James Yu")
window.geometry("640x480+100+100")
window.resizable(False, False)

def close():
    window.quit()
    window.destroy()

menubar=tkinter.Menu(window)

menu_1=tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="Lower menu 1-1")
menu_1.add_command(label="Lower menu 1-2")
menu_1.add_separator()
menu_1.add_command(label="Lower menu 1-3", command=close)
menubar.add_cascade(label="Upper menu 1", menu=menu_1)

menu_2=tkinter.Menu(menubar, tearoff=0, selectcolor="red")
menu_2.add_radiobutton(label="Lower menu 2-1", state="disable")
menu_2.add_radiobutton(label="Lower menu 2-2")
menu_2.add_radiobutton(label="Lower menu 2-3")
menubar.add_cascade(label="Upper menu 2", menu=menu_2)

menu_3=tkinter.Menu(menubar, tearoff=0)
menu_3.add_checkbutton(label="Lower menu 3-1")
menu_3.add_checkbutton(label="Lower manu 3-2")
menubar.add_cascade(label="Upper menu 3", menu=menu_3)

window.config(menu=menubar)

window.mainloop()

print("Window Close")

# 메뉴 이름=tkinter.Menu(윈도우 창)을 사용하여 해당 윈도우 창에 메뉴를 사용할 수 있습니다.
# 상위 메뉴 이름=tkinter.Menu(메뉴 이름, 매개변수1, 매개변수2, 매개변수3, ...)을 사용하여 해당 메뉴창에 표시할 상위 메뉴의 속성을 설정할 수 있습니다.
# 매개변수를 사용하여 상위 메뉴의 속성을 설정합니다.
# 상위 메뉴 이름.메서드(매개변수1, 매개변수2, 매개변수3, ...)를 사용하여 메서드에 해당하는 하위 메뉴를 추가할 수 있습니다.
# 매개변수를 사용하여 하위 메뉴의 속성을 설정합니다.
# 윈도우 창.config(menu=메뉴 이름)을 통하여 해당 윈도우 창에 메뉴를 등록할 수 있습니다.
# window.quit()는 위젯이 유지된 채 window.mainloop() 이후의 코드를 실행시킵니다.
# window.destroy()는 위젯을 파괴하고 window.mainloop() 이후의 코드를 실행시킵니다.

# add_command(매개변수)	    기본 메뉴 항목 생성
# add_radiobutton(매개변수)	라디오버튼 메뉴 항목 생성
# add_checkbutton(매개변수)	체크버튼 메뉴 항목 생성
# add_cascade(매개변수)	    상위 메뉴와 하위 메뉴 연결
# add_separator()	        구분선 생성
# add(유형, 매개변수)	        특정 유형의 메뉴 항목 생성
# delete(start_index, end_index)	start_index부터 end_index까지의 항목 삭제
# entryconfig(index, 매개변수)	    index 위치의 메뉴 항목 수정
# index(item)	            item 메뉴 항목의 index 위치 반환
# insert_separator (index)	index 위치에 구분선 생성
# invoke(index)	            index 위치의 항목 실행
# type(속성)	                선택 유형 반환 (command, radiobutton, checkbutton, cascade, separator, tearoff)
