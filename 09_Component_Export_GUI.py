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

        self.setup_text = Label(self.setup_frame, text="Setup")
        self.setup_text.grid(row=0)

        # frame for buttons

        self.play_quit_button_frame = Frame(self.setup_frame)
        self.play_quit_button_frame.grid(row=1)

        # play button

        self.play_button = Button(self.play_quit_button_frame, text="Play", command=lambda: self.open_play())
        self.play_button.grid(row=1, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.play_quit_button_frame, text="Quit", command=partial(root.destroy))
        self.quit_button.grid(row=1, column=1, padx=5)

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

        self.help_button = Button(self.help_stats_button_frame, text="Help", command=self.open_help)
        self.help_button.grid(row=0, column=0, padx=5)

        # stats button

        self.stats_button = Button(self.help_stats_button_frame, text="Stats", command=self.open_stats)
        self.stats_button.grid(row=0, column=1, padx=5)

        # quit button

        self.quit_button = Button(self.play_frame, text="Quit", command=partial(root.destroy))
        self.quit_button.grid(row=2)

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

        self.export_button = Button(self.export_quit_button_frame, text="Export", command=lambda: self.open_export())
        self.export_button.grid(row=1, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.export_quit_button_frame, text="Dismiss", command=partial(self.dismiss, partner))
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

        self.export_text = Label(self.export_frame, text="Export", font=("Arial", "16", "bold"))
        self.export_text.grid(row=0)

        # frame for buttons

        self.warning_quit_button_frame = Frame(self.export_frame)
        self.warning_quit_button_frame.grid(row=2)

        # warning button

        self.warning_button = Button(self.warning_quit_button_frame, text="Export",
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
