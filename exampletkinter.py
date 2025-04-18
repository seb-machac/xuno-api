import pystray
from PIL import Image



image = Image.open("assets/Xuno.png")

def GetCurrentClass():
    icon.notify('Hello World!')

icon = pystray.Icon("Timetable", image, "GeeksforGeeks", 
					menu=pystray.Menu( 
    pystray.MenuItem("Get current class", GetCurrentClass),
	pystray.MenuItem("Exit", lambda: icon.stop())))


icon.run()