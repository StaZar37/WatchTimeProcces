# import all require libs
# import main lib
import os

# import another main libs
try:
	import psutil as p
	import random
	import time
	import json
	import datetime

except Exception:
	os.system("pip install psutil random time json datetime")
	print("\n\n !!! Script needs reload !!!")
	exit()

# mini config
pn = "Telegram.exe" # our proccess name - Explorer
pf = "data.json" # path to data file

# var for clear recenlty time in proccess info
cl = False

# check exists data file
if not os.path.exists("data.json"):
	# create data.json
	f = open(pf, "w")
	f.close()


try:
	rt = int(6) # render time, after in code this value will change to random, from x-5 to x

	def check():
		result = False
		for proc in p.process_iter(['name', 'pid']):
			# print(proc.info['name'])
			if proc.info['name'] == pn:
				result = True

		return result

	# start
	while True:
		if check():
			print("DETECTED")

			# f for read info
			f = open(pf, "r")
			data = json.loads(f.read())
			f.close()

			def get_delta(rt, ct): # rec_time, current_time
				return int(ct - rt)

			# edit data
			if pn in data:
				all_time = data[pn]["all_time"]

				if cl: # if cl is True then reset rec_time
					data[pn]["rec_time"] = datetime.datetime.now().timestamp()
			else:
				all_time = 0
				data[pn] = {
					"rec_time": datetime.datetime.now().timestamp(),
					"all_time": 0,
				}

			delta = get_delta(data[pn]["rec_time"], datetime.datetime.now().timestamp())

			data[pn]["all_time"] = all_time + delta
			data[pn]["rec_time"] = datetime.datetime.now().timestamp()

			# f for write info
			f = open(pf, "w")
			js = json.dumps(data, indent = 4) # Json String
			f.write(js)
			f.close()

			# cl is False to don`t reset rec_time to count all_time without borders ? : )
			cl = False
		else:
			print("NOT DETECTED")

			# cl is True to reset next rec_time
			cl = True

		time.sleep(random.randint(rt - 5, rt))

except KeyboardInterrupt:
	print("Turn off...")