# Copied component 1

from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random
import re


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
        self.answer_column = ""
        self.given_column = ""

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
                                          command=lambda: self.update_numbers(self.atomic_number_button, "top", 0))
        self.atomic_number_button.grid(row=0, column=0, padx=5, pady=5)

        self.mass_number_button = Button(self.answer_frame, text="Mass\nNumber", width=10, height=2,
                                          command=lambda: self.update_numbers(self.mass_number_button, "top", 6))
        self.mass_number_button.grid(row=0, column=1, padx=5, pady=5)

        self.name_button = Button(self.answer_frame, text="Name of\nElement", width=10, height=2,
                                          command=lambda: self.update_numbers(self.name_button, "top", 1))
        self.name_button.grid(row=0, column=2, padx=5, pady=5)

        # row 2

        self.symbol_button = Button(self.answer_frame, text="Element\nSymbol", width=10, height=2,
                                          command=lambda: self.update_numbers(self.symbol_button, "top", 2))
        self.symbol_button.grid(row=1, column=0, padx=5, pady=5)

        self.group_button = Button(self.answer_frame, text="Group", width=10, height=2,
                                          command=lambda: self.update_numbers(self.group_button, "top", 3))
        self.group_button.grid(row=1, column=1, padx=5, pady=5)

        self.period_button = Button(self.answer_frame, text="Period", width=10, height=2,
                                          command=lambda: self.update_numbers(self.period_button, "top", 4))
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
                                               command=lambda: self.update_numbers(self.atomic_number_button_given,
                                                                                   "bot", 0))
        self.atomic_number_button_given.grid(row=0, column=0, padx=5, pady=5)

        self.mass_number_button_given = Button(self.given_frame, text="Mass\nNumber", width=10, height=2,
                                               command=lambda: self.update_numbers(self.mass_number_button_given,
                                                                                   "bot", 6))
        self.mass_number_button_given.grid(row=0, column=1, padx=5, pady=5)

        self.name_button_given = Button(self.given_frame, text="Name of\nElement", width=10, height=2,
                                        command=lambda: self.update_numbers(self.name_button_given,
                                                                            "bot", 1))
        self.name_button_given.grid(row=0, column=2, padx=5, pady=5)

        # row 2

        self.symbol_button_given = Button(self.given_frame, text="Element\nSymbol", width=10, height=2,
                                          command=lambda: self.update_numbers(self.symbol_button_given,
                                                                              "bot", 2))
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

    def update_numbers(self, option, category, category_column):
        if category == "top":
            self.symbol_button.configure(state=NORMAL)
            self.atomic_number_button.configure(state=NORMAL)
            self.mass_number_button.configure(state=NORMAL)
            self.name_button.configure(state=NORMAL)
            self.group_button.configure(state=NORMAL)
            self.period_button.configure(state=NORMAL)
            self.answer_option = option.cget('text').replace("\n", " ")
            self.answer_column = category_column
        else:
            self.symbol_button_given.configure(state=NORMAL)
            self.atomic_number_button_given.configure(state=NORMAL)
            self.mass_number_button_given.configure(state=NORMAL)
            self.name_button_given.configure(state=NORMAL)
            self.given_option = option.cget('text').replace("\n", " ")
            self.given_column = category_column
        if self.answer_option != "" and self.given_option != "":
            self.play_button.configure(state=NORMAL)

        option.config(state=DISABLED)


