# live obrazek o godzinie
from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry('1600x900')

town_frame = Frame(root,bg='blue')
town_frame.grid(row=0, column=0)


def_font = Font(family='Arial', size=24)

town = StringVar()
text_label = Label(town_frame, text='Podaj miasto dla którego chcesz poznać pogodę', font=def_font)
entry_town = Entry(town_frame, textvariable=town, font='Helvetica 44 bold', width=13)
send_butt = Button(town_frame, text='confirm', command=lambda: print(entry_town.get()), font='Helvetica 24 bold')
town_list = Listbox(town_frame, height=10)

text_label.grid(columnspan=2,row=0,ipady=10)
entry_town.grid(column=0, row=1, sticky=W+E+N+S)
send_butt.grid(column=1, row=1, sticky=W+E+N+S)
town_list.grid(column=0,row=2, sticky=W+E+N+S)

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
