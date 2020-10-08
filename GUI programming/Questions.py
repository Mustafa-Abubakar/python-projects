from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound

window = Tk()
window.configure(bg='brown')
window.title('Competition')
window.iconbitmap('myico.ico')
window.geometry('500x550')

q1 = 'The value of x + x(x^x) when x = 2 is:\t               \n'
q2 = 'The sum of three numbers is 98. The ratio of the first to\n' \
     'the second is 2/3, and the ratio of the second to the  \n' \
     'third is 5/8. The second number is: '
q3 = 'An object moves a long a straight path with s=4t^2-16t\n' \
     ' the acceleration of the object when t=1second is:'
q4 = 'The distance light travels in one year is approximately\n' \
     ' 5,870,000,000,000 miles. The distance light travels in \n' \
     '100 years is: \n'
q5 = 'A boy has 3 shirts, 2 trousers, and 2 pair os shoes, in\n' \
     '  how many different ways can the boy get dressed?     \n'
q6 = 'A ball is thrown up from a tower  with a speed 15m/s.   \n' \
     ' How high will go before it begins to fall?'
q7 = 'If you drop a 10kh rock from a top of a 5m ladder. if     \n' \
     '  the speed of the rock is 10m/s, the energy of the \n' \
     '  rock when it reaches the ground is: '
q8 = '10 people came from different places and shake hands \n' \
     'each other, in how many ways could this be done?'
q9 = 'If I selected a a card at a random from a deck of 52       \n' \
     'playing cards , then the probability of not getting \n' \
     'Ace is:'
q10 = 'The centripetal needed to keep a 0.5kg object moving \n' \
      'in circular of radius of 1m if the velocity is 4m/s is: '
wn = ' '


def clickSound():
    playsound('Mouse Click.mp3')


def question1():
    global wn
    window.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    # logo
    logo_frame = Frame(wn)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    label = Label(logo_frame, image=logo)
    label.pack()

    # welcoming
    wel = Label(logo_frame, text='Question One', font=('algerian', 25, 'bold'))
    wel.pack()

    # question
    question = Label(logo_frame, text=q1, font=('Berlin Sans FB Demi', 15, 'bold'))
    question.pack()

    # Choosing the Answer
    answer_var = IntVar()
    A1 = Radiobutton(logo_frame, text='16', command=clickSound, font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=1)
    A1.pack()
    A2 = Radiobutton(logo_frame, text='18',command=clickSound, font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=2)
    A2.pack()
    A3 = Radiobutton(logo_frame, text='64', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=3)
    A3.pack()
    A4 = Radiobutton(logo_frame, text='10', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=4)
    A4.pack()
    # frame pack
    logo_frame.pack()

    # checking the answer
    def answer():
        clickSound()
        if answer_var.get() == 4:
            playsound('Applause.mp3')
            question2()

    # welcoming
    wel = Label(logo_frame, text='', font=('algerian', 25, 'bold'))
    wel.pack()
    # Button
    Next_button = Button(logo_frame, text='Confirm', command=answer, width=10, font=('Castellar', 24, 'bold'),
                         bg='red', bd=10)
    Next_button.pack()

    wn.mainloop()


def question2():
    global wn
    wn.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    # logo
    logo_frame = Frame(wn)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    label = Label(logo_frame, image=logo)
    label.pack()

    # welcoming
    wel = Label(logo_frame, text='Question Two', font=('algerian', 25, 'bold'))
    wel.pack()

    # question
    question = Label(logo_frame, text=q2, font=('Berlin Sans FB Demi', 15, 'bold'))
    question.pack()

    # Choosing the Answer
    answer_var = IntVar()
    A1 = Radiobutton(logo_frame, text='30',command=clickSound, font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=1)
    A1.pack()
    A2 = Radiobutton(logo_frame, text='15', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=2)
    A2.pack()
    A3 = Radiobutton(logo_frame, text='20',command=clickSound, font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=3)
    A3.pack()
    A4 = Radiobutton(logo_frame, text='33', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=4)
    A4.pack()
    # frame pack
    logo_frame.pack()

    # checking the answer
    def answer():
        clickSound()
        if answer_var.get() == 1:
            playsound('Applause.mp3')
            question3()

    # welcoming
    wel = Label(logo_frame, text='', font=('algerian', 10, 'bold'))
    wel.pack()

    # Button
    Next_button = Button(logo_frame, text='Confirm', command=answer, width=10, font=('Castellar', 24, 'bold'),
                         bg='red', bd=10)
    Next_button.pack()

    wn.mainloop()


