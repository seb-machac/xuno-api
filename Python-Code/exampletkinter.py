import time
import json


database = "timetable.json"
data = json.loads(open("timetable.json").read()) 
day = 0
period = 0
times = 1748141738.6596377
U = time.strftime("%c", times.localtime())
W = time.localtime(1748141738.6596377)

print(U)
print(W)


periods = {
    
}