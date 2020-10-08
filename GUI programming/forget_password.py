from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import sqlite3
import random


def password(screen, user):
    username = user
    screen = screen
    screen.title('Forget password')
    screen.iconbitmap('myico.ico')
    screen.geometry('500x600')
    screen.resizable(False, False)
    screen.configure(bg='#FFA900')
    
    # login frame and label
    login_frame = Frame(screen)
    login_frame.configure(bg='#FFA900')
    
    list = []
    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    index = 0
    while index < 3:
        lower = random.choice(Alphabet)
        upper = random.choice(Alphabet)
        num = random.choice(number)
        list.append(upper.upper())
        list.append(lower)
        list.append(num)
        index += 1
    code  = ['C','o','d','e', ':', ]
    
    code_label = Label(login_frame, text=code+list, font=('Time new roman', 0, 'bold'))
    code_label.configure(bg='#8119ff')
    code_label.pack()
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 0, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()
    
    # new password Frame label and widget
    password_frame = Frame(login_frame, bg='#FFA900')
    password_frame.pack()
    
    password_label = Label(password_frame, text='New password\t', font=('Comic Sans MS', 10, 'bold'))
    password_label.configure(bg='#FFA900')
    password_label.pack(side='left')
    
    password_entrty = Entry(password_frame, width=30, show='*', font=('Comic Sans MS', 10))
    password_entrty.pack(side='right')
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 10, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()
    
    # confirm password Frame label and widget
    confirm_frame = Frame(login_frame, bg='#FFA900')
    confirm_frame.pack()
    
    confirm_label = Label(confirm_frame, text='Confirm password\t', font=('Comic Sans MS', 10, 'bold'))
    confirm_label.configure(bg='#FFA900')
    confirm_label.pack(side='left')

    confirm_entry = Entry(confirm_frame, width=30, show='*', font=('Comic Sans MS', 10))
    code_label.configure(bg='#FFA900')
    confirm_entry.pack(side='right')
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 10, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()
    
    # code Frame label and widget
    coding_frame = Frame(login_frame, bg='#FFA900')
    coding_frame.pack()
    
    Coding_label = Label(coding_frame, text='Enter code\t', font=('Comic Sans MS', 10, 'bold'))
    Coding_label.configure(bg='#FFA900')
    Coding_label.pack(side='left')
    
    coding_entry = Entry(coding_frame, width=30, font=('Comic Sans MS', 10))
    coding_entry.pack(side='right')
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 20, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()
    
    def Pass():
        password = password_entrty.get()
        confirmation = confirm_entry.get()
        code = coding_entry.get()
        coding = []
        for i in code:
            coding.append(i)
            
        if password == '' or confirmation == '' or code == '':
            tkinter.messagebox.showerror('Error', 'Please Fill all the blanks')
            
        elif ' ' in password:
            tkinter.messagebox.showerror('Error', "Password can't contain spaces")

        elif len(password) < 8:
            tkinter.messagebox.showerror('Error', 'Your password must be atleast 8 characters')

        elif len(password) > 14:
            tkinter.messagebox.showerror('Error', "Your password must be less than 14 characters")
            
        elif password != confirmation:
            tkinter.messagebox.showwarning('Error', 'Please check your confirmation password')
            
        elif coding != list:
            tkinter.messagebox.showerror('Error', 'Please check the code')
        else:
            message = tkinter.messagebox.askyesno('Confirmation', 'Are you sure that you want to change your '
                                                                     'password.\n ')
            if message == 1:
                password_entrty.delete(0, END)
                confirm_entry.delete(0, END)
                coding_entry.delete(0, END)
                # checking user data
                conn = sqlite3.connect('registration.db')
                c = conn.cursor()
                c.execute("SELECT *FROM registration WHERE username=?", (username,))
                c.execute("UPDATE registration SET password = ? WHERE username = ? ", (confirmation, username,))
                conn.commit()
                tkinter.messagebox.showinfo('Message', "You're successfully changed your password")
           

    
    # Button of log in
    ok = Button(login_frame, text='Save', command=Pass, width=10, font=('Comic Sans MS', 10, 'bold'))
    ok.configure(bg='#ff1100')
    ok.pack()
    
    login_frame.pack()
    
    screen.mainloop()


def forgetPassword(screen):
    screen = screen
    screen.title('Forget password')
    screen.iconbitmap('myico.ico')
    screen.geometry('500x550')
    screen.resizable(False, False)
    screen.configure(bg='#FFA900')
    
    # logo  Frame with its labels
    Logo_frame = Frame(screen)
    Logo_frame.configure(bg='#FFA900')
    Logo_frame.pack()
    
    logo_img = ImageTk.PhotoImage(Image.open('myico.ico'))
    Logo_label = Label(Logo_frame, image=logo_img)
    Logo_label.configure(bg='#FFA900')
    Logo_label.pack()
    
    # Space between frames
    space_label = Label(screen, text='', font=('Comic Sans MS', 20, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()
    
    # login frame and label
    login_frame = Frame(screen)
    login_frame.configure(bg='#FFA900')
    
    user_label = Label(login_frame, text='if you forget your password, please enter your username',
                       font=('Comic Sans MS', 10, 'bold'))
    user_label.configure(bg='#FFA900')
    user_label.pack()
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 20, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()
    
    # username Frame label and widget
    username_frame = Frame(login_frame)
    username_frame.configure(bg='#FFA900')
    username_frame.pack()
    
    username_entrty = Entry(username_frame, width=30, font=('Comic Sans MS', 10))
    username_entrty.insert(0, 'Enter Your username')
    username_entrty.pack()
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 20, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()
    
    def Pass():
        username = username_entrty.get()
        # checking user data
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute("SELECT *FROM registration WHERE username=?", (username,))
        data = c.fetchone()
        conn.commit()
        
        if username_entrty.get() == '':
            tkinter.messagebox.showerror('Error', 'Please enter your username')
        
        elif data is None:
            tkinter.messagebox.showerror('Error', 'Invalid username\n Please enter your username correctly')
        else:
            screen.deletecommand(str(login_frame))
            password(screen, username)
    
    # Button of log in
    ok = Button(login_frame, text='OK', command=Pass, width=10, font=('Comic Sans MS', 10, 'bold'))
    ok.configure(bg='#ff1100')
    ok.pack()
    
    login_frame.pack()
    
    screen.mainloop()

# forgetPassword(screen=Tk())