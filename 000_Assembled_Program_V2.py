# V2 consists of small tweaks to usability

from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random
import re
from os import path


def regex_check(file_name):
    if re.search("[.<>:\"/|?*\\\\\040]", file_name):
        return "Invalid file name - illegal character(s)(. < > : \" / \\ | ? * )"
    if file_name == "":
        return "Invalid file name - can't be blank"
    return "No Error"


def get_score(y):
    print(y)
    return y[1]


class Start:
    def __init__(self):
        print("Program started")

        # prevents resizing box

        root.resizable(False, False)

        # set up frame

        self.start_frame = Frame(padx=5, pady=5)
        self.start_frame.grid()

        # header text

        self.start_text = Label(self.start_frame, text="Periodic Table Quiz", font=("Arial", "16", "bold"),
                                justify=LEFT, anchor="w")
        self.start_text.grid(row=0, pady=5, sticky=W)

        # instructions text

        self.instructions_text = Label(self.start_frame, justify=LEFT,
                                       text="Hello and welcome to my periodic table quiz game. \n"
                                            "In this game, you will be tested on your knowledge of \n"
                                            "specific elements in the periodic table. \n"
                                            "You will select two aspects of elements. You must \n"
                                            "identify one based on the other.",
                                       font=("Arial", "9"), anchor="w")
        self.instructions_text.grid(row=1, pady=5, sticky=W)

        # frame for buttons

        self.setup_quit_button_frame = Frame(self.start_frame)
        self.setup_quit_button_frame.grid(row=2, pady=5)

        # setup button

        self.setup_button = Button(self.setup_quit_button_frame, text="Begin Setup",
                                   pady=10, padx=100, command=lambda: self.open_setup())
        self.setup_button.grid(row=0, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.setup_quit_button_frame, text="Quit",
                                  pady=10, padx=20, command=partial(root.destroy))
        self.quit_button.grid(row=0, column=1, padx=5)

    def open_setup(self):
        Setup()
        root.withdraw()


