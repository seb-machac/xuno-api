#-------------------------------------------------                                                                 Importing section
import json
from tkinter import *
from tkinter import ttk
import time

#-------------------------------------------------                                                                 Defining variable section
window = Tk()
window.title("main")
window.geometry("120x200")

database = "timetable.json"
data = json.loads(open("timetable.json").read())                                                                   #Parses json file


DayComboboxVars = StringVar()
PeriodComboboxVars = StringVar()


PeriodLinker = {"Period 1": 0,
              "Period 2": 1,
              "Period 3": 2,
              "Period 4": 3,
              "Period 5": 4,
              "Period 6": 5}

DayLinker = {"Monday": 0,                                                                                          #Connect day strings to corresponding integers
             "Tuesday": 1,
             "Wednesday": 2,
             "Thursday": 3,
             "Friday": 4}

DaysCombo = ("Monday",
		     "Tuesday",
		     "Wednesday",
		     "Thursday",
		     "Friday")

PeriodsCombo = ("Period 1",
                "Period 2",
                "Period 3",
                "Period 4",
                "Period 5",
                "Period 6")

ClassName = "none"
ClassRoom = "none"
vsv = False
ManualInput = False
#-------------------------------------------------                                                                 Main function section
def GetTime():
    day = int(time.strftime("%u",time.localtime())) - 1
    #period = 

def GetClass(day, period):
    global ClassName
    global ClassRoom
    global vsv
    global ManualInput


    if "description" in data["data"]["dates"][day]["periods"][period]["timetables"][0]:                            #Checks if period is vsv
        ClassName = data["data"]["dates"][day]["periods"][period]["programs"][0]["name"]
        ClassRoom = data["data"]["dates"][day]["periods"][period]["programs"][0]["room_name"]                      #Prints vsv data
        if __name__ == '__main__':
            ClassNameLabel.config(text= ClassName)
            ClassRoomLabel.config(text= ClassRoom)
        else:
            if ManualInput == True:
                ClassNameLabel.config(text= ClassName)
                ClassRoomLabel.config(text= ClassRoom)

    else:                                                                                                          #Gets and prints current class
            ClassName = data["data"]["dates"][day]["periods"][period]["className"]
            ClassRoom = data["data"]["dates"][day]["periods"][period]["timetables"][0]["timetable"]["roomlist"]
            ClassNameLabel.config(text= ClassName)
            ClassRoomLabel.config(text= ClassRoom)


#-------------------------------------------------                                                                 Tkinter section


DayLabel = Label(window,                                                                                           #Creates a Day label
                 bg="White",
                 fg="Black",
                 text="Enter Day:")


DayCombobox = ttk.Combobox(window, 
                           state= "readonly", 
                           values=DaysCombo, 
                           textvariable=DayComboboxVars) 

PeriodLabel = Label(window,                                                                                        #Creates a Period label
                 bg="White",
                 fg="Black",
                 text="Enter Period:")

PeriodCombobox = ttk.Combobox(window, 
                              state= "readonly", 
                              values=PeriodsCombo, 
                              textvariable=PeriodComboboxVars) 




GetClassButton = Button(window,                                                                                    #Creates a Get Class Button
                        text="click",
                        command= 
                        lambda: GetClass(DayLinker.get(DayComboboxVars.get(), 5), 
                                         PeriodLinker.get(PeriodComboboxVars.get(), 5)))

ClassNameLabel = Label(window,                                                                                     #Creates a Period label
                 bg="White",
                 fg="Black",
                 text=ClassName)

ClassRoomLabel = Label(window,                                                                                     #Creates a Period label
                 bg="White",
                 fg="Black",
                 text=ClassRoom)

DayLabel.grid(column=1, 
              row=1)                                                                                               #Initialises DayLabel

DayCombobox.grid(column=1, 
                 row=2, 
                 pady = (0,0))                                                                                     #Initialises DayEntry

PeriodLabel.grid(column=1, 
                 row=3, 
                 pady = (10,0))                                                                                    #Initialises PeriodLabel

PeriodCombobox.grid(column=1, 
                    row=4, 
                    pady = (0,0))                                                                                  #Initialises PeriodEntry

GetClassButton.grid(column=1, 
                    row=5)                                                                                         #Initialises GetClassButton

ClassNameLabel.grid(column=1, 
                    row=6, 
                    pady = (10,0))

ClassRoomLabel.grid(column=1, 
                    row=7, 
                    pady = (0,0))

if __name__ == '__main__':                                                                                         #Checks if script is run as main file or imported as a library
    window.mainloop()                                                                                              #if file was ran as main script then initialise the root window