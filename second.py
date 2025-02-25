import json

database = "timetable.json"
data = json.loads(open(database).read())


if "description" in data["data"]["dates"][2]["periods"][1]:
    print("yes vsv")
else:
    print("no vsv")