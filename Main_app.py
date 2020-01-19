import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('1600x900')

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)
        self.frames[StartPage] = frame

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.grid(row=0, column=0, sticky="nsew")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        information_page = InformationWidget(self)
        information_page.pack()

        graph_page = GraphWidget(self)
        graph_page.pack()

        day_page = DayWeatherWidget(self)
        day_page.pack()


class InformationWidget(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background='blue')

        self.label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)

        self.button2 = tk.Button(self, text='change text', command=lambda: self.change_text('fred oszukal freda'))
        self.button2.pack(pady=10, padx=10)

    def change_text(self, text):
        self.label['text'] = text


class GraphWidget(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background='green')

        self.label = tk.Label(self, text="Tutaj bedzie stonk graph", font=LARGE_FONT)
        self.label.grid(row=0, column=0)

        self.label = tk.Label(self, text="Tutaj tez stonk graph", font=LARGE_FONT)
        self.label.grid(row=0, column=1)

        self.label = tk.Label(self, text="I tu", font=LARGE_FONT)
        self.label.grid(row=0, column=2)



class DayWeatherWidget(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background='red')

        self.label = tk.Label(self, text="Poniedzialek", font=LARGE_FONT)
        self.label.grid(row=0, column=0, padx=5)

        self.label = tk.Label(self, text="Wtorek", font=LARGE_FONT)
        self.label.grid(row=0, column=1, padx=5)

        self.label = tk.Label(self, text="Sroda", font=LARGE_FONT)
        self.label.grid(row=0, column=2, padx=5)

        self.label = tk.Label(self, text="Czwartek", font=LARGE_FONT)
        self.label.grid(row=0, column=3, padx=5)

        self.label = tk.Label(self, text="Piatek", font=LARGE_FONT)
        self.label.grid(row=0, column=4, padx=5)

        self.label = tk.Label(self, text="Sobota", font=LARGE_FONT)
        self.label.grid(row=0, column=5, padx=5)

        self.label = tk.Label(self, text="Niedziela", font=LARGE_FONT)
        self.label.grid(row=0, column=6, padx=5)








app = SeaofBTCapp()
app.mainloop()