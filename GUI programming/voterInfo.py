import tkinter
from tkinter.ttk import Combobox

wn = tkinter.Tk()
wn.title('Digital Election')


def voterInfo():
    # message
    design = tkinter.Label(wn, text='***********',
                           font=('Forte', 55, 'normal'))
    design.pack(side='top')

    Welcome = tkinter.Label(wn, text='Registration of voters ',
                            font=('Forte', 15, 'normal'))
    Welcome.pack(side='top')
    # Frames
    name_frame = tkinter.Frame()
    gender_frame = tkinter.Frame()
    email_frame = tkinter.Frame()
    id_frame = tkinter.Frame()
    password_frame = tkinter.Frame()

    #  Create and pack the widgets for voter name.
    voter_name = tkinter.Label(name_frame, text='Voter Name\t', font=('Berlin Sans FB Demi', 12,))
    promt_voterName = tkinter.Entry(name_frame, width=25, font=('Comic Sans MS', 10,))
    promt_voterName.pack(side='right')
    voter_name.pack(side='left')

    # Create and pack the widgets for voter password.
    Gender = tkinter.Label(gender_frame, text='Gender\t\t', font=('Berlin Sans FB Demi', 12,))
    Gender.pack(side='left')
    Gender = Combobox(gender_frame, value='Male Female', width=18, font=('Comic Sans MS', 12,))
    Gender.pack(side='right')

    # Create and pack the widgets for voter email.
    voterEmail = tkinter.Label(email_frame, text='voter email\t', font=('Berlin Sans FB Demi', 12,))
    promt_voterEmail = tkinter.Entry(email_frame, width=25, font=('Comic Sans MS', 10,))
    promt_voterEmail.pack(side='right')
    voterEmail.pack(side='left')

    # Create and pack the widgets for voter ID.
    voterID = tkinter.Label(id_frame, text='voter ID\t\t', font=('Berlin Sans FB Demi', 12,))
    promt_voterID = tkinter.Entry(id_frame, width=25, font=('Comic Sans MS', 10,))
    promt_voterID.pack(side='right')
    voterID.pack(side='left')

    # Create and pack the widgets for voter password.
    voterPasswod = tkinter.Label(password_frame, text='voter Password\t', font=('Berlin Sans FB Demi', 12,))
    promt_voterPassword = tkinter.Entry(password_frame, width=25, font=('Comic Sans MS', 10,))
    promt_voterPassword.pack(side='right')
    voterPasswod.pack(side='left')

    #
    name_frame.pack()
    gender_frame.pack()
    email_frame.pack()
    id_frame.pack()
    password_frame.pack()

    # message
    Welcome = tkinter.Label(wn, text='', font=('Forte', 15, 'normal'))
    Welcome.pack(side='top')

    # buttons
    Next = tkinter.Button(wn, text='Next', font=('Castellar', 12, 'bold'), bg='red', bd=2)
    Next.pack(side='right')
    Pre = tkinter.Button(wn, text='Pre', font=('Castellar', 12, 'bold'), bg='cyan')
    Pre.pack(side='left')


voterInfo()
wn.mainloop()
