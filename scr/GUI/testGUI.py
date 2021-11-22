from tkinter import *
from tkinter import ttk



class mainApp (ttk.Frame):

    def __init__(self, parent, images, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.images = images
        btn = [[0 for x in range(50)] for x in range(50)]
        for y in range(50):
            for x in range(50):
                btn[x][y] = ttk.Button(self.parent, width=2)
                btn[x][y].grid(column=x, row=y)

    # root = Tk()
    # frm = ttk.Frame(root, padding=10)
    # frm.grid()
    # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    # root.mainloop()