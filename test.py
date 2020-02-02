import requests
import json
from datetime import date

link = 'https://api.darksky.net/forecast/7c53a90481bcc12e69c188a374ddae2d/51.7833,19.4667?units=si'


class Info():
    def __init__(self, link):
        self.link = link

    req = requests.get(link)
    data = req.json()

    days = [i for i in data['daily']['data']]  # list of day Json objects

    days_temp_High = [int(i['temperatureHigh']) for i in days]
    days_temp_Low = [int(i['temperatureLow']) for i in days]
    days_icon = [i['icon'] for i in days]

    week_days_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    day = date.today().weekday()
    week_days = []
    for i in range(7):
        try:
            week_days.append(week_days_dict[day])
        except KeyError:
            day = 0
            week_days.append(week_days_dict[day])
        day += 1


data_unit = Info(link)

for i in range(7):
    print('At {} highest temp will be {} and the lowest will be {}, and the weather summary is {}'.format(data_unit.week_days[i],
                                                                           data_unit.days_temp_High[i],
                                                                           data_unit.days_temp_Low[i],
                                                                           data_unit.days_icon[i]))
