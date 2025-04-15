import json #imports


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

def ClassesInput():
    GetClasses(days.get(input("What day? ").strip().lower(), 5), int(input("What period? ")) - 1)
    
def GetClasses(day, period):
    
    vsv = False
    if "description" in data["data"]["dates"][day]["periods"][period]["timetables"][0]: #checks if period is vsv
        ClassName = data["data"]["dates"][day]["periods"][period]["programs"][0]["name"]
        ClassRoom = data["data"]["dates"][day]["periods"][period]["programs"][0]["room_name"]
        print(ClassName, ClassRoom) 
        vsv = True
    else:
        isvsv = False
        if day != 5 and period < 6 and vsv == False: #gets and prints current class
            ClassName = data["data"]["dates"][day]["periods"][period]["className"]
            ClassRoom = data["data"]["dates"][day]["periods"][period]["timetables"][0]["timetable"]["roomlist"]
            print(ClassName, ClassRoom)
            
        elif vsv == False:
            print("Not a valid day")

GetClasses(days.get(input("What day? ").strip().lower(), 5), int(input("What period? ")) - 1)
