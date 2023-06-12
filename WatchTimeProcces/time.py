# import main lib
import os

# import another main libs
try:
	import json

except Exception as e:
	os.system("pip install json")
	exit()

# check exists data file
if not os.path.exists("data.json"):
	exit("data.json doesn`t exist")

proccesses = json.loads(open("data.json", "r").read())

for proccess in proccesses:
	name = proccess
	time = proccesses[proccess]["all_time"]

	h = time // 60 // 60
	m = (time - h * 60 * 60) // 60
	s = time - h * 60 * 60 - m * 60

	time = f"{h} часов {m} минут {s} секунд"

	print(f"Процесс: {name}\nВремя: {time}\n")