class Play:
    def __init__(self, partner):
        print("Program played")

        # set up element list

        with open('elements.csv', newline='') as f:
            reader = csv.reader(f)
            self.element_data = list(reader)

        # set number of rounds and score to zero

        self.rounds = 0
        self.score = 0

        # set toplevel

        self.play_box = Toplevel()

        # set up closing behaviour

        self.play_box.protocol('WM_DELETE_WINDOW', partial(root.destroy))

        # set up frame

        self.play_frame = Frame(self.play_box, padx=5, pady=5)
        self.play_frame.grid()

        # header text

        self.play_text = Label(self.play_frame, text="Periodic Table Quiz", font=("Arial", "16", "bold"))
        self.play_text.grid(row=0)

        # Rounds played / points

        self.point_rounds_text = Label(self.play_frame, text="Rounds played: 0 / 10\n"
                                                            "Points: 0")
        self.point_rounds_text.grid(row=1)

        # Instructions / question

        self.instruction_text = Label(self.play_frame, text="Select the correct answer to the question below...\n\n"
                                                     "The {} of the element with the {} below "
                                                     "is:".format(partner.answer_option.lower(),
                                                                  partner.given_option.lower()))
        self.instruction_text.grid(row=2)

        # Given thing

        self.play_text_given = Label(self.play_frame, font=("Arial", "14"))
        self.play_text_given.grid(row=3)

        # Option frame

        self.option_frame = Frame(self.play_frame)
        self.option_frame.grid(row=4, pady=5)

        # top row

        self.option_1 = Button(self.option_frame, text="1", height=2, width=20,
                               command=lambda: self.answer_chosen(self.option_1, partner))
        self.option_1.grid(row=0, column=0, padx=5, pady=5)

        self.option_2 = Button(self.option_frame, text="2", height=2, width=20,
                               command=lambda: self.answer_chosen(self.option_2, partner))
        self.option_2.grid(row=0, column=1, padx=5, pady=5)

        # bottom row

        self.option_3 = Button(self.option_frame, text="3", height=2, width=20,
                               command=lambda: self.answer_chosen(self.option_3, partner))
        self.option_3.grid(row=1, column=0, padx=5, pady=5)

        self.option_4 = Button(self.option_frame, text="4", height=2, width=20,
                               command=lambda: self.answer_chosen(self.option_4, partner))
        self.option_4.grid(row=1, column=1, padx=5, pady=5)

        self.update_option(partner)

        # Next button

        self.next_button = Button(self.play_frame, text="Next", height=2, width=43,
                                  command=lambda: self.next_pressed(partner))

        # frame for help / export buttons

        self.help_stats_button_frame = Frame(self.play_frame)
        self.help_stats_button_frame.grid(row=6, pady=5)

        # help button

        self.help_button = Button(self.help_stats_button_frame, text="Help", command=self.open_help,
                                  height=2, width=20)
        self.help_button.grid(row=0, column=0, padx=5)

        # stats button

        self.stats_button = Button(self.help_stats_button_frame, text="Stats", command=self.open_stats,
                                   height=2, width=20)
        self.stats_button.grid(row=0, column=1, padx=5)

        # quit button

        self.quit_button = Button(self.play_frame, text="Quit", height=2, width=43, command=partial(root.destroy))
        self.quit_button.grid(row=7)

    def update_option(self, partner):

        # picks 4 random rows from list of csv

        random_options = random.sample(self.element_data, 4)

        # selects 1 of 4 rows to be correct

        self.correct_row = random.choice(random_options)

        # sets given info to that of correct element

        self.play_text_given.configure(text="{}: {}".format(partner.given_option,
                                                            self.correct_row[partner.given_column]))

        # configures text on buttons

        self.option_1.configure(text=random_options[0][partner.answer_column])
        self.option_2.configure(text=random_options[1][partner.answer_column])
        self.option_3.configure(text=random_options[2][partner.answer_column])
        self.option_4.configure(text=random_options[3][partner.answer_column])

        # figures out which button has correct information on it

        self.option_list = ([self.option_1, self.option_2, self.option_3, self.option_4])
        for x in self.option_list:
            if x.cget("text") == self.correct_row[partner.answer_column]:
                self.correct_option = x

    def answer_chosen(self,chosen, partner):

        # checks if text on button matches that of the correct button

        if str(self.correct_row[partner.answer_column]) == chosen.cget("text"):
            chosen.configure(bg="pale green")

            # increases score count if correct

            self.score += 1
        else:
            chosen.configure(bg="pink")
            self.correct_option.configure(bg="pale green")

        # increases round count

        self.rounds += 1

        self.point_rounds_text.configure(text="Rounds played: {} / 10\nPoints: {}".format(self.rounds, self.score))

        # disables all option buttons

        self.option_1.configure(state=DISABLED)
        self.option_2.configure(state=DISABLED)
        self.option_3.configure(state=DISABLED)
        self.option_4.configure(state=DISABLED)

        if self.rounds != 10:

            # shows next button

            self.next_button.grid(row=5)

    def next_pressed(self, partner):

        # resets buttons, hides next button, chooses new options

        self.option_1.configure(bg="white smoke", state=NORMAL)
        self.option_2.configure(bg="white smoke", state=NORMAL)
        self.option_3.configure(bg="white smoke", state=NORMAL)
        self.option_4.configure(bg="white smoke", state=NORMAL)
        self.next_button.grid_forget()
        self.update_option(partner)

    def open_help(self):
        self.help_button.configure(state=DISABLED)
        Help(self)

    def open_stats(self):
        self.stats_button.configure(state=DISABLED)
        Stats(self)