class Setup:
    def __init__(self):
        print("Program setuped")

        # set toplevel

        self.setup_box = Toplevel()

        # prevents resizing box

        self.setup_box.resizable(False, False)

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

        self.instructions_text = Label(self.setup_frame, justify=LEFT,
                                       text="Please select the information about an element you \n"
                                            "will be given and please select the information you \n"
                                            "must deduce from what is given.",
                                       font=("Arial", "9"))
        self.instructions_text.grid(row=1, pady=5)

        # top buttons label

        self.top_label = Label(self.setup_frame, text="Please select what you would like to practice")
        self.top_label.grid(row=2, pady=5)

        # frame for answer options

        self.answer_frame = Frame(self.setup_frame)
        self.answer_frame.grid(row=3, pady=5)

        # Answer buttons

        # dummy object for functions with blank values to stop errors

        self.dummy = Button()
        self.keep_disabled = self.dummy
        self.keep_disabled_given = self.dummy

        # row 1

        self.atomic_number_button = Button(self.answer_frame, text="Atomic\nNumber", width=10, height=2,
                                           command=lambda: self.update_numbers(self.atomic_number_button, "top", 0,
                                                                               self.atomic_number_button_given))
        self.atomic_number_button.grid(row=0, column=0, padx=5, pady=5)

        self.mass_number_button = Button(self.answer_frame, text="Mass\nNumber", width=10, height=2,
                                         command=lambda: self.update_numbers(self.mass_number_button, "top", 6,
                                                                             self.mass_number_button_given))
        self.mass_number_button.grid(row=0, column=1, padx=5, pady=5)

        self.name_button = Button(self.answer_frame, text="Name of\nElement", width=10, height=2,
                                  command=lambda: self.update_numbers(self.name_button, "top", 1,
                                                                      self.name_button_given))
        self.name_button.grid(row=0, column=2, padx=5, pady=5)

        # row 2

        self.group_button = Button(self.answer_frame, text="Group", width=10, height=2,
                                   command=lambda: self.update_numbers(self.group_button, "top", 3, self.dummy))
        self.group_button.grid(row=1, column=0, padx=5, pady=5)

        self.symbol_button = Button(self.answer_frame, text="Element\nSymbol", width=10, height=2,
                                    command=lambda: self.update_numbers(self.symbol_button, "top", 2,
                                                                        self.symbol_button_given))
        self.symbol_button.grid(row=1, column=1, padx=5, pady=5)

        self.period_button = Button(self.answer_frame, text="Period", width=10, height=2,
                                    command=lambda: self.update_numbers(self.period_button, "top", 4, self.dummy))
        self.period_button.grid(row=1, column=2, padx=5, pady=5)

        self.top_button_list = [self.atomic_number_button, self.mass_number_button, self.name_button,
                                self.symbol_button, self.group_button, self.period_button]

        # bottom buttons

        # bottom buttons label

        self.bottom_label = Label(self.setup_frame, text="Please select what you would like to be given")
        self.bottom_label.grid(row=4, pady=5)

        # frame for given options

        self.given_frame = Frame(self.setup_frame)
        self.given_frame.grid(row=5, pady=5)

        # Given buttons

        # row 1

        self.atomic_number_button_given = Button(self.given_frame, text="Atomic\nNumber", width=10, height=2,
                                                 command=lambda: self.update_numbers(self.atomic_number_button_given,
                                                                                   "bot", 0, self.atomic_number_button))
        self.atomic_number_button_given.grid(row=0, column=0, padx=5, pady=5)

        self.mass_number_button_given = Button(self.given_frame, text="Mass\nNumber", width=10, height=2,
                                               command=lambda: self.update_numbers(self.mass_number_button_given,
                                                                                   "bot", 6, self.mass_number_button))
        self.mass_number_button_given.grid(row=0, column=1, padx=5, pady=5)

        self.name_button_given = Button(self.given_frame, text="Name of\nElement", width=10, height=2,
                                        command=lambda: self.update_numbers(self.name_button_given,
                                                                            "bot", 1, self.name_button))
        self.name_button_given.grid(row=0, column=2, padx=5, pady=5)

        # row 2

        self.symbol_button_given = Button(self.given_frame, text="Element\nSymbol", width=10, height=2,
                                          command=lambda: self.update_numbers(self.symbol_button_given,
                                                                              "bot", 2, self.symbol_button))
        self.symbol_button_given.grid(row=1, column=1, padx=5, pady=5)

        self.bottom_button_list = [self.atomic_number_button_given, self.mass_number_button_given,
                                   self.name_button_given, self.symbol_button_given]

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

    def update_numbers(self, option, category, category_column, counterpart):

        #  when option clicked, check if it was a top row button or bottom row button

        if category == "top":

            # reset all top buttons except for counterpart to bottom row option selected

            for x in self.top_button_list:
                if x != self.keep_disabled:
                    x.configure(state=NORMAL, bg="white smoke")

            # resets old counterpart

            self.keep_disabled_given.configure(state=NORMAL, bg="white smoke")

            # get text value on button selected

            self.answer_option = option.cget('text').replace("\n", " ")

            # save button id for later use

            self.answer_column = category_column

            # stores counterpart to keep disabled

            self.keep_disabled_given = counterpart
        else:

            # same as top row but for bottom row

            for x in self.bottom_button_list:
                if x != self.keep_disabled_given:
                    x.configure(state=NORMAL, bg="white smoke")

            self.keep_disabled.configure(state=NORMAL, bg="white smoke")

            self.given_option = option.cget('text').replace("\n", " ")

            self.given_column = category_column

            self.keep_disabled = counterpart

        # enable play button if two options selected

        if self.answer_option != "" and self.given_option != "":
            self.play_button.configure(state=NORMAL)

        # disables option selected and counterpart and changes their colors

        counterpart.configure(state=DISABLED, bg="pink")
        option.config(state=DISABLED, bg="pale green")


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
        self.answer_column = partner.answer_column
        self.given_column = partner.given_column

        # set toplevel

        self.play_box = Toplevel()

        # prevents resizing box

        self.play_box.resizable(False, False)

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

        # Instructions / question

        self.save_text = Label(self.play_frame, text="To save your score to the leaderboard, export the\n"
                                                     "leaderboard in the stats menu")
        self.save_text.grid(row=6)

        # frame for help / export buttons

        self.help_stats_button_frame = Frame(self.play_frame)
        self.help_stats_button_frame.grid(row=7, pady=5)

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
        self.quit_button.grid(row=8)

    def update_option(self, partner):

        # uses loop to prevent repetition

        check_loop = ""
        while check_loop == "":

            # picks 4 random rows from list of csv

            random_options = random.sample(self.element_data, 4)
            check_list = []
            for x in random_options:
                check_list.append(x[partner.answer_column])
                print(check_list)
            check_dict = dict.fromkeys(check_list)
            if len(check_dict) == 4:
                check_loop = 1

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

    def answer_chosen(self, chosen, partner):

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

        # prevents resizing box

        self.help_box.resizable(False, False)

        # set up closing behaviour

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.dismiss, partner))

        # set up frame

        self.help_frame = Frame(self.help_box, pady=5)
        self.help_frame.grid()

        # header text

        self.help_text = Label(self.help_frame, text="Help / Instructions", font=("Arial", "16", "bold"),
                               justify=LEFT, anchor="w")
        self.help_text.grid(row=0, sticky=W)

        # header text

        self.instruction_text = Label(self.help_frame, justify=LEFT, width=40,
                                      text="This is a game in which you are tested on your \n"
                                           "knowledge about the periodic table. \n\n"
                                           "You are provided with information about a specific \n"
                                           "element and from this, you must deduce which of \n"
                                           "the four answers provided is correct.\n",
                                      anchor="w")
        self.instruction_text.grid(row=1, sticky=W)

        # dismiss button

        self.quit_button = Button(self.help_frame, text="Dismiss", command=partial(self.dismiss, partner),
                                  width=40, height=2)
        self.quit_button.grid(row=2, padx=5)

    def dismiss(self, partner):
        partner.help_button.configure(state=NORMAL)
        self.help_box.destroy()


