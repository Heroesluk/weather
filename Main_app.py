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

    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


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

        information_page = InformationWidget(self)
        information_page.grid(row=0,column=0,sticky="nsew")

        graph_page = GraphWidget(self)
        graph_page.grid(row=1,column=0,sticky="nsew")

        day_page = DayWeatherWidget(self)
        day_page.grid(row=2,column=0,sticky="nsew")

        town_list = ListTown(self)
        town_list.grid(rowspan=2, row=0, column=1, sticky="nsew")

print('dziala')
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
        self.temp_img = tk.PhotoImage(file='weather_mon.gif')

        self.configure(background='red')

        self.MON_frame = tk.Frame(self)
        self.MON_day = tk.Label(self.MON_frame, text='Monday', font=SMOLL_FONT).pack()
        self.MON_img = tk.Label(self.MON_frame, image=self.temp_img).pack()
        self.MON_temp = tk.Label(self.MON_frame, text='5°C 0°C', font=SMOLL_FONT).pack()

        self.TUE_frame = tk.Frame(self)
        self.TUE_day = tk.Label(self.TUE_frame, text='Monday', font=SMOLL_FONT).pack()
        self.TUE_img = tk.Label(self.TUE_frame, image=self.temp_img).pack()
        self.TUE_temp = tk.Label(self.TUE_frame, text='5°C 0°C', font=SMOLL_FONT).pack()

        self.WED_frame = tk.Frame(self)
        self.WED_day = tk.Label(self.WED_frame, text='Monday', font=SMOLL_FONT).pack()
        self.WED_img = tk.Label(self.WED_frame, image=self.temp_img).pack()
        self.WED_temp = tk.Label(self.WED_frame, text='5°C 0°C', font=SMOLL_FONT).pack()

        self.THU_frame = tk.Frame(self)
        self.THU_day = tk.Label(self.THU_frame, text='Monday', font=SMOLL_FONT).pack()
        self.THU_img = tk.Label(self.THU_frame, image=self.temp_img).pack()
        self.THU_temp = tk.Label(self.THU_frame, text='5°C 0°C', font=SMOLL_FONT).pack()

        self.FRI_frame = tk.Frame(self)
        self.FRI_day = tk.Label(self.FRI_frame, text='Monday', font=SMOLL_FONT).pack()
        self.FRI_img = tk.Label(self.FRI_frame, image=self.temp_img).pack()
        self.FRI_temp = tk.Label(self.FRI_frame, text='5°C 0°C', font=SMOLL_FONT).pack()

        self.SAT_frame = tk.Frame(self)
        self.SAT_day = tk.Label(self.SAT_frame, text='Monday', font=SMOLL_FONT).pack()
        self.SAT_img = tk.Label(self.SAT_frame, image=self.temp_img).pack()
        self.SAT_temp = tk.Label(self.SAT_frame, text='5°C 0°C', font=SMOLL_FONT).pack()

        self.SUN_frame = tk.Frame(self)
        self.SUN_day = tk.Label(self.SUN_frame, text='Monday', font=SMOLL_FONT).pack()
        self.SUN_img = tk.Label(self.SUN_frame, image=self.temp_img).pack()
        self.SUN_temp = tk.Label(self.SUN_frame, text='5°C 0°C', font=SMOLL_FONT).pack()

#
        self.MON_frame.grid(row=0, column=0, padx=20)
        self.TUE_frame.grid(row=0, column=1, padx=20)
        self.WED_frame.grid(row=0, column=2, padx=20)
        self.THU_frame.grid(row=0, column=3, padx=20)
        self.FRI_frame.grid(row=0, column=4, padx=20)
        self.SAT_frame.grid(row=0, column=5, padx=20)
        self.SUN_frame.grid(row=0, column=6, padx=20)


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