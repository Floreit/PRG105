import tkinter

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label_1 = tkinter.Label(self.main_window, text='Hello Dave')
        self.label_2 = tkinter.Label(self.main_window, text='You are looking well')
        self.label_1.pack(side='left')
        self.label_2.pack(side='right')
        tkinter.mainloop()

my_gui = MyGui()


