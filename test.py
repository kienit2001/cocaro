from tkinter import *
from main import run

def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()



root = Tk()

def main():

    de = False

    def clicked():
        print("asdasdasd")
        run(1)
    # root.attributes('-alpha', 0.0)
    # menubar = tkinter.Menu(root)
    # filemenu = tkinter.Menu(menubar, tearoff=0)
    # filemenu.add_command(label="Exit", command=root.destroy)
    # menubar.add_cascade(label="File", menu=filemenu)
    # root.config(menu=menubar)
    # frm = tkinter.Frame(root, bd=4, relief='raised')
    # frm.pack(fill='x')
    # lab = tkinter.Label(frm, text='Hello World!', bd=4, relief='sunken')
    # lab.pack(ipadx=4, padx=4, ipady=4, pady=4, fill='both')
    center(root)
    #root.attributes('-alpha', 1.0)
    redbutton = Button(root, text="Dễ", fg="red", command=clicked)
    # print(clicked())
    if de :
        return 1
    redbutton.place(x=70, y=50,width=70,height=20)
    greenbutton = Button(root, text="Trung bình", fg="black",command=clicked)
    greenbutton.place(x=70, y=100,width=70,height=20)
    bluebutton = Button(root, text="khó", fg="blue",command=clicked)
    bluebutton.place(x=70, y=150,width=70,height=20)
    # root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

    root.mainloop()

