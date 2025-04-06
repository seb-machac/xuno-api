import json #imports


def GetClass():
    global vsv
    global database
    global data
    global days
    global periodnum # all of the global variables are defined

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

    day = days.get(input("What day? ").strip().lower(), 5) #asks for day

    periodinput = input("What period? ") #asks for period

    #all of the variables are set


    if int(periodinput) < 7:
        periodnum = int(periodinput) - 1
    else:
        periodnum = 6 #sets period number


    if "description" in data["data"]["dates"][day]["periods"][periodnum]["timetables"][0]: #checks if period is vsv
        print(data["data"]["dates"][day]["periods"][periodnum]["programs"][0]["name"])
        print(data["data"]["dates"][day]["periods"][periodnum]["programs"][0]["room_name"]) #prints vsv data
        vsv = True
    else:
        isvsv = False
        if day != 5 and periodnum < 6 and vsv == False: #gets and prints current class
            print(data["data"]["dates"][day]["periods"][periodnum]["className"])
            print(data["data"]["dates"][day]["periods"][periodnum]["timetables"][0]["timetable"]["roomlist"])
            classname = data["data"]["dates"][day]["periods"][periodnum]["className"]
            return classname
        elif vsv == False:
            print("Not a valid day")