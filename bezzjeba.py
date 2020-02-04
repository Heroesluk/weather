import tkinter as tk
import requests
import json
from datetime import date
global cuck
global DataInfo
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


class Info():  # days_temp_high&low week_days
    def __init__(self, link):
        self.link = link
        self.req = requests.get(link)
        self.data = self.req.json()
        self.days = [i for i in self.data['daily']['data']]  # list of day Json objects

        # Day info for  Information Widget
        self.icon = self.data['currently']['icon']
        self.town = 'Lodz' #Do zmiany na variable
        self.temperature = self.data['currently']['temperature']
        self.forecast = self.data['currently']['summary']
        self.timezone = self.data['timezone'] # Temporary for town

        # Daily
        self.days_temp_High = [int(i['temperatureHigh']) for i in self.days]
        self.days_temp_Low = [int(i['temperatureLow']) for i in self.days]
        self.days_icon = [i['icon'] for i in self.days]
        self.week_days_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday',
                               6: 'Sunday'}
        self.day = date.today().weekday()
        self.week_days = []
        for i in range(8):
            try:
                self.week_days.append(self.week_days_dict[self.day])
            except KeyError:
                self.day = 0
                self.week_days.append(self.week_days_dict[self.day])
            self.day += 1

        self.day = self.week_days[0] #current day



DataInfo = Info('https://api.darksky.net/forecast/7c53a90481bcc12e69c188a374ddae2d/51.7833,19.4667?units=si')

class Model:
    pass


class View:

    def __init__(self, master):
        self.frame = tk.Frame(master)  # Parent
        self.frame.pack()

        self.GraphWidget = self.GraphClass(self.frame)
        self.InformationWidget = self.InformationClass(self.frame)
        self.TownListWidget = self.TownListClass(self.frame)
        self.DayWeatherWidget = self.DayWeatherClass(self.frame)

        self.GraphWidget.grid(row=1, column=0, sticky="nsew")
        self.InformationWidget.grid(row=0, column=0, sticky="nsew")
        self.TownListWidget.grid(rowspan=2, row=0, column=1, sticky="nsew")
        self.DayWeatherWidget.grid(row=2, column=0, sticky="nsew")

    class GraphClass(tk.Frame):

        def __init__(self, master):
            tk.Frame.__init__(self, master)
            self.spread_frame = tk.Frame(self)
            matlibb(self.spread_frame)
            self.spread_frame.grid(row=0, columnspan=2)

    class InformationClass(tk.Frame):
        # show: TOWN, DAY, TIME, WEATHER_TYPE(E.G CLOUDY), WEATHER_TYPE_ICON,
        # DAY_TEMPERATURE, RAINFALL_CHANCE, MOISTURE, WIND_STR

        def __init__(self, parent):
            tk.Frame.__init__(self, parent)
            self.configure(background='blue')
            self.weather_image = tk.PhotoImage(file='weather.gif')

            # Parent Frames

            self.town_label = tk.Label(self, text=DataInfo.timezone, font=LARGE_FONT)  # Displays town
            self.day_label = tk.Label(self, text=DataInfo.day, font=SMOLL_FONT)  # Displays day
            self.forcecast_label = tk.Label(self, text=DataInfo.forecast, font=SMOLL_FONT)  # Displays text forecast
            self.display_frame = tk.Frame(self)  # Displays weather(as picture) and temperature
            self.info_frame = tk.Frame(self)  # Frame containing 3 labels made below
            self.buttons_frame = tk.Frame(self)

            self.day_label.grid(row=1, column=0)
            self.town_label.grid(row=0, column=0)
            self.forcecast_label.grid(row=2, column=0)
            self.display_frame.grid(row=3, column=0)
            self.info_frame.grid(row=0, column=1)
            self.buttons_frame.grid(row=1, column=1)

            # Children Frames

            self.temperature = tk.Label(self.display_frame, text='{}°C'.format(int(DataInfo.temperature)), font=SMOLL_FONT)
            self.image_label = tk.Label(self.display_frame, image=self.weather_image)

            self.rainfall = tk.Label(self.info_frame, text='rainfall chance', font=SMOLL_FONT)
            self.moisture = tk.Label(self.info_frame, text='moisture', font=SMOLL_FONT)
            self.wind = tk.Label(self.info_frame, text='wind strenght', font=SMOLL_FONT)

            self.button_1 = tk.Button(self.buttons_frame, text='Temperature',
                                      command=lambda: Controller.rebuild(cuck))
            self.button_2 = tk.Button(self.buttons_frame, text='rainfall chance')
            self.button_3 = tk.Button(self.buttons_frame, text='wind')

            self.image_label.grid(row=0, column=0)
            self.temperature.grid(row=0, column=1)

            self.rainfall.grid(row=0, column=0)
            self.moisture.grid(row=1, column=0)
            self.wind.grid(row=2, column=0)

            self.button_1.grid(row=0, column=0, ipadx=10, ipady=5)
            self.button_2.grid(row=0, column=1, ipadx=10, ipady=5)
            self.button_3.grid(row=0, column=2, ipadx=10, ipady=5)

    class TownListClass(tk.Frame):
        def __init__(self, parent):
            tk.Frame.__init__(self, parent)

            eg = [str(i) + ' tak, dziala' for i in range(50)]
            var_eg = tk.StringVar(value=eg)

            self.entry = tk.Entry(self)
            self.entry.pack(fill='both')

            self.listbox = tk.Listbox(self, height=20, width=35, listvariable=var_eg)
            self.listbox.pack()

    class DayWeatherClass(tk.Frame):
        # SHOW: DAY, WEATHER_TYPE_ICON, DAY_TEMPERATURE, NIGHT_TEMPERATURE

        def __init__(self, parent):
            tk.Frame.__init__(self, parent)
            self.temp_img = tk.PhotoImage(file='weather_mon.gif')

        def build(self, Data):
            for i in range(len(Data.days_temp_High)):
                self.w_frame = tk.Frame(self)
                self.w_frame.day = tk.Label(self.w_frame, text=Data.week_days[i], font=SMOLL_FONT).pack()
                self.w_frame.img = tk.Label(self.w_frame, image=self.temp_img).pack()
                self.w_frame.temp = tk.Label(self.w_frame, text=' {}°C,  {}°C'.format(Data.days_temp_High[i],
                                                                                  Data.days_temp_Low[i])).pack()

                self.w_frame.pack(side='left')


class Controller:

    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.view.DayWeatherWidget.build(DataInfo)

    def run(self):
        self.root.title('works')
        self.root.mainloop()

    def rebuild(self):
        DataInfo = Info('https://api.darksky.net/forecast/7c53a90481bcc12e69c188a374ddae2d/35.6895000,139.6917100?units=si')
        self.view.frame.destroy()
        self.view = View(self.root)
        self.view.DayWeatherClass.build(self.view.DayWeatherWidget, DataInfo)



cuck = Controller()
cuck.run()