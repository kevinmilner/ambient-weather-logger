#!/usr/bin/env python3

from ambient_api.ambientapi import AmbientAPI
import os, sys
import time
import csv

if len(sys.argv) != 2:
	print("usage: <output-dir>")
	sys.exit(1)

outDir = sys.argv[1]
if not os.path.isdir(outDir):
	os.mkdir(outDir)

if not ("AMBIENT_ENDPOINT" in os.environ):
	print("must set AMBIENT_ENDPOINT environmental variable!")
	sys.exit(1)
if not ("AMBIENT_API_KEY" in os.environ):
	print("must set AMBIENT_API_KEY environmental variable!")
	sys.exit(1)
if not ("AMBIENT_APPLICATION_KEY" in os.environ):
	print("must set AMBIENT_APPLICATION_KEY environmental variable!")
	sys.exit(1)

api = AmbientAPI(log_level='CONSOLE')

devices = api.get_devices()

print("Loaded "+str(len(devices))+" devices")

if len(devices) < 1:
	print("no devices found, inspect output above")
	sys.exit(1)

for device in devices:
	print(device)
	lastData = device.last_data
	date = lastData["dateutc"]
	print("Last date: "+str(date))
	myDir = outDir
	if len(devices) > 1:
		myDir = outDir+"/"+str(device.mac_address).replace(":","")
	for field in lastData:
		if field == "dateutc" or field == "tz" or field == "date" or field == "lastRain" or field == "yearlyrainin" or field == "monthlyrainin" or field == "weeklyrainin":
			continue
		value = lastData[field]
		print(field+": "+str(value))
		fName = myDir+"/"+field+".csv"
		with open(fName, 'a', newline='') as csvfile:
			writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
			writer.writerow([date,value])

