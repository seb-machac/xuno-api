#-------------------------------------------------                                                                 Importing section
import json
from tkinter import *

#-------------------------------------------------                                                                 Defining variable section
window = Tk()
window.title("main")
window.geometry("120x200")

database = "timetable.json"
data = json.loads(open("timetable.json").read())                                                                   #Parses json file

DayVar = StringVar()                                                                                               #Defines DayVar and PeriodVar as strings
PeriodVar = StringVar()

days = {"monday": 0, "mon": 0,                                                                                     #Connect day strings to corresponding integers
        "tuesday": 1, "tue": 1,
        "wednesday": 2, "wed": 2,
        "thursday": 3, "thu": 3,
        "friday": 4, "fri": 4,}
ClassName = "none"
ClassRoom = "none"
#-------------------------------------------------                                                                 Main function section

def GetClass():
    global ClassName
    global ClassRoom
    global vsv
    vsv = False

    day = days.get(DayVar.get().strip().lower(), 5)                                                                #Gets DayVar from entry and sets it to day

    period = int(PeriodVar.get())                                                                                  #Get PeriodVar from entry and sets it to period

    if period - 1 < 6:
        pass                                                                                                       #Exits if statement if valid day
    else:
        return                                                                                                     #Exits function if not a valid period

    if "description" in data["data"]["dates"][day]["periods"][period - 1]["timetables"][0]:                        #Checks if period is vsv
        ClassName = data["data"]["dates"][day]["periods"][period - 1]["programs"][0]["name"]
        ClassRoom = data["data"]["dates"][day]["periods"][period - 1]["programs"][0]["room_name"]                  #Prints vsv data
        ClassNameLabel.config(text= ClassName)
        ClassRoomLabel.config(text= ClassRoom)

    else:
        if period - 1 < 6 and vsv == False:                                                                        #Gets and prints current class
            ClassName = data["data"]["dates"][day]["periods"][period - 1]["className"]
            ClassRoom = data["data"]["dates"][day]["periods"][period - 1]["timetables"][0]["timetable"]["roomlist"]
            ClassNameLabel.config(text= ClassName)
            ClassRoomLabel.config(text= ClassRoom)
        elif vsv == False:
            print("Not a valid day")


#-------------------------------------------------                                                                 Tkinter section


DayLabel = Label(window,                                                                                           #Creates a Day label
                 bg="White",
                 fg="Black",
                 text="Enter Day:")


DayEntry = Entry(window,                                                                                           #Creates a Day entry
                 bg="White",
                 bd=2,
                 #font=
                 fg="Black",
                 #justify=
                 relief=FLAT,
                 show="",
                 textvariable=DayVar)



PeriodLabel = Label(window,                                                                                        #Creates a Period label
                 bg="White",
                 fg="Black",
                 text="Enter Period:")

PeriodEntry = Entry(window,                                                                                        #Creates a Period entry
                    bg="White",
                    bd=2,
                    #font=
                    fg="Black",
                    #justify=
                    relief=FLAT,
                    show="",
                    textvariable=PeriodVar)



GetClassButton = Button(window,                                                                                    #Creates a Get Class Button
                        text="click",
                        command=GetClass)

ClassNameLabel = Label(window,                                                                                        #Creates a Period label
                 bg="White",
                 fg="Black",
                 text=ClassName)

ClassRoomLabel = Label(window,                                                                                        #Creates a Period label
                 bg="White",
                 fg="Black",
                 text=ClassRoom)

DayLabel.grid(column=1, row=1)                                                                                     #Initialises DayLabel
DayEntry.grid(column=1, row=2, pady = (0,0))                                                                       #Initialises DayEntry

PeriodLabel.grid(column=1, row=3, pady = (10,0))                                                                   #Initialises PeriodLabel
PeriodEntry.grid(column=1, row=4, pady = (0,0))                                                                    #Initialises PeriodEntry

GetClassButton.grid(column=1, row=5)                                                                               #Initialises GetClassButton

ClassNameLabel.grid(column=1, row=6, pady = (10,0))
ClassRoomLabel.grid(column=1, row=7, pady = (0,0))

window.mainloop()                                                                                                  #Starts the mainloop