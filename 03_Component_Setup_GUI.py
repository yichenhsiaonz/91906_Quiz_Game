# Copied tkinter template

from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self):
        print("Program started")

        # set up frame

        self.start_frame = Frame(padx=50, pady=5)
        self.start_frame.grid()

        # header text

        self.start_text = Label(self.start_frame, text="Start")
        self.start_text.grid(row=0)

        # frame for buttons

        self.setup_quit_button_frame = Frame(self.start_frame)
        self.setup_quit_button_frame.grid(row=1)

        # setup button

        self.setup_button = Button(self.setup_quit_button_frame, text="Setup", command=lambda: self.open_setup())
        self.setup_button.grid(row=1, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.setup_quit_button_frame, text="Quit", command=partial(root.destroy))
        self.quit_button.grid(row=1, column=1, padx=5)

    def open_setup(self):
        Setup(self)
        root.withdraw()


class Setup:
    def __init__(self, partner):
        print("Program setuped")

        #set toplevel

        self.setup_box = Toplevel()

        # set up closing behaviour

        self.setup_box.protocol('WM_DELETE_WINDOW', partial(root.destroy))

        # set up frame

        self.setup_frame = Frame(self.setup_box, padx=50, pady=5)
        self.setup_frame.grid()

        # header text

        self.setup_text = Label(self.setup_frame, text="Setup", font=("Arial", "16", "bold"))
        self.setup_text.grid(row=0, pady=5)

        # instruction text

        self.instructions_text = Label(self.setup_frame, text="PLease choose what you would like to practice and what\n"
                                                              "what information will be given",
                                       font=("Arial", "9"))
        self.instructions_text.grid(row=1, pady=5)

        # frame for answer options

        self.answer_frame = Frame(self.setup_frame)
        self.answer_frame.grid(row=2, pady=5)

        # Answer buttons

        # row 1

        self.atomic_number_button = Button(self.answer_frame, text="Atomic\nNumber", width=10, height=2)
        self.atomic_number_button.grid(row=0, column=0, padx=5, pady=5)

        self.mass_number_button = Button(self.answer_frame, text="Mass\nNumber", width=10, height=2)
        self.mass_number_button.grid(row=0, column=1, padx=5, pady=5)

        self.Name_button = Button(self.answer_frame, text="Name of\nElement", width=10, height=2)
        self.Name_button.grid(row=0, column=2, padx=5, pady=5)

        # row 2

        self.symbol_button = Button(self.answer_frame, text="Element\nSymbol", width=10, height=2)
        self.symbol_button.grid(row=2, column=0, padx=5, pady=5)

        self.group_button = Button(self.answer_frame, text="Group", width=10, height=2)
        self.group_button.grid(row=2, column=1, padx=5, pady=5)

        self.period_button = Button(self.answer_frame, text="Period", width=10, height=2)
        self.period_button.grid(row=2, column=2, padx=5, pady=5)

        # frame for buttons

        self.play_quit_button_frame = Frame(self.setup_frame)
        self.play_quit_button_frame.grid(row=4, pady=5)

        # play button

        self.play_button = Button(self.play_quit_button_frame, text="Play", command=lambda: self.open_play())
        self.play_button.grid(row=0, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.play_quit_button_frame, text="Quit", command=partial(root.destroy))
        self.quit_button.grid(row=0, column=1, padx=5)

    def open_play(self):
        Play(self)
        self.setup_box.withdraw()



class Play:
    def __init__(self, partner):
        print("Program played")

        # set toplevel

        self.play_box = Toplevel()

        # set up closing behaviour

        self.play_box.protocol('WM_DELETE_WINDOW', partial(root.destroy))

        # set up frame

        self.play_frame = Frame(self.play_box, padx=50, pady=5)
        self.play_frame.grid()

        # header text

        self.play_text = Label(self.play_frame, text="Play")
        self.play_text.grid(row=0)

        # frame for buttons

        self.help_stats_button_frame = Frame(self.play_frame)
        self.help_stats_button_frame.grid(row=1, pady=5)

        # help button

        self.help_button = Button(self.help_stats_button_frame, text="Help")
        self.help_button.grid(row=0, column=0, padx=5)

        # stats button

        self.stats_button = Button(self.help_stats_button_frame, text="Stats")
        self.stats_button.grid(row=0, column=1, padx=5)

        # quit button

        self.quit_button = Button(self.play_frame, text="Quit", command=partial(root.destroy))
        self.quit_button.grid(row=2)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Periodic Table Quiz")
    something = Start()
    root.mainloop()