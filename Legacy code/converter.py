import re

def process(lenght, width):
    def extract(strin):
        rex = re.compile("(\d+)°(\d+)′(\d+)″([A-Z])")
        match = re.match(rex, strin)
        data = match.groups()

        hours = float(data[0])
        minutes = (float(data[1]) * 100) / 6000
        seconds = (float(data[2]) * 100) / 360000

        val = hours + seconds + minutes
        if data[3] == 'S' or data[3] == 'W':
            return -val

        return val

    lenght = extract(lenght)
    width = extract(width)
    return lenght, width
