import pystray
from PIL import Image
import GUI
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

image = Image.open("assets/Xuno.png")

def GetCurrentClass():
    GUI.ManualInput = False
    lambda icon, item: icon.notify('Hello World!')
    print("Hello World")

def InputClass():
    ManualInput = True
    GUI.window.mainloop()

    elif str(query) == "Input Class":
        GUI.window.mainloop()

    elif str(query) == "Exit":
        icon.stop()


icon = pystray.Icon("Timetable", image, "Current Class:", 
					menu=pystray.Menu( 
    pystray.MenuItem("Get current class", GetCurrentClass),
	pystray.MenuItem("Input Class", lambda: GUI.window.mainloop()),
	pystray.MenuItem("Exit", lambda: icon.stop())))


icon.run()