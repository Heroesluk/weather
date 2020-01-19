# live obrazek o godzinie
from tkinter import *
from tkinter.font import Font
from scrapper import find_cord
from converter import process
from api_data_parser import get_data

lenght = '51.776666666666664'
width = '19.454722222222223'

weath_data = get_data(lenght, width)

root = Tk()
root.geometry('1600x900')

def ini(root):
    # Weather Section

    weather_font = Font(family='Courier bold', size=24)
    weather_frame = Frame(root)
    weather_frame.grid(row=1, column=0)

    #    # temperature section
    temp_frame = Frame(weather_frame)

    temperature_text = Label(temp_frame, text='Temperatura wynosi: ', font=weather_font)
    temperature_display = Label(temp_frame, text=str(int(weath_data['temperature'])) + '°C', font='Courier 48 bold')

    temperature_text.grid(row=0, column=0)
    temperature_display.grid(row=1, column=0)

    #    # summary section
    sum_frame = Frame(weather_frame)

    summary_text = Label(sum_frame, text=weath_data['summary'], font=weather_font)
    sum_img = PhotoImage(file='overcast.gif')
    summary_img = Label(sum_frame, image=sum_img)

    summary_text.grid(row=0, column=0)
    summary_img.grid(row=1, column=0)

    #    # wind section
    wind_frame = Frame(weather_frame)

    wind_speed = Label(wind_frame, text='Predkosc wiatru: ' + str(weath_data['windSpeed']) + 'Km/H')
    wind_gust = Label(wind_frame, text='Porywy Wiatru do: ' + str(weath_data['windGust']) + 'Km/H')

    wind_speed.grid(row=0, column=0)
    wind_gust.grid(row=1, column=0)

    temp_frame.grid(row=0, column=0)
    sum_frame.grid(row=0, column=1)
    wind_frame.grid(row=0, column=2)
ini(root)

def dummy(town):
    try:
        global lenght
        global width
        global weath_data
        lenght_raw, width_raw = find_cord(town)
        lenght, width = process(lenght_raw, width_raw)
        print(lenght, width, town)
        weath_data = get_data(lenght, width)
        ini(root)

    except TypeError:
        print('niepoprawny')


# Town Frame section
def_font = Font(family='Arial', size=24)

town_frame = Frame(root, bg='blue')
town_frame.grid(row=0, column=0)
town = StringVar()

text_label = Label(town_frame, text='Podaj miasto dla którego chcesz poznać pogodę', font=def_font)
entry_town = Entry(town_frame, textvariable=town, font='Helvetica 44 bold', width=13)
send_butt = Button(town_frame, text='confirm', command=lambda: dummy(entry_town.get()), font='Helvetica 24 bold')
town_list = Listbox(town_frame, height=10)

text_label.grid(columnspan=2, row=0, ipady=10)
entry_town.grid(column=0, row=1, sticky=W + E + N + S)
send_butt.grid(column=1, row=1, sticky=W + E + N + S)
town_list.grid(column=0, row=2, sticky=W + E + N + S)

town_frame.grid_columnconfigure(0, weight=0)
town_frame.grid_columnconfigure(1, weight=1)




root.mainloop()
