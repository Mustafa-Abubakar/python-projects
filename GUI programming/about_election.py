import tkinter
from tkinter.ttk import Combobox

wn = tkinter.Tk()
wn.title('Digital Election')


def voters():
    # message
    design = tkinter.Label(wn, text='***********',
                            font=('Forte', 55, 'normal'))
    design.pack(side='top')
    Welcome = tkinter.Label(wn, text='Fill all these blanks',
                            font=('Forte', 15, 'normal'))
    Welcome.pack(side='top')

    # Frames
    Num_voters = tkinter.Frame(wn)
    Num_votes_eachVoter = tkinter.Frame(wn)

    #  Create and pack the widgets for number of voters.
    voters = ['1-20', '20-50', '50-100', '100-200', '200-300', '300-500', '500+']
    Nvoters = tkinter.Label(Num_voters, text='Number of voters \t\t\t',
                            font=('Berlin Sans FB Demi', 12,))
    promt_Nvters = Combobox(Num_voters, value=voters, width=15, font=('Comic Sans MS', 10,))
    promt_Nvters.pack(side='right')
    Nvoters.pack(side='left')

    # Create and pack the widgets for Number of votes each voter.
    times = '1-time'
    time2 = 'more than 1 time'
    Nvotes = tkinter.Label(Num_votes_eachVoter, text='How many times can each voter votes?\t',
                           font=('Berlin Sans FB Demi', 12,))
    promt_Nvotes = Combobox(Num_votes_eachVoter, value=(times, time2), width=15, font=('Comic Sans MS', 10,))
    promt_Nvotes.pack(side='right')
    Nvotes.pack(side='left')

    #
    Num_voters.pack()
    Num_votes_eachVoter.pack()

    #

    # message
    design = tkinter.Label(wn, text=' ',
                            font=('Forte', 55, 'normal'))
    design.pack(side='top')
    Welcome = tkinter.Label(wn, text='',
                            font=('Forte', 15, 'normal'))
    Welcome.pack(side='top')

    # buttons
    Next = tkinter.Button(wn, text='Next', font=('Castellar', 12, 'bold'), bg='red', bd=2)
    Next.pack(side='right')
    Pre = tkinter.Button(wn, text='Pre', font=('Castellar', 12, 'bold'), bg='cyan')
    Pre.pack(side='left')


voters()
wn.mainloop()
