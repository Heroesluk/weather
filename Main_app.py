import tkinter as tk

LARGE_FONT = ("Verdana", 25)
SMOLL_FONT = ("Verdana", 13)
def matlibb(root):
    import tkinter

    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg, NavigationToolbar2Tk)
    # Implement the default Matplotlib key bindings.
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    import numpy as np

    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)

    canvas.mpl_connect("key_press_event", on_key_press)

    def _quit():
        root.quit()  # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)
    # If you put root.destroy() here, it will cause an error if the window is
    # closed with the window manager.


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
        information_page.grid(row=0,column=0,pady=50,sticky="nsew")

        graph_page = GraphWidget(self)
        graph_page.grid(row=1,column=0,sticky="nsew")

        day_page = DayWeatherWidget(self)
        day_page.grid(row=2,column=0,sticky="nsew")


class InformationWidget(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background='blue')

#
        self.town_label = tk.Label(self, text='MIASTO', font=LARGE_FONT)  # Displays town
        self.town_label.grid(row=0, column=0)

        self.day_label = tk.Label(self, text='DZIEN', font=SMOLL_FONT)  # Displays day
        self.day_label.grid(row=1, column=0)

        self.forcecast_label = tk.Label(self, text='FORECAST', font=SMOLL_FONT)  # Displays text forecast
        self.forcecast_label.grid(row=2, column=0)

#

        self.display_frame = tk.Frame(self)  # Displays weather(as picture) and temperature
        self.display_frame.grid(row=3, column=0)

        self.temperature = tk.Label(self.display_frame, text='18°C', font=SMOLL_FONT)
        self.weather_image = tk.PhotoImage(file='weather.gif')
        self.image_label = tk.Label(self.display_frame, image=self.weather_image)

        self.image_label.grid(row=0, column=0)
        self.temperature.grid(row=0,column=1)


##
        self.info_frame = tk.Frame(self)  # Frame containing 3 labels made below
        self.info_frame.grid(row=0, column=1, padx=1100)

        self.rainfall = tk.Label(self.info_frame, text='rainfall chance', font=SMOLL_FONT)
        self.rainfall.grid(row=0, column=0)

        self.moisture = tk.Label(self.info_frame, text='moisture', font=SMOLL_FONT)
        self.moisture.grid(row=1, column=0)

        self.wind = tk.Label(self.info_frame, text='wind strenght', font=SMOLL_FONT)
        self.wind.grid(row=2, column=0)
##
        self.graph_switch_frame = tk.Frame(self)
        self.graph_switch_frame.grid(row=1,column=1, padx=1100)

        self.button_1 = tk.Button(self.graph_switch_frame, text='Temperature')
        self.button_2 = tk.Button(self.graph_switch_frame, text='rainfall chance')
        self.button_3 = tk.Button(self.graph_switch_frame, text='wind')

        self.button_1.grid(row=0, column=0, ipadx=10, ipady=5)
        self.button_2.grid(row=0, column=1, ipadx=10, ipady=5)
        self.button_3.grid(row=0, column=2, ipadx=10, ipady=5)




    def change_text(self, text):
        #self.label['text'] = text
        pass


class GraphWidget(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background='green')

        self.spread_frame = tk.Frame(self)
        matlibb(self.spread_frame)
        self.spread_frame.grid(row=0, columnspan=2)


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