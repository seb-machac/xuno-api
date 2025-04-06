#-------------------------------------------------                                                                 Importing section
import json
from tkinter import *

#-------------------------------------------------                                                                 Defining variable section
window = Tk()
window.title("main")
window.geometry("120x150")

database = "timetable.json"
data = json.loads(open("timetable.json").read())                                                                   #Parses json file

DayVar = StringVar()                                                                                               #Defines DayVar and PeriodVar as strings
PeriodVar = StringVar()

days = {"monday": 0, "mon": 0,                                                                                     #Connect day strings to corresponding integers
        "tuesday": 1, "tue": 1,
        "wednesday": 2, "wed": 2,
        "thursday": 3, "thu": 3,
        "friday": 4, "fri": 4,}

#-------------------------------------------------                                                                 Main function section

def GetClass():

    global vsv
    vsv = False

    day = days.get(DayVar.get().strip().lower(), 5)                                                                #Gets DayVar from entry and sets it to day

    period = int(PeriodVar.get())                                                                                  #Get PeriodVar from entry and sets it to period

    if period - 1 < 6:
        pass                                                                                                       #Exits if statement if valid day
    else:
        period = 5                                                                                                 #Sets period number as 5 if not valid day

    if "description" in data["data"]["dates"][day]["periods"][period - 1]["timetables"][0]:                        #Checks if period is vsv
        print(data["data"]["dates"][day]["periods"][period - 1]["programs"][0]["name"])
        print(data["data"]["dates"][day]["periods"][period - 1]["programs"][0]["room_name"])                       #Prints vsv data
        vsv = True
    else:
        if period - 1 < 6 and vsv == False:                                                                        #Gets and prints current class
            print(data["data"]["dates"][day]["periods"][period - 1]["className"])
            print(data["data"]["dates"][day]["periods"][period - 1]["timetables"][0]["timetable"]["roomlist"])
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
                 fg="grey",
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
                    fg="grey",
                    #justify=
                    relief=FLAT,
                    show="",
                    textvariable=PeriodVar)



GetClassButton = Button(window,                                                                                    #Creates a Get Class Button
                        text="click",
                        command=GetClass)


DayLabel.grid(column=1, row=1)                                                                                     #Initialises DayLabel
DayEntry.grid(column=1, row=2, pady = (0,0))                                                                       #Initialises DayEntry

PeriodLabel.grid(column=1, row=3, pady = (10,0))                                                                   #Initialises PeriodLabel
PeriodEntry.grid(column=1, row=4, pady = (0,0))                                                                    #Initialises PeriodEntry

GetClassButton.grid(column=1, row=5)                                                                               #Initialises GetClassButton

window.mainloop()                                                                                                  #Starts the mainloop