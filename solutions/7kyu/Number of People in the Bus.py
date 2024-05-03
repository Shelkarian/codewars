def number(bus_stops):
    enter = 0
    exit = 0
    for i in bus_stops:
        enter += i[0]
        exit += i[1]

    return enter - exit