class Stats:
    def __init__(self, partner):
        print("Program statsed")

        # set score

        self.score = partner.score

        # set Toplevel

        self.stats_box = Toplevel()

        # prevents resizing box

        self.stats_box.resizable(False, False)

        # set up closing behaviour

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.dismiss, partner))

        # set up frame

        self.stats_frame = Frame(self.stats_box, padx=5, pady=5)
        self.stats_frame.grid()

        # header text

        self.stats_heading = Label(self.stats_frame, text="Stats", font=("Arial", "16", "bold"), anchor="w")
        self.stats_heading.grid(row=0, sticky=W)

        # space for text

        self.leaderboard_file = "Leaderboards/{}_{}_leaderboard.csv".format(partner.given_column, partner.answer_column)

        csv_file = open(self.leaderboard_file, "a",
                        newline='')
        csv_file.close()

        csv_file = open(self.leaderboard_file, "r")
        self.leaderboard_list = []
        written = 0

        # copies scores from csv to list

        for x in csv.reader(csv_file):

            # checks to see if player score is higher than score being written to insert it in right place

            if int(x[1]) < self.score and written == 0:
                self.leaderboard_list.append("*")
                self.leaderboard_list.append([x[0], int(x[1])])
                written = 1

            # if already written player score or not the right place, writes score from csv

            else:
                self.leaderboard_list.append([x[0], int(x[1])])

        # inserts score to bottom of list if player score is not higher than any scores in csv

        if written == 0:
            self.leaderboard_list.append("*")

        csv_file.close()

        self.leaderboard_text = ""

        # writes out list as text while checking for placeholder

        for x in self.leaderboard_list:

            # replaces placeholder with actual score in leaderboard

            if x == "*":
                self.leaderboard_text += "**** You: {} ****\n".format(self.score)

            # writes everything else

            else:
                self.leaderboard_text += "{}: {}\n".format(x[0], int(x[1]))

        self.stats_text = Label(self.stats_frame, text="Points: {}\n"
                                                       "Questions answered correctly: {}\n"
                                                       "Questions answered incorrectly: {}\n"
                                                       "Total rounds played: {}\n"
                                                       "\n"
                                                       "Leaderboard:\n"
                                                       "{}".format(self.score, self.score,
                                                                   partner.rounds - self.score,
                                                                   partner.rounds, self.leaderboard_text),
                                justify=LEFT)
        self.stats_text.grid(row=1)

        # frame for buttons

        self.export_quit_button_frame = Frame(self.stats_frame)
        self.export_quit_button_frame.grid(row=2)

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

        # get leaderboard filename

        self.leaderboard_file = partner.leaderboard_file

        # set Toplevel

        self.export_box = Toplevel()

        # prevents resizing box

        self.export_box.resizable(False, False)

        # set up closing behaviour

        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.dismiss, partner))

        # set up frame

        self.export_frame = Frame(self.export_box, pady=5)
        self.export_frame.grid()

        # header text

        self.export_text = Label(self.export_frame, text="Export", font=("Arial", "16", "bold"),
                                 anchor="w", justify=LEFT)
        self.export_text.grid(row=0, sticky=W)

        # response label

        self.response_text = Label(self.export_frame, justify=LEFT, anchor="w",
                                   text="The leaderboard for the current combination\n"
                                        "of questions / answers will be exported to a\n"
                                        "text file in the same folder as the game.\n\n"
                                        "Your score will also be saved")
        self.response_text.grid(row=1, sticky=W)

        # frame for file name / export button

        self.entry_export_button_frame = Frame(self.export_frame)
        self.entry_export_button_frame.grid(row=2)

        # User name label

        self.user_name_text = Label(self.entry_export_button_frame, anchor="w", text="Enter user name here")
        self.user_name_text.grid(row=0, column=0, sticky=W)

        # User name

        self.user_name_entry = Entry(self.entry_export_button_frame, width=20,
                                     font=("Arial", 14, "bold"))
        self.user_name_entry.grid(row=1, column=0)

        # File name label

        self.file_name_text = Label(self.entry_export_button_frame, anchor="w", text="Enter file name here")
        self.file_name_text.grid(row=2, column=0, sticky=W)

        # file_name

        self.file_name_entry = Entry(self.entry_export_button_frame, width=20,
                                     font=("Arial", 14, "bold"))
        self.file_name_entry.grid(row=3, column=0)

        # warning button

        self.export_button = Button(self.entry_export_button_frame, text="Export",
                                    command=partial(self.export, partner))
        self.export_button.grid(row=3, column=1)

        # response label

        self.response_text = Label(self.export_frame, text="")
        self.response_text.grid(row=3)

        # dismiss button

        self.dismiss_button = Button(self.export_frame, text="Dismiss",
                                     command=partial(self.dismiss, partner))
        self.dismiss_button.grid(row=4, ipadx=110, ipady=10, padx=5)

    def export(self, partner):

        # gets strings from inputs

        self.file = self.file_name_entry.get()
        self.user = self.user_name_entry.get()

        # gets list of scores from leaderboard

        self.leaderboard_list = partner.leaderboard_list

        # replaces placeholder player score with real score and username

        for x in range(len(self.leaderboard_list)):
            if self.leaderboard_list[x] == "*":
                self.current_score = [self.user, partner.score]
                self.leaderboard_list[x] = self.current_score

        # sorts list by score descending

        self.leaderboard_list.sort(key=get_score, reverse=True)

        # checks for illegal characters in filename

        self.response_text.config(text=(regex_check(self.file)))

        if regex_check(self.file) == "No Error":

            # warns about existing file

            if path.isfile("{}.txt".format(self.file)):
                OverwriteWarning(self)

            # if no exisiting file, create text file

            else:

                txt_file = open("{}.txt".format(self.file), "a")

                csv_file = open(self.leaderboard_file, "w", newline='')
                csv_writer = csv.writer(csv_file)
                # writes scores to file

                for x in self.leaderboard_list:
                    csv_writer.writerow(x)
                    txt_file.write("{}: {}\n".format(x[0], x[1]))

                txt_file.close()
                csv_file.close()

                self.response_text.configure(text="Exported!")

    def dismiss(self, partner):
        partner.export_button.configure(state=NORMAL)
        self.export_box.destroy()


