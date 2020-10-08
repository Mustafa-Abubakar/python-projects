from tkinter import*

def btnCkick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)

def ClearDisplay():
    global operator
    operator=''
    text_Input.set('')

def EqualInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ''

def off():
    exit()

cal = Tk()
cal.title("Calculator @Ascad Bin Abubakar")
operator = ""
text_Input = StringVar()

textDisplay = Entry(cal, font=('arial', 20 ,'bold'),textvariable=text_Input, bd=30,
                    insertwidth=4,bg="cyan",justify="right").grid(columnspan=4)

Percentage = Button(cal, padx=13, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="%", command=lambda:btnCkick('/100'),bg="gray").grid(row=1,column=0)

power = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="^",  command=lambda:btnCkick('**'), bg="gray",).grid(row=1,column=1)

DEL = Button(cal, padx=4, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="Del", command=ClearDisplay, bg="red",).grid(row=1,column=2)

AC = Button(cal, padx=5, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="AC", command=off,bg="red",).grid(row=1,column=3)


#=================================================================================


btn1 = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="1", command=lambda:btnCkick(1),bg="gray",).grid(row=2,column=0)

btn2 = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="2", command=lambda:btnCkick(2),bg="gray",).grid(row=2,column=1)

btn3 = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="3", command=lambda:btnCkick(3),bg="gray",).grid(row=2,column=2)

Addition = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="+", command=lambda:btnCkick('+'),bg="gray",).grid(row=2,column=3)

#=============================================================================
btn4 = Button(cal, padx=16, pady=16,bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="4",command=lambda:btnCkick(4),bg="gray",).grid(row=3,column=0)

btn5 = Button(cal, padx=16, pady=16,bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="5",command=lambda:btnCkick(5),bg="gray",).grid(row=3,column=1)

btn6 = Button(cal, padx=16, pady=16,bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="6",command=lambda:btnCkick(6),bg="gray",).grid(row=3,column=2)

Subtraction = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="- ", command=lambda:btnCkick('-'),bg="gray",).grid(row=3,column=3)

#============================================================================
btn7 = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="7", command=lambda:btnCkick(7), bg="gray",).grid(row=4,column=0)

btn8 = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="8",command=lambda:btnCkick(8),bg="gray",).grid(row=4,column=1)

btn9 = Button(cal, padx=16,pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="9",command=lambda:btnCkick(9),bg="gray",).grid(row=4,column=2)

Multiply = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="* ", command=lambda:btnCkick('*'),bg="gray",).grid(row=4,column=3)

#=========================================================================

btn0 = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="0", command=lambda:btnCkick(0),bg="gray",).grid(row=5,column=0)

Point = Button(cal, padx=13, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text=". ", command=lambda:btnCkick('.'),bg="gray").grid(row=5,column=1)

Division = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="/ ", command=lambda:btnCkick('/'),bg="gray",).grid(row=5,column=2)


Equals = Button(cal, padx=16, pady=16, bd=8, fg='white', font=('arial', 20 ,'bold'),
              text="=", command=EqualInput, bg="gray",).grid(row=5,column=3)


cal.mainloop()

