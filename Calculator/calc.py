#Quinten White
#3/4/2022
#CALCULATOR
from tkinter import *


expression = ""



def press(num):

    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():

    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":

    gui = Tk()
    gui.configure(background="white")
    gui.title(" Calculator")
    gui.geometry("375x300")
    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=80, ipadx=90)

    button1 = Button(gui, text=' 1 ', fg='white', bg='black',
                     command=lambda: press(1), height=3, width=12)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='white', bg='black',
                     command=lambda: press(2), height=3, width=12)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='white', bg='black',
                     command=lambda: press(3), height=3, width=12)
    button3.grid(row=2, column=2)
    button4 = Button(gui, text=' 4 ', fg='white', bg='black',
                     command=lambda: press(4), height=3, width=12)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='white', bg='black',
                     command=lambda: press(5), height=3, width=12)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='white', bg='black',
                     command=lambda: press(6), height=3, width=12)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='white', bg='black',
                     command=lambda: press(7), height=3, width=12)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='white', bg='black',
                     command=lambda: press(8), height=3, width=12)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='white', bg='black',
                     command=lambda: press(9), height=3, width=12)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='white', bg='black',
                     command=lambda: press(0), height=3, width=12)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='white', bg='black',
                  command=lambda: press("+"), height=3, width=12)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='white', bg='black',
                   command=lambda: press("-"), height=3, width=12)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='white', bg='black',
                      command=lambda: press("*"), height=3, width=12)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='white', bg='black',
                    command=lambda: press("/"), height=3, width=12)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='white', bg='black',
                   command=equalpress, height=3, width=12)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='white', bg='black',
                   command=clear, height=3, width=12)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='white', bg='black',
                 command=lambda: press('.'), height=3, width=12)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()