class OverwriteWarning:
    def __init__(self, partner):
        print("Program warninged")

        # get leaderboard filename

        self.leaderboard_file = partner.leaderboard_file

        # set Toplevel

        self.warning_box = Toplevel()

        # prevents resizing box

        self.warning_box.resizable(False, False)

        # set up closing behaviour

        self.warning_box.protocol('WM_DELETE_WINDOW', partial(self.dismiss, partner))

        # set up frame

        self.warning_frame = Frame(self.warning_box, padx=50, pady=5)
        self.warning_frame.grid()

        # header text

        self.warning_heading = Label(self.warning_frame, text="Overwrite Warning")
        self.warning_heading.grid(row=0)

        # main text

        self.warning_text = Label(self.warning_frame, text="The file '{}.txt' already exists."
                                                           " Would you like to overwrite it?".format(partner.file))
        self.warning_text.grid(row=1)

        # Yes / No button frame

        self.yes_no_frame = Frame(self.warning_frame)
        self.yes_no_frame.grid(row=2)

        # yes button

        self.yes_button = Button(self.yes_no_frame, text="Yes", command=partial(self.export, partner))
        self.yes_button.grid(column=0, row=0, padx=5)

        # no button

        self.no_button = Button(self.yes_no_frame, text="No", command=partial(self.dismiss, partner))
        self.no_button.grid(column=1, row=0, padx=5)

    def export(self, partner):
        txt_file = open("{}.txt".format(partner.file), "w")

        csv_file = open(self.leaderboard_file, "w", newline='')
        csv_writer = csv.writer(csv_file)
        # writes scores to file

        for x in partner.leaderboard_list:
            csv_writer.writerow(x)
            txt_file.write("{}: {}\n".format(x[0], x[1]))

        partner.response_text.configure(text="Exported!")

        txt_file.close()
        csv_file.close()

        self.dismiss(partner)

    def dismiss(self, partner):
        partner.export_button.configure(state=NORMAL)
        self.warning_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Periodic Table Quiz")
    something = Start()
    root.mainloop()