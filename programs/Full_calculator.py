from tkinter import *
import math
import parser
import tkinter.messagebox

cal = Tk()
cal.title("Scientific Calculator ")
operator = ""
text_Input = StringVar()
cal.configure(background="gray")

textDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30,
                    insertwidth=4, bg="cyan", justify="right").grid(columnspan=5)


def btnCkick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)


def ClearDisplay():
    global operator
    operator = ''
    text_Input.set('')


def EqualInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ''


def sin(number, ):
    global operator
    math.sin(number)


def off():
    exit()


# ==========================Row 2 ===================================================
Factorial = Button(cal, padx=10, pady=0, bd=4, fg='white', font=('arial', 20, 'bold'),
                   text="!", bg="black").grid(row=2, column=0)

Redical = Button(cal, padx=6, pady=0, bd=4, fg='white', font=('arial', 20, 'bold'),
                 text="√", bg="black", command=lambda: btnCkick("√")).grid(row=2, column=1)

Square = Button(cal, padx=6, pady=0, bd=4, fg='white', font=('arial', 20, 'bold'),
                text="^", bg="black", command=lambda: btnCkick('**')).grid(row=2, column=2)

ln = Button(cal, padx=14, pady=14, bd=4, fg='white', font=('arial', 10, 'bold'),
            text="ln", bg="black", command=lambda: btnCkick("ln")).grid(row=2, column=3)

log = Button(cal, padx=11, pady=15, bd=4, fg='white', font=('arial', 10, 'bold'),
             text="log", bg="black", command=lambda: btnCkick("log")).grid(row=2, column=4)

# ==========================Row 3 ===================================================
Percentage = Button(cal, padx=10, pady=0, bd=4, fg='white', font=('arial', 20, 'bold'),
                    text=" ", bg="black").grid(row=3, column=0)

Percentage = Button(cal, padx=10, pady=0, bd=4, fg='white', font=('arial', 20, 'bold'),
                    text=" ", bg="black").grid(row=3, column=1)

Sin = Button(cal, padx=11, pady=14, bd=4, fg='white', font=('arial', 10, 'bold'),
             text="sin", bg="black", command=lambda: btnCkick("sin")).grid(row=3, column=2)

Cos = Button(cal, padx=11, pady=14, bd=4, fg='white', font=('arial', 10, 'bold'),
             text="cos", bg="black", command=lambda: btnCkick("cos")).grid(row=3, column=3)

Tan = Button(cal, padx=11, pady=14, bd=4, fg='white', font=('arial', 10, 'bold'),
             text="tan", bg="black", command=lambda: btnCkick("tan")).grid(row=3, column=4)

# ==========================Row 4 ===================================================
plus_or_minus = Button(cal, padx=13, pady=8, bd=4, fg='white', font=('arial', 15, 'bold'),
                       text="±", bg="black", ).grid(row=4, column=0)
Obracket = Button(cal, padx=10, pady=0, bd=4, fg='white', font=('arial', 20, 'bold'),
                  text="(", bg="black", command=lambda: btnCkick('(')).grid(row=4, column=1)

Cbracket = Button(cal, padx=10, pady=0, bd=4, fg='white', font=('arial', 20, 'bold'),
                  text=")", bg="black", command=lambda: btnCkick(')')).grid(row=4, column=2)

Pi = Button(cal, padx=10, pady=8, bd=4, fg='white', font=('arial', 15, 'bold'),
            text="π", bg="black", command=lambda: btnCkick(math.pi)).grid(row=4, column=3)

Modulas = Button(cal, padx=7, pady=14, bd=4, fg='white', font=('arial', 10, 'bold'),
                 text="Mod", bg="black", command=lambda: btnCkick("%")).grid(row=4, column=4)

# ==========================Row 5 ===================================================
btn7 = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="7", bg="white", command=lambda: btnCkick(7)).grid(row=5, column=0)

btn8 = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="8", bg="white", command=lambda: btnCkick(8)).grid(row=5, column=1)

btn9 = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="9", bg="white", command=lambda: btnCkick(9)).grid(row=5, column=2)

Del = Button(cal, padx=12, pady=22, bd=4, fg='black', font=('arial', 13, 'bold'),
             text="Del", bg="red", command=ClearDisplay).grid(row=5, column=3)

AC = Button(cal, padx=12, pady=22, bd=4, fg='black', font=('arial', 13, 'bold'),
            text="AC", bg="red", command=off).grid(row=5, column=4)

# ==========================Row 6 ===================================================
btn4 = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="4", bg="white", command=lambda: btnCkick(4)).grid(row=6, column=0)

btn5 = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="5", bg="white", command=lambda: btnCkick(5)).grid(row=6, column=1)

btn6 = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="6", bg="white", command=lambda: btnCkick(6)).grid(row=6, column=2)

Multiply = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
                  text="×", bg="white", command=lambda: btnCkick('*')).grid(row=6, column=3)

Devision = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
                  text="÷", bg="white", command=lambda: btnCkick("/")).grid(row=6, column=4)

# ==========================Row 7 ===================================================
btn1 = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="1", bg="white", command=lambda: btnCkick(1)).grid(row=7, column=0)

btn2 = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="2", bg="white", command=lambda: btnCkick(2)).grid(row=7, column=1)

btn3 = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="3", bg="white", command=lambda: btnCkick(3)).grid(row=7, column=2)

Addition = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
                  text="+", bg="white", command=lambda: btnCkick('+')).grid(row=7, column=3)

Subtraction = Button(cal, padx=13, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
                     text="-", bg="white", command=lambda: btnCkick('-')).grid(row=7, column=4)

# ==========================Row 8 ===================================================
btn0 = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="0", bg="white", command=lambda: btnCkick(0)).grid(row=8, column=0)

btnpoint = Button(cal, padx=13, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
                  text=".", bg="white", command=lambda: btnCkick('.')).grid(row=8, column=1)

btnExponent = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
                     text="e", bg="white", command=lambda: btnCkick('e')).grid(row=8, column=2)

Percentage = Button(cal, padx=6, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
                    text="%", bg="white", command=lambda: btnCkick('/100')).grid(row=8, column=3)

btnequals = Button(cal, padx=10, pady=10, bd=4, fg='black', font=('arial', 20, 'bold'),
                   text="=", bg="white", command=EqualInput).grid(row=8, column=4)

cal.mainloop()
