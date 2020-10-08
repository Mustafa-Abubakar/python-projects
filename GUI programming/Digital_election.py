import tkinter
import sqlite3

wn = tkinter.Tk()
wn.title('Digital Election')


# create a table

# c.execute("""CREATE TABLE login(
#         first_name text,
#         middle_name text,
#         last_name text,
#         email text,
#         password, text
#  )""")

def submit():
    # create a database and connect to your file
    conn = sqlite3.connect('SignUp.db')

    # creat a curser
    c = conn.cursor()

    # inser into the table
    c.execute("INSERT INTO SingUp")

    # commit changes
    conn.commit()

    # close connection
    conn.close()
    #
    # promt_fName.delete(0, END)
    # promt_mName.delete(0, END)
    # promt_lName.delete(0, END)
    # promt_email.delete(0, END)
    # promt_password.delete(0, END)
    # promt_con_pass.delete(0, END)



# welcoming message
design = tkinter.Label(wn, text='***********',
                       font=('Forte', 25, 'normal'))
design.pack(side='top')

Welcome = tkinter.Label(wn, text='Welcome to Digital Election, To use this program please SingUp',
                        font=('Forte', 11, 'normal'))
Welcome.pack(side='top')

# Frames
fName_frame = tkinter.Frame(wn)
mName_frame = tkinter.Frame(wn)
lName_frame = tkinter.Frame(wn)
Email_frame = tkinter.Frame(wn)
Pass_frame = tkinter.Frame(wn)
conf_frame = tkinter.Frame(wn)

#  Create and pack the widgets for first name.
fName = tkinter.Label(fName_frame, text='First Name:\t', font=('Berlin Sans FB Demi', 12,))
promt_fName = tkinter.Entry(fName_frame, width=25, font=('Comic Sans MS', 10,))
promt_fName.pack(side='right')
fName.pack(side='left')

# Create and pack the widgets for second name.
mName = tkinter.Label(mName_frame, text='Middle Name:\t', font=('Berlin Sans FB Demi', 12,))
promt_mName = tkinter.Entry(mName_frame, width=25, font=('Comic Sans MS', 10,))
promt_mName.pack(side='right')
mName.pack(side='left')

# Create and pack the widgets for last name.
lName = tkinter.Label(lName_frame, text='Last Name:\t', font=('Berlin Sans FB Demi', 12,))
promt_lName = tkinter.Entry(lName_frame, width=25, font=('Comic Sans MS', 10,))
promt_lName.pack(side='right')
lName.pack(side='left')

# Create and pack the widgets for email.
Email = tkinter.Label(Email_frame, text='Email:          \t', font=('Berlin Sans FB Demi', 12,))
promt_email = tkinter.Entry(Email_frame, width=25, font=('Comic Sans MS', 10,))
promt_email.pack(side='right')
Email.pack(side='left')

# Create and pack the widgets for password.
Password = tkinter.Label(Pass_frame, text='Create Password:\t', font=('Berlin Sans FB Demi', 12,))
promt_password = tkinter.Entry(Pass_frame, width=25, font=('Comic Sans MS', 10,))
promt_password.pack(side='right')
Password.pack(side='left')

# Create and pack the widgets for confirmation password.
Con_password = tkinter.Label(conf_frame, text='Confirm Password:\t', font=('Berlin Sans FB Demi', 12,))
promt_con_pass = tkinter.Entry(conf_frame, width=25, font=('Comic Sans MS', 10,))
promt_con_pass.pack(side='right')
Con_password.pack(side='left')

# frames
fName_frame.pack()
mName_frame.pack()
lName_frame.pack()
Email_frame.pack()
Pass_frame.pack()
conf_frame.pack()

# SignUp
SignUp = tkinter.Button(wn, text='Sign Up', font=('Castellar', 12, 'bold'), bg='red', bd=2)
SignUp.pack()
Old_account = tkinter.Label(wn, text='Already Have an Account', font=('Bauhaus 93', 15, 'normal'))
Old_account.pack()
SignIn = tkinter.Button(wn, text='Sign In', font=('Castellar', 12, 'bold'), bg='cyan')
SignIn.pack()




wn.mainloop()
