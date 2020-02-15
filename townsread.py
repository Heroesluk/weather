import csv

def towns():
    with open('worldcities.csv', 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        data = []

        for row in csv_reader:
            data.append(row)

    cites = [i[1] for i in data]
    latitiude = [i[2] for i in data]
    longitiude = [i[3] for i in data]

    lat_long = zip(latitiude, longitiude)
    city_cord = dict(zip(cites, lat_long))

    return city_cord


city_cord = towns()
print(city_cord)