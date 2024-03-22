from tkinter import *

root = Tk()

root.title("sample calculator")

display_space = Entry(root, width=15)
display_space.grid(row=0, column=0, columnspan=3)


def display_number(numbers):
    present_number = display_space.get()
    display_space.delete(0, END)
    display_space.insert(0, str(present_number) + str(numbers))


def action_clear():
    display_space.delete(0, END)


def action_add():
    first_value = display_space.get()
    global firstvalue
    global math
    math = "addition"
    firstvalue = int(first_value)
    display_space.delete(0, END)


def action_sub():
    first_value = display_space.get()
    global firstvalue
    global math
    math = "subtraction"
    firstvalue = int(first_value)
    display_space.delete(0, END)


def action_mul():
    first_value = display_space.get()
    global firstvalue
    global math
    math = "multiplication"
    firstvalue = int(first_value)
    display_space.delete(0, END)


def action_div():
    first_value = display_space.get()
    global firstvalue
    global math
    math = "division"
    firstvalue = int(first_value)
    display_space.delete(0, END)


def action_equal():
    second_value = display_space.get()
    display_space.delete(0, END)
    if math == "addition":
        display_space.insert(0, firstvalue + int(second_value))
    if math == "subtraction":
        display_space.insert(0, firstvalue - int(second_value))
    if math == "multiplication":
        display_space.insert(0, firstvalue * int(second_value))
    if math == "division":
        display_space.insert(0, int(firstvalue / int(second_value)))
    # if math == "addition":
    # display_space.insert(0, firstvalue + int(second_value))
    # if math == "addition":
    # display_space.insert(0, firstvalue + int(second_value))""


button1 = Button(root, text="1", width=5, height=5, padx=1, pady=1, command=lambda: display_number(1))
button2 = Button(root, text="2", width=5, height=5, padx=1, pady=1, command=lambda: display_number(2))
button3 = Button(root, text="3", width=5, height=5, padx=1, pady=1, command=lambda: display_number(3))
button4 = Button(root, text="4", width=5, height=5, padx=1, pady=1, command=lambda: display_number(4))
button5 = Button(root, text="5", width=5, height=5, padx=1, pady=1, command=lambda: display_number(5))
button6 = Button(root, text="6", width=5, height=5, padx=1, pady=1, command=lambda: display_number(6))
button7 = Button(root, text="7", width=5, height=5, padx=1, pady=1, command=lambda: display_number(7))
button8 = Button(root, text="8", width=5, height=5, padx=1, pady=1, command=lambda: display_number(8))
button9 = Button(root, text="9", width=5, height=5, padx=1, pady=1, command=lambda: display_number(9))
button0 = Button(root, text="0", width=5, height=5, padx=1, pady=1, command=lambda: display_number(0))

button_clear = Button(root, text="clear", width=5, height=5, padx=1, pady=1, command=action_clear)

button_add = Button(root, text="+", width=5, height=5, padx=1, pady=1, command=action_add)
button_sub = Button(root, text="-", width=5, height=5, padx=1, pady=1, command=action_sub)
button_mul = Button(root, text="*", width=5, height=5, padx=1, pady=1, command=action_mul)
button_div = Button(root, text="/", width=5, height=5, padx=1, pady=1, command=action_div)
button_equal = Button(root, text="=", width=5, height=5, padx=1, pady=1, command=action_equal)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

button_clear.grid(row=4, column=2)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_equal.grid(row=4, column=1)

root.mainloop()