import tkinter as tk
import requests
from datetime import date, datetime
from townsread import towns
from graph import matlibb
#TODO: czas w wykresie z wlasnego na dany dla strefy czasowej, current czas jako label, UI improvment

#nie chce mi sie tego gowna na razie drazyc
LARGE_FONT = ("Verdana", 25)
SMOLL_FONT = ("Verdana", 13)


class Info():  # days_temp_high&low week_days
    def __init__(self, link):
        self.link = link
        self.req = requests.get(link)
        self.data = self.req.json()
        self.days = [i for i in self.data['daily']['data']]  # list of day Json objects

        # Hour info for Graph
        self.hour_unix_times = [i['time'] for i in self.data['hourly']['data']][:24]
        self.hour_normal_times = [datetime.utcfromtimestamp(i).strftime('%H') for i in self.hour_unix_times]

        self.hour_temperatures = [i['temperature'] for i in self.data['hourly']['data']][:24]
        self.hour_rain_prob = [i['precipProbability'] for i in self.data['hourly']['data']][:24]
        self.hour_wind_speed = [i['windSpeed'] for i in self.data['hourly']['data']][:24]

        for i in range(len(self.hour_normal_times)):
            print(('time is {}, temperature is {}, rain probability is {}, wind speed is {}').format(
                self.hour_normal_times[i], self.hour_temperatures[i], self.hour_rain_prob[i], self.hour_wind_speed[i]))

        # Day info for  Information Widget
        self.icon = self.data['currently']['icon']
        self.town = 'Lodz'  # Do zmiany na variable
        self.temperature = self.data['currently']['temperature']
        self.forecast = self.data['currently']['summary']
        self.timezone = self.data['timezone']  # Temporary for town
        self.wind = int(self.data['currently']['windSpeed'] * 1.610)
        self.humidity = int(self.data['currently']['humidity'] * 100)
        self.rain_chance = int(self.data['currently']['precipProbability'] * 100)

        # Daily info for day weather widget
        self.days_temp_High = [int(i['temperatureHigh']) for i in self.days]
        self.days_temp_Low = [int(i['temperatureLow']) for i in self.days]
        self.days_icon = [i['icon'] for i in self.days]
        self.week_days_dict = {0: 'Monay', 1: 'Tuesday', 2: 'Wednsday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday',
                               6: 'Sunday'}
        self.day = date.today().weekday()
        self.week_days = []
        self.full_week_days = []
        for i in range(8):
            try:
                self.week_days.append(self.week_days_dict[self.day])
            except KeyError:
                self.day = 0
                self.week_days.append(self.week_days_dict[self.day])
            self.day += 1

        self.day = self.week_days[0]  # current day


DataInfo = Info('https://api.darksky.net/forecast/7c53a90481bcc12e69c188a374ddae2d/51.7833,19.4667?units=si') #Default data


