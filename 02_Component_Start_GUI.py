# functionality copied from GUI skeleton

from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self):
        print("Program started")

        # prevents resizing box

        root.resizable(False, False)

        # set up frame

        self.start_frame = Frame(padx=5, pady=5)
        self.start_frame.grid()

        # header text

        self.start_text = Label(self.start_frame, text="Periodic Table Quiz", font=("Arial", "16", "bold"))
        self.start_text.grid(row=0, pady=5)

        # instructions text

        self.instructions_text = Label(self.start_frame, text="Hello and welcome to my periodic table quiz game",
                                       font=("Arial", "9"))
        self.instructions_text.grid(row=1, pady=5)

        # frame for buttons

        self.setup_quit_button_frame = Frame(self.start_frame)
        self.setup_quit_button_frame.grid(row=2, pady=5)

        # setup button

        self.setup_button = Button(self.setup_quit_button_frame, text="Begin Setup",
                                    pady=10, padx=100,command=lambda: self.open_setup())
        self.setup_button.grid(row=0, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.setup_quit_button_frame, text="Quit",
                                  pady=10, padx=20, command=partial(root.destroy))
        self.quit_button.grid(row=0, column=1, padx=5)

    def open_setup(self):
        Setup(self)
        root.withdraw()


class Setup:
    def __init__(self, partner):
        print("Program setuped")

        #set toplevel

        self.setup_box = Toplevel()

        self.setup_box.resizable(False, False)

        # set up closing behaviour

        self.setup_box.protocol('WM_DELETE_WINDOW', partial(root.destroy))

        # set up frame

        self.setup_frame = Frame(self.setup_box, padx=50, pady=5)
        self.setup_frame.grid()

        # header text

        self.setup_text = Label(self.setup_frame, text="Setup")
        self.setup_text.grid(row=0)

        # frame for buttons

        self.play_quit_button_frame = Frame(self.setup_frame)
        self.play_quit_button_frame.grid(row=1)

        # play button

        self.play_button = Button(self.play_quit_button_frame, text="Play")
        self.play_button.grid(row=1, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.play_quit_button_frame, text="Quit", command=partial(root.destroy))
        self.quit_button.grid(row=1, column=1, padx=5)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Periodic Table Quiz")
    something = Start()
    root.mainloop()