def question3():
    global wn
    wn.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    # logo
    logo_frame = Frame(wn)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    label = Label(logo_frame, image=logo)
    label.pack()

    # welcoming
    wel = Label(logo_frame, text='Question Three', font=('algerian', 25, 'bold'))
    wel.pack()

    # question
    question = Label(logo_frame, text=q3, font=('Berlin Sans FB Demi', 15, 'bold'))
    question.pack()

    # Choosing the Answer
    answer_var = IntVar()
    A1 = Radiobutton(logo_frame, text='8m/s   ', font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=1)
    A1.pack()
    A2 = Radiobutton(logo_frame, text='-8m/s^2', font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=2)
    A2.pack()
    A3 = Radiobutton(logo_frame, text='8m/s^2 ', font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=3)
    A3.pack()
    A4 = Radiobutton(logo_frame, text='-8m/s  ', font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=4)
    A4.pack()
    # frame pack
    logo_frame.pack()

    # checking the answer
    def answer():
        clickSound()
        if answer_var.get() == 3:
            playsound('Applause.mp3')
            question4()

    # welcoming
    wel = Label(logo_frame, text='', font=('algerian', 20, 'bold'))
    wel.pack()

    # Button
    Next_button = Button(logo_frame, text='Confirm', command=answer, width=10, font=('Castellar', 24, 'bold'),
                         bg='red', bd=10)
    Next_button.pack()

    wn.mainloop()


def question4():
    global wn
    wn.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    # logo
    logo_frame = Frame(wn)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    label = Label(logo_frame, image=logo)
    label.pack()

    # welcoming
    wel = Label(logo_frame, text='Question Four', font=('algerian', 25, 'bold'))
    wel.pack()

    # question
    question = Label(logo_frame, text=q4, font=('Berlin Sans FB Demi', 15, 'bold'))
    question.pack()

    # Choosing the Answer
    answer_var = IntVar()
    A1 = Radiobutton(logo_frame,command=clickSound,text='587 × 10^-10 miles', font=('Berlin Sans FB Demi', 15, 'bold'),
                     variable=answer_var,
                     value=1)
    A1.pack()
    A2 = Radiobutton(logo_frame, command=clickSound,text='587 × 10^8 miles  ', font=('Berlin Sans FB Demi', 15, 'bold'),
                     variable=answer_var,
                     value=2)
    A2.pack()
    A3 = Radiobutton(logo_frame, command=clickSound,text='587 × 10^12 miles ', font=('Berlin Sans FB Demi', 15, 'bold'),
                     variable=answer_var,
                     value=3)
    A3.pack()
    A4 = Radiobutton(logo_frame, command=clickSound,text='587 × 10^10 miles ', font=('Berlin Sans FB Demi', 15, 'bold'),
                     variable=answer_var,
                     value=4)
    A4.pack()
    # frame pack
    logo_frame.pack()

    # checking the answer
    def answer():
        clickSound()
        if answer_var.get() == 3:
            playsound('Applause.mp3')
            question5()

    # Button
    Next_button = Button(logo_frame, text='Confirm', command=answer, width=10, font=('Castellar', 24, 'bold'),
                         bg='red', bd=10)
    Next_button.pack()

    wn.mainloop()


