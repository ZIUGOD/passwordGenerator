from tkinter import *
from random import choice
from os import name, system

# variables
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
specials = "!@#$%&*-_=+"
specials2 = ")(][}{~^´`}|\/"


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def generatePassword():
    values = ""
    label_password["text"] = ""

    if number_check_var.get():
        values += numbers

    if lower_check_var.get():
        values += lower_case

    if upper_check_var.get():
        values += upper_case

    if specials_check_var.get():
        values += specials

    if specials2_check_var.get():
        values += specials2

    if values == "":
        label_warning["text"] = "You need to check at least 1 checkbox!"
        clear()
        print("Error")
    else:
        for i in range(16):
            label_password["text"] += choice(values)
            label_warning["text"] = ""
        clear()
        print(values)
        print("Password generated!")


clear()


app = Tk()


# app window specs
window_x = 520
window_y = 600


# user screen infos
user_screen_x = app.winfo_screenwidth()
user_screen_y = app.winfo_screenheight()


# window position
position_x = (user_screen_x / 2) - (window_x / 2)
position_y = (user_screen_y / 2) - (window_y / 2)


# labels
label_title = Label(
    app,
    text="Password generator",
    font="Verdana 18",
    fg="lime",
    bg="black",
    relief="flat",
    width=100,
    height=2,
)
label_password = Label(
    app,
    text="final password",
    font="Verdana 14",
    fg="black",
    bg="bisque",
    relief="flat",
    height=2,
)
label_warning = Label(
    app,
    text="",
    font="Verdana 14",
    fg="red",
    bg="bisque",
    relief="flat",
    height=2,
)


# checkboxes vars
number_check_var = BooleanVar()
lower_check_var = BooleanVar()
upper_check_var = BooleanVar()
specials_check_var = BooleanVar()
specials2_check_var = BooleanVar()


# checkboxes
number_check = Checkbutton(
    app,
    text="Numbers",
    font="Verdana 14",
    fg="black",
    bg="bisque",
    relief="flat",
    height=2,
    variable=number_check_var,
    onvalue=True,
    offvalue=False,
)
number_check.select()
lower_check = Checkbutton(
    app,
    text="abc ... xyz",
    font="Verdana 14",
    fg="black",
    bg="bisque",
    relief="flat",
    height=2,
    variable=lower_check_var,
    onvalue=True,
    offvalue=False,
)
lower_check.select()
upper_check = Checkbutton(
    app,
    text="ABC ... XYZ",
    font="Verdana 14",
    fg="black",
    bg="bisque",
    relief="flat",
    height=2,
    variable=upper_check_var,
    onvalue=True,
    offvalue=False,
)
upper_check.select()
specials_check = Checkbutton(
    app,
    text=specials,
    font="Verdana 14",
    fg="black",
    bg="bisque",
    relief="flat",
    height=2,
    variable=specials_check_var,
    onvalue=True,
    offvalue=False,
)
specials2_check = Checkbutton(
    app,
    text=specials2,
    font="Verdana 14",
    fg="black",
    bg="bisque",
    relief="flat",
    height=2,
    variable=specials2_check_var,
    onvalue=True,
    offvalue=False,
)


# window size configs
app.title("Password generator - by ZIUGOD")
app.geometry(
    "%dx%d+%d+%d" % (window_x, window_y, position_x, position_y)
)  # window size and where to appear
app.minsize(width=480, height=592)  # minimum size
app.resizable(False, False)  # not resizing X and Y
app["bg"] = "bisque"
# app["bg"] = "white"


# buttons
button_generate = Button(
    app,
    text="Generate password",
    font="Verdana 16",
    fg="white",
    bg="#331c00",
    padx=6,
    pady=3,
    bd=3,
    relief="ridge",
    command=lambda: generatePassword(),
)  # main button


# packs
label_title.pack()
label_password.pack()
label_warning.pack()
number_check.pack()
lower_check.pack()
upper_check.pack()
specials_check.pack()
specials2_check.pack()


button_generate.pack()

app.mainloop()  # running the application
