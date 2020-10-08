from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('Application')
window.geometry('600x600')
window.configure(bg='red')
window.iconbitmap('myico.ico')


home = Frame(window)
home.configure(bg='blue')
page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)
page4 = Frame(window)

def raise_to(frame):
    frame.tkraise()

for frame in (home, page1, page2, page3, page4):
    frame.grid(row=0, column=0, sticky='news')

# ================= Home Page ===================================
image = ImageTk.PhotoImage(Image.open('myIcon..png'))
logo = Label(home, image=image)
logo.pack(side='top')
button = Button(home, text="next", command=lambda:raise_to(page1))
button.pack()

# ==================== ===========================================
welcome1 = Label(page1, text="PageOne")
welcome1.pack()
button = Button(page1, text="next", command=lambda:raise_to(page2))
button.pack()
welcome2 = Label(page2, text="pageTwo")
welcome2.pack()
button = Button(page2, text="next", command=lambda:raise_to(page3))
button.pack()
welcome3 = Label(page3, text="pageThree")
welcome3.pack()
button = Button(page3, text="next", command=lambda:raise_to(page4))
button.pack()
welcome4 = Label(page4, text="pageFour")
welcome4.pack()
button = Button(page4, text="next", command=lambda:raise_to(home))
button.pack()
raise_to(home)
window.mainloop()