def question5():
    global wn
    wn.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    # logo
    logo_frame = Frame(wn)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    label = Label(logo_frame, image=logo)
    label.pack()

    # welcoming
    wel = Label(logo_frame, text='Question Five', font=('algerian', 25, 'bold'))
    wel.pack()

    # question
    question = Label(logo_frame, text=q5, font=('Berlin Sans FB Demi', 15, 'bold'))
    question.pack()

    # Choosing the Answer
    answer_var = IntVar()
    A1 = Radiobutton(logo_frame, text='8 ways ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=1)
    A1.pack()
    A2 = Radiobutton(logo_frame, text='12 ways', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=2)
    A2.pack()
    A3 = Radiobutton(logo_frame, text='2 ways ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=3)
    A3.pack()
    A4 = Radiobutton(logo_frame, text='6 ways ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=4)
    A4.pack()
    # frame pack
    logo_frame.pack()

    # checking the answer
    def answer():
        clickSound()
        if answer_var.get() == 2:
            playsound('Applause.mp3')
            question6()

    # welcoming
    wel = Label(logo_frame, text='', font=('algerian', 10, 'bold'))
    wel.pack()

    # Button
    Next_button = Button(logo_frame, text='Confirm', command=answer, width=10, font=('Castellar', 24, 'bold'),
                         bg='red', bd=10)
    Next_button.pack()

    wn.mainloop()


def question6():
    global wn
    wn.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    # logo
    logo_frame = Frame(wn)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    label = Label(logo_frame, image=logo)
    label.pack()

    # welcoming
    wel = Label(logo_frame, text='Question Six', font=('algerian', 25, 'bold'))
    wel.pack()

    # question
    question = Label(logo_frame, text=q6, font=('Berlin Sans FB Demi', 15, 'bold'))
    question.pack()

    # Choosing the Answer
    answer_var = IntVar()
    A1 = Radiobutton(logo_frame, text='20m ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=1)
    A1.pack()
    A2 = Radiobutton(logo_frame, text='150m ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=2)
    A2.pack()
    A3 = Radiobutton(logo_frame, text='1.5m ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=3)
    A3.pack()
    A4 = Radiobutton(logo_frame, text='22.5m', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=4)
    A4.pack()
    # frame pack
    logo_frame.pack()

    # checking the answer
    def answer():
        clickSound()
        if answer_var.get() == 4:
            playsound('Applause.mp3')
            question7()

    # welcoming
    wel = Label(logo_frame, text='', font=('algerian', 20, 'bold'))
    wel.pack()

    # Button
    Next_button = Button(logo_frame, text='Confirm', command=answer, width=10, font=('Castellar', 24, 'bold'),
                         bg='red', bd=10)
    Next_button.pack()

    wn.mainloop()


def question7():
    global wn
    wn.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    # logo
    logo_frame = Frame(wn)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    label = Label(logo_frame, image=logo)
    label.pack()

    # welcoming
    wel = Label(logo_frame, text='Question Seven', font=('algerian', 25, 'bold'))
    wel.pack()

    # question
    question = Label(logo_frame, text=q7, font=('Berlin Sans FB Demi', 15, 'bold'))
    question.pack()

    # Choosing the Answer
    answer_var = IntVar()
    A1 = Radiobutton(logo_frame, text='500J', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=1)
    A1.pack()
    A2 = Radiobutton(logo_frame, text='5J  ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=2)
    A2.pack()
    A3 = Radiobutton(logo_frame, text='100J', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=3)
    A3.pack()
    A4 = Radiobutton(logo_frame, text='50J ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=4)
    A4.pack()
    # frame pack
    logo_frame.pack()

    # checking the answer
    def answer():
        clickSound()
        if answer_var.get() == 1:
            playsound('Applause.mp3')
            question8()

    # welcoming
    wel = Label(logo_frame, text='', font=('algerian', 10, 'bold'))
    wel.pack()

    # Button
    Next_button = Button(logo_frame, text='Confirm', command=answer, width=10, font=('Castellar', 24, 'bold'),
                         bg='red', bd=10)
    Next_button.pack()

    wn.mainloop()


def question8():
    global wn
    wn.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    # logo
    logo_frame = Frame(wn)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    label = Label(logo_frame, image=logo)
    label.pack()

    # welcoming
    wel = Label(logo_frame, text='Question Eight', font=('algerian', 25, 'bold'))
    wel.pack()

    # question
    question = Label(logo_frame, text=q8, font=('Berlin Sans FB Demi', 15, 'bold'))
    question.pack()

    # Choosing the Answer
    answer_var = IntVar()
    A1 = Radiobutton(logo_frame, text='45 ways ',command=clickSound, font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=1)
    A1.pack()
    A2 = Radiobutton(logo_frame, text='30 ways ',command=clickSound, font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=2)
    A2.pack()
    A3 = Radiobutton(logo_frame, text='100 ways ',command=clickSound, font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=3)
    A3.pack()
    A4 = Radiobutton(logo_frame, text='10 ways ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=4)
    A4.pack()
    # frame pack
    logo_frame.pack()

    # checking the answer
    def answer():
        clickSound()
        if answer_var.get() == 1:
            playsound('Applause.mp3')
            question9()

    # welcoming
    wel = Label(logo_frame, text='', font=('algerian', 20, 'bold'))
    wel.pack()

    # Button
    Next_button = Button(logo_frame, text='Confirm', command=answer, width=10, font=('Castellar', 24, 'bold'),
                         bg='red', bd=10)
    Next_button.pack()

    wn.mainloop()


def question9():
    global wn
    wn.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    # logo
    logo_frame = Frame(wn)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    label = Label(logo_frame, image=logo)
    label.pack()

    # welcoming
    wel = Label(logo_frame, text='Question Nine', font=('algerian', 25, 'bold'))
    wel.pack()

    # question
    question = Label(logo_frame, text=q9, font=('Berlin Sans FB Demi', 15, 'bold'))
    question.pack()

    # Choosing the Answer
    answer_var = IntVar()
    A1 = Radiobutton(logo_frame, text='1/13 ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=1)
    A1.pack()
    A2 = Radiobutton(logo_frame, text='1/4  ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=2)
    A2.pack()
    A3 = Radiobutton(logo_frame, text='1/52 ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=3)
    A3.pack()
    A4 = Radiobutton(logo_frame, text='12/13', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=4)
    A4.pack()
    # frame pack
    logo_frame.pack()

    # checking the answer
    def answer():
        clickSound()
        if answer_var.get() == 4:
            playsound('Applause.mp3')
            question10()

    # welcoming
    wel = Label(logo_frame, text='', font=('algerian', 10, 'bold'))
    wel.pack()

    # Button
    Next_button = Button(logo_frame, text='Confirm', command=answer, width=10, font=('Castellar', 24, 'bold'),
                         bg='red', bd=10)
    Next_button.pack()

    wn.mainloop()


def question10():
    global wn
    wn.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    # logo
    logo_frame = Frame(wn)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    label = Label(logo_frame, image=logo)
    label.pack()

    # welcoming
    wel = Label(logo_frame, text='Question Ten', font=('algerian', 25, 'bold'))
    wel.pack()

    # question
    question = Label(logo_frame, text=q10, font=('Berlin Sans FB Demi', 15, 'bold'))
    question.pack()

    # Choosing the Answer
    answer_var = IntVar()
    A1 = Radiobutton(logo_frame, text='4N ', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=1)
    A1.pack()
    A2 = Radiobutton(logo_frame, text='8N ',command=clickSound, font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=2)
    A2.pack()
    A3 = Radiobutton(logo_frame, text='16N', command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=3)
    A3.pack()
    A4 = Radiobutton(logo_frame, text='2N ',command=clickSound,font=('Berlin Sans FB Demi', 15, 'bold'), variable=answer_var,
                     value=4)
    A4.pack()
    # frame pack
    logo_frame.pack()

    # checking the answer
    def answer():
        clickSound()
        if answer_var.get() == 2:
            playsound('Applause.mp3')
            winner()

    # welcoming
    wel = Label(logo_frame, text='', font=('algerian', 25, 'bold'))
    wel.pack()

    # Button
    Next_button = Button(logo_frame, text='Confirm', command=answer, width=10, font=('Castellar', 24, 'bold'),
                         bg='red', bd=10)
    Next_button.pack()

    wn.mainloop()


def winner():
    global wn
    wn.destroy()
    wn = Tk()
    wn.iconbitmap('myico.ico')
    wn.title('Competition')
    wn.configure(bg='brown')
    wn.geometry('500x500')

    img = ImageTk.PhotoImage(Image.open('cup.jpg'))

    # frame
    cup_frame = Frame(wn)
    cup = Label(cup_frame, image=img)
    cup.pack()
    cup_frame.pack()

    # cog
    wel = Label(cup_frame, text='Conguratulation \n You Won ', font=('algerian', 25, 'bold'))
    wel.pack()

    wn.mainloop()


# logo
logo_frame = Frame(window)
logo = ImageTk.PhotoImage(Image.open('Logo.png'))
label = Label(logo_frame, image=logo)
label.pack()
# welcoming
wel = Label(logo_frame, text='Welcome', font=('algerian', 25, 'bold'))
wel.pack()

# text
text = Label(logo_frame, text='Get Start Your Competition', font=('Berlin Sans FB Demi', 30, 'bold'))
text.pack()

# image
image = ImageTk.PhotoImage(Image.open('images.jpg'))
label = Label(logo_frame, image=image)
label.pack()

# frame pack
logo_frame.pack()

# Button
Next_button = Button(logo_frame, text='→', command=question1, width=2, font=('Castellar', 24, 'bold'), bg='red', bd=10)
Next_button.pack(side='right')

window.mainloop()
