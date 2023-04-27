from tkinter import *
class Gallery :
    def __init__(self, listbox, lbl_img, lbl_info):
        self.listbox = listbox
        self.lbl_img = lbl_img
        self.lbl_info = lbl_info
win = Tk()
win.title("나만의 사진첩")
win.geometry("1000x500+100+100")
img = PhotoImage(file = "basic.png")
img_lbl = Label(win, image = img)
info_lbl = Label(win, text = '보이냐?\n가운데\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', bg = 'black', fg = 'white', width = 50, height = 50)
guide_lbl = Label(win, text = '파일명과 메모를\n쉼표(,)로 구분지어 작성한 후\nsave 버튼을 클릭하세요', width = 50, height = 5, bg = 'yellow')
img_list = Listbox(win, height = 10)
text_box = Text(win, height = 50)
save_btn = Button(win, text = 'Save')
img_lbl.grid(row = 0, column = 0)
img_list.grid(row = 0, column = 1)
info_lbl.grid(row = 2, column = 0)
guide_lbl.grid(row = 1, column = 2)
text_box.grid(row = 2, column = 2)
save_btn.grid(row = 2, column = 3)
gallery = Gallery(img_list, img_lbl, info_lbl)
win.mainloop()