class View:

    def __init__(self, master, data, town='Lodz'):
        self.town = town
        self.data = data
        self.frame = tk.Frame(master)  # Parent
        self.frame.pack()

        self.GraphWidget = self.GraphClass(self.frame, self.data)
        self.InformationWidget = self.InformationClass(self.frame, self.data, self.town)
        self.TownListWidget = self.TownListClass(self.frame)
        self.DayWeatherWidget = self.DayWeatherClass(self.frame, self.data)

        self.GraphWidget.grid(row=1, column=0, sticky="nsew")
        self.InformationWidget.grid(row=0, column=0, sticky="nsew")
        self.TownListWidget.grid(rowspan=2, row=0, column=1, sticky="nsew")
        self.DayWeatherWidget.grid(row=2, column=0, sticky="nsew")

    class GraphClass(tk.Frame):

        def __init__(self, master, data):
            tk.Frame.__init__(self, master)
            self.data = data
            self.spread_frame = tk.Frame(self)
            self.configure(background='red')
            matlibb(self.spread_frame, self.data)
            self.spread_frame.grid(row=0, columnspan=2)

    class InformationClass(tk.Frame):
        # show: TOWN, DAY, TIME, WEATHER_TYPE(E.G CLOUDY), WEATHER_TYPE_ICON,
        # DAY_TEMPERATURE, RAINFALL_CHANCE, MOISTURE, WIND_STR

        def __init__(self, parent, data, town):
            tk.Frame.__init__(self, parent)
            self.data = data
            self.town = town
            self.configure(background='blue')
            self.weather_image = tk.PhotoImage(file=data.icon + '.gif')

            # Parent Frames

            self.town_label = tk.Label(self, text=self.town, font=LARGE_FONT)  # Displays town
            self.day_label = tk.Label(self, text=self.data.day, font=SMOLL_FONT)  # Displays day
            self.forcecast_label = tk.Label(self, text=self.data.forecast, font=SMOLL_FONT)  # Displays text forecast
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

            self.temperature = tk.Label(self.display_frame, text='{}°C'.format(int(self.data.temperature)),
                                        font=SMOLL_FONT)
            self.image_label = tk.Label(self.display_frame, image=self.weather_image)

            self.rainfall = tk.Label(self.info_frame, text='Rainfall chance: {}%'.format(data.rain_chance),
                                     font=SMOLL_FONT)
            self.moisture = tk.Label(self.info_frame, text='Humidity: {}%'.format(data.humidity), font=SMOLL_FONT)
            self.wind = tk.Label(self.info_frame, text='Wind: {}%'.format(data.wind), font=SMOLL_FONT)

            self.button_1 = tk.Button(self.buttons_frame, text='Temperature')
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

            self.towns = ['Tokyo', 'New York', 'Mexico City', 'Mumbai', 'Sao Paulo', 'Delhi', 'Delhi', 'Shanghai',
                          'Kolkata',
                          'Los Angeles', 'Dhaka', 'Buenos Aires', 'Karachi', 'Cairo', 'Rio de Janeiro', 'Osaka',
                          'Moscow', 'Katowice']
            self.selected_town = ''
            self.var_towns = tk.StringVar(value=self.towns)

            self.listbox = tk.Listbox(self, height=20, width=35, listvariable=self.var_towns)
            self.listbox.bind('<<ListboxSelect>>', self.on_item_select)

            self.entry_var = tk.StringVar
            self.entry = tk.Entry(self)
            self.entry.bind('<Key>', self.on_new_entry)

            self.confirm_button = tk.Button(self, text='confirm town',
                                            command=lambda: MainApp.rebuild(self.selected_town))

            self.entry.grid(row=0, column=0)
            self.confirm_button.grid(row=1, column=0)
            self.listbox.grid(row=2, column=0)

        def on_new_entry(self, evt):
            w = evt.widget
            search_var = w.get()
            if search_var != '':
                self.towns = [i for i in MainApp.all_towns if search_var.lower() == i[:len(search_var)].lower()]

            self.var_towns = tk.StringVar(value=self.towns)
            self.listbox = tk.Listbox(self, height=35, width=35, listvariable=self.var_towns)
            self.listbox.bind('<<ListboxSelect>>', self.on_item_select)
            self.listbox.grid(row=2, column=0)

        def on_item_select(self, evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            self.selected_town = value

    class DayWeatherClass(tk.Frame):
        # SHOW: DAY, WEATHER_TYPE_ICON, DAY_TEMPERATURE, NIGHT_TEMPERATURE

        def __init__(self, parent, data):
            tk.Frame.__init__(self, parent)
            self.data = data
            self.images = [(tk.PhotoImage(file=self.data.days_icon[i] + '.gif')) for i in range(len(data.days_icon))]
            self.build()

        def build(self):
            for i in range(len(self.data.days_temp_High)):
                self.w_frame = tk.Frame(self)
                self.w_frame.day = tk.Label(self.w_frame, text=self.data.week_days[i], font=SMOLL_FONT).pack()
                self.w_frame.img = tk.Label(self.w_frame, image=self.images[i]).pack()
                self.w_frame.temp = tk.Label(self.w_frame, text=' {}°C,  {}°C'.format(self.data.days_temp_High[i],
                                                                                      self.data.days_temp_Low[
                                                                                          i])).pack()

                self.w_frame.pack(side='left')


class Controller:

    def __init__(self):
        self.root = tk.Tk()
        self.view = View(self.root, DataInfo)
        self.towns = towns()  # A Dict with structure: Town: (latitude, longitude)
        self.all_towns = towns().keys()

    def run(self):
        self.root.title('works')
        self.root.mainloop()

    def rebuild(self, town):
        if town == '':
            pass
        else:
            latitude, longitude = self.towns[town][0], self.towns[town][1]
            DataInfo = Info(
                'https://api.darksky.net/forecast/7c53a90481bcc12e69c188a374ddae2d/{},{}?units=si'.format(latitude,
                                                                                                          longitude))
            self.view.frame.destroy()
            self.view = View(self.root, DataInfo, town)


MainApp = Controller()
MainApp.run()
