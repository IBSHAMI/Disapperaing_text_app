from tkinter import *
import time


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.config(bg="#231e23")
        self.wm_geometry("800x500")

        self.title_label = Label(text="Type like your life depends on it!!! \n Once you stop typing the timer will begin", bg="#231e23", font=("Colfax", 18, "italic"),
                              fg="#39a6a3")
        self.title_label.grid(row=0, column=1)

        self.timer = Text(self, height=2, width=10, highlightthickness=2.8,
                          highlightbackground="#00adb5")
        self.timer.grid(row=0, column=2, pady=10, padx=120)


if __name__ == "__main__":
    main = MainWindow()
    # # bind the main app window to any keypress event
    # main.bind("<KeyPress>", check)
    main.mainloop()
