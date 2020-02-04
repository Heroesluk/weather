import tkinter as tk
import requests
import json
from datetime import date

# TODO: wyswietlanie miast z pliku: NAJPOPULARNIEJSZE -> TE PO WYSZUKANIU
# TODO: implementacja wyswietlania informacji w aplikacji, na podstawie wybranego z LISTY miasta
# TODO: UI Improvment

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

    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


class Info():
    def __init__(self, link):
        self.link = link
        self.req = requests.get(link)
        self.data = self.req.json()
        self.days = [i for i in self.data['daily']['data']]  # list of day Json objects

        self.days_temp_High = [int(i['temperatureHigh']) for i in  self.days]
        self.days_temp_Low = [int(i['temperatureLow']) for i in  self.days]
        self.days_icon = [i['icon'] for i in  self.days]

        self.week_days_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        self.day = date.today().weekday()

        self.week_days = []


        for i in range(7):
            try:
                self.week_days.append(self.week_days_dict[self.day])
            except KeyError:
                self.day = 0
                self.week_days.append(self.week_days_dict[self.day])
            self.day += 1


def find():
    for i in range(7):
        print('At {} highest temp will be {} and the lowest will be {}, and the weather summary is {}'.format(
            d_unt.week_days[i],
            d_unt.days_temp_High[i],
            d_unt.days_temp_Low[i],
            d_unt.days_icon[i]))


d_unt = Info('https://api.darksky.net/forecast/7c53a90481bcc12e69c188a374ddae2d/51.7833,19.4667?units=si')
find()


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

#

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.information_page = InformationWidget(self)
        self.information_page.grid(row=0,column=0,sticky="nsew")

        self.graph_page = GraphWidget(self)
        self.graph_page.grid(row=1,column=0,sticky="nsew")

        self.day_page = DayWeatherWidget(self)
        self.day_page.grid(row=2,column=0,sticky="nsew")

        self.town_list = ListTown(self)
        self.town_list.grid(rowspan=2, row=0, column=1, sticky="nsew")

        self.button = tk.Button(self,command=self.on_click)
        self.button.grid(row=3,column=1)

    def on_click(self):
        self.day_page.overwrite()



class InformationWidget(tk.Frame):
    # show: TOWN, DAY, TIME, WEATHER_TYPE(E.G CLOUDY), WEATHER_TYPE_ICON,
    # DAY_TEMPERATURE, RAINFALL_CHANCE, MOISTURE, WIND_STR

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
        self.info_frame.grid(row=0, column=1)

        self.rainfall = tk.Label(self.info_frame, text='rainfall chance', font=SMOLL_FONT)
        self.rainfall.grid(row=0, column=0)

        self.moisture = tk.Label(self.info_frame, text='moisture', font=SMOLL_FONT)
        self.moisture.grid(row=1, column=0)

        self.wind = tk.Label(self.info_frame, text='wind strenght', font=SMOLL_FONT)
        self.wind.grid(row=2, column=0)
##
        self.graph_switch_frame = tk.Frame(self)
        self.graph_switch_frame.grid(row=1,column=1)

        self.button_1 = tk.Button(self.graph_switch_frame, text='Temperature')
        self.button_2 = tk.Button(self.graph_switch_frame, text='rainfall chance')
        self.button_3 = tk.Button(self.graph_switch_frame, text='wind')

        self.button_1.grid(row=0, column=0, ipadx=10, ipady=5)
        self.button_2.grid(row=0, column=1, ipadx=10, ipady=5)
        self.button_3.grid(row=0, column=2, ipadx=10, ipady=5)


class GraphWidget(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background='green')

        self.spread_frame = tk.Frame(self)
        matlibb(self.spread_frame)
        self.spread_frame.grid(row=0, columnspan=2)


class DayWeatherWidget(tk.Frame):
    # SHOW: DAY, WEATHER_TYPE_ICON, DAY_TEMPERATURE, NIGHT_TEMPERATURE

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.temp_img = tk.PhotoImage(file='weather_mon.gif')

        self.configure(background='red')

        self.create_w()

    def create_w(self):
        self.MON_frame = tk.Frame(self)
        self.MON_frame.MON_day = tk.Label(self.MON_frame, text=d_unt.week_days[1], font=SMOLL_FONT)
        self.MON_frame.MON_img = tk.Label(self.MON_frame, image=self.temp_img).pack()
        self.MON_frame.MON_temp = tk.Label(self.MON_frame,
                                 text='{}C {}°C'.format(d_unt.days_temp_High[0], d_unt.days_temp_Low[0]),
                                 font=SMOLL_FONT).pack()

        self.MON_frame.grid(row=0,column=0)

    def overwrite(self):
        global d_unt
        del d_unt

        d_unt = Info('https://api.darksky.net/forecast/7c53a90481bcc12e69c188a374ddae2d/35.6895000,139.6917100?units=si')
        self.create_w()



class ListTown(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        eg = [str(i) + ' tak, dziala' for i in range(50)]
        var_eg = tk.StringVar(value=eg)

        self.entry = tk.Entry(self)
        self.entry.pack(fill='both')

        self.listbox = tk.Listbox(self, height=20, width=35, listvariable=var_eg)
        self.listbox.pack()


app = SeaofBTCapp()
app.mainloop()