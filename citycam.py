# app that scrapes the last 24 hours of various weatherbug city cameras at 5 minute intervals.
# TO DO: 
# add more citycodes
import os, sys
import requests
import random
import time
import datetime



hour = 00
minute = 00
"{:02d}".format(minute)
"{:02d}".format(hour)
now = datetime.datetime.now()
# print ("Current year: %d" % now.year)
# print ("Current month: %d" % now.month)
# print ("Current day: %d" % now.day)
yesterday = now.day - 1
day = yesterday
month = now.month
year = now.year
blankcount = 0
cityCode = 0
total = 0

def getInput():
	print("Select a camera capture feed:")
	pickcam = int (input ("1. USC Skyline\t2. San Francisco\n3. Cincinatti\t4. Indianapolis\n5. Gettysburg\t6. St. Mary's, Chicago\n7. Houston\t8. Cedar Point Park, Ohio\n") )
	if pickcam == 1:
		cityCode = 'LSN01'
	elif pickcam == 2:
		cityCode = 'SANFR'
	elif pickcam == 3:
		cityCode = 'WLWTT'
	elif pickcam == 4:
		cityCode = 'INDLS'
	elif pickcam == 5:
		cityCode = 'GTTGB'
	elif pickcam == 6:
		cityCode = 'CHCMV'
	elif pickcam == 7:
		cityCode = 'ABTTX'		
	elif pickcam == 8:
		cityCode = 'SADKY'


	else:
		while True:
			print("FUCK YOU") 
	return(cityCode)


cityCode = getInput()
curdir = "./" + str(cityCode)
os.system('rm -rf ' + curdir)
os.mkdir( curdir)
if os.path.isdir(curdir):
	print("This directory exists. Overwrite it?")
	decisions = str (input ("Type Y or N\n"))
	if decisions.lower() == "n":
		exit()
	else:
		pass
while True:
	"{:02d}".format(hour)
	"{:02d}".format(minute)
	if minute >= 55:
		minute = 00
		#print("RESTART, minute at " + str("{:02d}".format(minute)))
		hour = hour + 1
	if hour > 24:
		day = now.day
	#print("hour: " + str("{:02d}".format(hour)))	
	#print("minute: " + str("{:02d}".format(minute)))	
	timestamp = str("{:02d}".format(month)) + str("{:02d}".format(day)) + str("{:02d}".format(year)) + str("{:02d}".format(hour)) + str("{:02d}".format(minute))  
	url = "https://cameras-cam.cdn.weatherbug.net/" + cityCode + "/" + str("{:02d}".format(year)) + "/" + str("{:02d}".format(month)) + "/" + str("{:02d}".format(day))+ "/" + timestamp + "_l.jpg"
	#print(url)
	r = requests.get(url, allow_redirects=True)
	open(curdir + "/" + cityCode + str(timestamp) + '.jpg', 'wb').write(r.content)
	b = os.path.getsize(curdir + "/" + cityCode + str(timestamp) + '.jpg')
	#print("file size: " + str(b))
	#if filesize is smaller than 300 bytes, delete it
	if b < 300:
		blankcount += 1
		os.remove(curdir + "/" + cityCode + str(timestamp) + '.jpg')
		#print("blank image")
	else:
		total += 1
		print("writing " + curdir + '/' + str(timestamp) + ".jpg" + " | " + "hour: " + str("{:02d}".format(hour)) + " minute: " + str("{:02d}".format(minute)) + " | Total images: " + str(total), end="\r")
		blankcount = 0

	##if there are 3 empty images in a row, quit
	if blankcount > 30:
		print("Looks like that's all the images for the past 24 hours. Quitting..")
		break
	if cityCode == 'ABTTX':
		minute = minute + 1
	if cityCode != 'ABTTX':
		minute = minute + 5

	