class Help:
    def __init__(self, partner):
        print("Program helped")

        # set Toplevel

        self.help_box = Toplevel()

        # set up closing behaviour

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.dismiss, partner))

        # set up frame

        self.help_frame = Frame(self.help_box, padx=50, pady=5)
        self.help_frame.grid()

        # header text

        self.help_text = Label(self.help_frame, text="Help")
        self.help_text.grid(row=0)

        # dismiss button

        self.quit_button = Button(self.help_frame, text="Dismiss", command=partial(self.dismiss, partner))
        self.quit_button.grid(row=1, padx=5)

    def dismiss(self, partner):
        partner.help_button.configure(state=NORMAL)
        self.help_box.destroy()


class Stats:
    def __init__(self, partner):
        print("Program statsed")

        # set Toplevel

        self.stats_box = Toplevel()

        # set up closing behaviour

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.dismiss, partner))

        # set up frame

        self.stats_frame = Frame(self.stats_box, padx=50, pady=5)
        self.stats_frame.grid()

        # header text

        self.stats_text = Label(self.stats_frame, text="Stats")
        self.stats_text.grid(row=0)

        # frame for buttons

        self.export_quit_button_frame = Frame(self.stats_frame)
        self.export_quit_button_frame.grid(row=1)

        # export button

        self.export_button = Button(self.export_quit_button_frame, text="Export",
                                    command=lambda: self.open_export())
        self.export_button.grid(row=1, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.export_quit_button_frame, text="Dismiss",
                                  command=partial(self.dismiss, partner))
        self.quit_button.grid(row=1, column=1, padx=5)

    def open_export(self):
        self.export_button.configure(state=DISABLED)
        Export(self)

    def dismiss(self, partner):
        partner.stats_button.configure(state=NORMAL)
        self.stats_box.destroy()


class Export:
    def __init__(self, partner):
        print("Program exported")

        # set Toplevel

        self.export_box = Toplevel()

        # set up closing behaviour

        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.dismiss, partner))

        # set up frame

        self.export_frame = Frame(self.export_box, padx=50, pady=5)
        self.export_frame.grid()

        # header text

        self.export_text = Label(self.export_frame, text="Export")
        self.export_text.grid(row=0)

        # frame for buttons

        self.warning_quit_button_frame = Frame(self.export_frame)
        self.warning_quit_button_frame.grid(row=1)

        # warning button

        self.warning_button = Button(self.warning_quit_button_frame, text="Warning",
                                     command=lambda: self.open_warning())
        self.warning_button.grid(row=1, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.warning_quit_button_frame, text="Dismiss",
                                  command=partial(self.dismiss, partner))
        self.quit_button.grid(row=1, column=1, padx=5)

    def open_warning(self):
        self.warning_button.configure(state=DISABLED)
        Warning(self)

    def dismiss(self, partner):
        partner.export_button.configure(state=NORMAL)
        self.export_box.destroy()


class Warning:
    def __init__(self, partner):
        print("Program warninged")

        # set Toplevel

        self.warning_box = Toplevel()

        # set up closing behaviour

        self.warning_box.protocol('WM_DELETE_WINDOW', partial(self.dismiss, partner))

        # set up frame

        self.warning_frame = Frame(self.warning_box, padx=50, pady=5)
        self.warning_frame.grid()

        # header text

        self.warning_text = Label(self.warning_frame, text="Warning")
        self.warning_text.grid(row=0)

        # dismiss button

        self.quit_button = Button(self.warning_frame, text="Dismiss", command=partial(self.dismiss, partner))
        self.quit_button.grid(row=1, padx=5)

    def dismiss(self, partner):
        partner.warning_button.configure(state=NORMAL)
        self.warning_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Periodic Table Quiz")
    something = Start()
    root.mainloop()