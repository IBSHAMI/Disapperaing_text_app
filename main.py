from tkinter import *
import time


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.config(bg="#e3fdfd")
        self.wm_geometry("800x500")
        
        self.title_label = Label(text="Type like your life depends on it!!!")
        self.title_label.grid(row=1 ,column=2)

        self.timer = Text(self, height=1, width=20, highlightthickness=2.8,
                          highlightbackground="#00adb5")
        self.timer.grid(row=0, column=0, pady=10)


if __name__ == "__main__":
    main = MainWindow()
    # # bind the main app window to any keypress event
    # main.bind("<KeyPress>", check)
    main.mainloop()
