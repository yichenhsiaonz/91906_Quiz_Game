# Copied component 1

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

        # Stored variables

        self.answer_option = ""
        self.given_option = ""

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

        self.atomic_number_button = Button(self.answer_frame, text="Atomic\nNumber", width=10, height=2,
                                          command=lambda: self.update_numbers(self.atomic_number_button, "top"))
        self.atomic_number_button.grid(row=0, column=0, padx=5, pady=5)

        self.mass_number_button = Button(self.answer_frame, text="Mass\nNumber", width=10, height=2,
                                          command=lambda: self.update_numbers(self.mass_number_button, "top"))
        self.mass_number_button.grid(row=0, column=1, padx=5, pady=5)

        self.name_button = Button(self.answer_frame, text="Name of\nElement", width=10, height=2,
                                          command=lambda: self.update_numbers(self.name_button, "top"))
        self.name_button.grid(row=0, column=2, padx=5, pady=5)

        # row 2

        self.symbol_button = Button(self.answer_frame, text="Element\nSymbol", width=10, height=2,
                                          command=lambda: self.update_numbers(self.symbol_button, "top"))
        self.symbol_button.grid(row=1, column=0, padx=5, pady=5)

        self.group_button = Button(self.answer_frame, text="Group", width=10, height=2,
                                          command=lambda: self.update_numbers(self.group_button, "top"))
        self.group_button.grid(row=1, column=1, padx=5, pady=5)

        self.period_button = Button(self.answer_frame, text="Period", width=10, height=2,
                                          command=lambda: self.update_numbers(self.period_button, "top"))
        self.period_button.grid(row=1, column=2, padx=5, pady=5)

        # top buttons label

        self.top_label = Label(self.setup_frame, text="Please select what you would like to practice")
        self.top_label.grid(row=3, pady=5)

        # bottom buttons

        # frame for given options

        self.given_frame = Frame(self.setup_frame)
        self.given_frame.grid(row=4, pady=5)

        # Given buttons

        # row 1

        self.atomic_number_button_given = Button(self.given_frame, text="Atomic\nNumber", width=10, height=2,
                                          command=lambda: self.update_numbers(self.atomic_number_button_given, "bot"))
        self.atomic_number_button_given.grid(row=0, column=0, padx=5, pady=5)

        self.mass_number_button_given = Button(self.given_frame, text="Mass\nNumber", width=10, height=2,
                                          command=lambda: self.update_numbers(self.mass_number_button_given, "bot"))
        self.mass_number_button_given.grid(row=0, column=1, padx=5, pady=5)

        self.name_button_given = Button(self.given_frame, text="Name of\nElement", width=10, height=2,
                                          command=lambda: self.update_numbers(self.name_button_given, "bot"))
        self.name_button_given.grid(row=0, column=2, padx=5, pady=5)

        # row 2

        self.symbol_button_given = Button(self.given_frame, text="Element\nSymbol", width=10, height=2,
                                          command=lambda: self.update_numbers(self.symbol_button_given, "bot"))
        self.symbol_button_given.grid(row=1, column=1, padx=5, pady=5)

        # bottom buttons label

        self.bottom_label = Label(self.setup_frame, text="Please select what you would like to be given")
        self.bottom_label.grid(row=5, pady=5)

        # frame for buttons

        self.play_quit_button_frame = Frame(self.setup_frame)
        self.play_quit_button_frame.grid(row=6, pady=5)

        # play button

        self.play_button = Button(self.play_quit_button_frame, text="Play", command=lambda: self.open_play(),
                                  state=DISABLED)
        self.play_button.grid(row=0, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.play_quit_button_frame, text="Quit", command=partial(root.destroy))
        self.quit_button.grid(row=0, column=1, padx=5)

    def open_play(self):
        Play(self)
        self.setup_box.withdraw()

    # update_numbers enables all buttons in category and then disables selected button,
    # updates selected option variables

    def update_numbers(self, option, category):
        if category == "top":
            self.symbol_button.configure(state=NORMAL)
            self.atomic_number_button.configure(state=NORMAL)
            self.mass_number_button.configure(state=NORMAL)
            self.name_button.configure(state=NORMAL)
            self.group_button.configure(state=NORMAL)
            self.period_button.configure(state=NORMAL)
            self.answer_option = option.cget('text').replace("\n", " ")
        else:
            self.symbol_button_given.configure(state=NORMAL)
            self.atomic_number_button_given.configure(state=NORMAL)
            self.mass_number_button_given.configure(state=NORMAL)
            self.name_button_given.configure(state=NORMAL)
            self.given_option = option.cget('text').replace("\n", " ")
        if self.answer_option != "" and self.given_option != "":
            self.play_button.configure(state=NORMAL)

        option.config(state=DISABLED)


class Play:
    def __init__(self, partner):
        print("Program played")

        # set Toplevel

        self.play_box = Toplevel()

        # set up closing behaviour

        self.play_box.protocol('WM_DELETE_WINDOW', partial(root.destroy))

        # set up frame

        self.play_frame = Frame(self.play_box, padx=50, pady=5)
        self.play_frame.grid()

        # header text

        self.play_text = Label(self.play_frame, text="Play")
        self.play_text.grid(row=0)

        # body text

        self.play_text = Label(self.play_frame, text="{},{}".format(partner.answer_option, partner.given_option))
        self.play_text.grid(row=1)

        # frame for buttons

        self.help_stats_button_frame = Frame(self.play_frame)
        self.help_stats_button_frame.grid(row=2, pady=5)

        # help button

        self.help_button = Button(self.help_stats_button_frame, text="Help")
        self.help_button.grid(row=0, column=0, padx=5)

        # stats button

        self.stats_button = Button(self.help_stats_button_frame, text="Stats")
        self.stats_button.grid(row=0, column=1, padx=5)

        # quit button

        self.quit_button = Button(self.play_frame, text="Quit", command=partial(root.destroy))
        self.quit_button.grid(row=3)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Periodic Table Quiz")
    something = Start()
    root.mainloop()