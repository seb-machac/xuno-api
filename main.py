import json #imports

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

database = "timetable.json"
data = json.loads(open(database).read()) #setup json reading

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

vsv = False #define variables

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(day, periodnum):
    if "description" in data["data"]["dates"][day]["periods"][periodnum]:
        print(data["data"]["dates"][day]["periods"][periodnum]["programs"][0]["name"])
        print(data["data"]["dates"][day]["periods"][periodnum]["programs"][0]["room_name"])
        vsv = True
    else:
        isvsv = False
        notvsv(day, periodnum)

#----------------------------------------------------------------------------------------------

def notvsv(day, periodnum):
    if day != 5 and periodnum < 6 and vsv == False:
        print(data["data"]["dates"][day]["periods"][periodnum]["className"])
        print(data["data"]["dates"][day]["periods"][periodnum]["timetables"][0]["timetable"]["roomlist"])
    elif vsv == False:
        print("Not a valid day")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dayinput = input("What day? ").strip().lower()  # asks for day, removes leading/trailing spaces, and converts to lowercase

days = {
    "monday": 0, "mon": 0,
    "tuesday": 1, "tue": 1,
    "wednesday": 2, "wed": 2,
    "thursday": 3, "thu": 3,
    "friday": 4, "fri": 4,
}

day = days.get(dayinput, 5)  # default to 5 if input is not recognized

#----------------------------------------------------------------------------------------------

periodinput = input("What period? ") #asks for period

if int(periodinput) < 7:
    periodnum = int(periodinput) - 1
else:
    periodnum = 6


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

main(day, periodnum) #main function

