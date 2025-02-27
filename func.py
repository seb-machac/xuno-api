import json #imports




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    global vsv
    global database
    global data
    global days
    global periodnum

    database = "timetable.json"
    data = json.loads(open(database).read())
    vsv = False

    days = {
        "monday": 0, "mon": 0,
        "tuesday": 1, "tue": 1,
        "wednesday": 2, "wed": 2,
        "thursday": 3, "thu": 3,
        "friday": 4, "fri": 4,
    }

    day = days.get(input("What day? ").strip().lower(), 5)

    periodinput = input("What period? ") #asks for period


    if int(periodinput) < 7:
        periodnum = int(periodinput) - 1
    else:
        periodnum = 6


    if "description" in data["data"]["dates"][day]["periods"][periodnum]["timetables"][0]:
        print(data["data"]["dates"][day]["periods"][periodnum]["programs"][0]["name"])
        print(data["data"]["dates"][day]["periods"][periodnum]["programs"][0]["room_name"])
        vsv = True
    else:
        isvsv = False
        if day != 5 and periodnum < 6 and vsv == False:
            print(data["data"]["dates"][day]["periods"][periodnum]["className"])
            print(data["data"]["dates"][day]["periods"][periodnum]["timetables"][0]["timetable"]["roomlist"])
        elif vsv == False:
            print("Not a valid day")