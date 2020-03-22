#!/usr/bin/env python3
# python3 app that scrapes the last 24 hours of various weatherbug city cameras at 5 minute intervals.

import os, sys
import requests
import random
import time
import datetime





# cityCode = getInput()


        
    # os.system('del ' + curdir)
def getimgs(cityCode,curdir):
    hour = 00
    minute = 00
    "{:02d}".format(minute)
    "{:02d}".format(hour)
    now = datetime.datetime.now()
    yesterday = now.day - 1
    day = yesterday
    month = now.month
    year = now.year
    blankcount = 0
    # cityCode = 0
    total = 0
    while True:
        "{:02d}".format(hour)
        "{:02d}".format(minute)
        if minute >= 55:
            minute = 00
            hour = hour + 1
        if hour > 24:
            day = now.day
        timestamp = str("{:02d}".format(month)) + str("{:02d}".format(day)) + str("{:02d}".format(year)) + str("{:02d}".format(hour)) + str("{:02d}".format(minute))  
        url = "https://cameras-cam.cdn.weatherbug.net/" + cityCode + "/" + str("{:02d}".format(year)) + "/" + str("{:02d}".format(month)) + "/" + str("{:02d}".format(day))+ "/" + timestamp + "_l.jpg"
        r = requests.get(url, allow_redirects=True)
        open(curdir + "/" + cityCode + str(timestamp) + '.jpg', 'wb').write(r.content)
        b = os.path.getsize(curdir + "/" + cityCode + str(timestamp) + '.jpg')
        #if filesize is smaller than 300 bytes, delete it
        if b < 300:
            blankcount += 1
            os.remove(curdir + "/" + cityCode + str(timestamp) + '.jpg')
        else:
            total += 1
            print("writing " + curdir + '/' + str(timestamp) + ".jpg" + " | " + "hour: " + str("{:02d}".format(hour)) + " minute: " + str("{:02d}".format(minute)) + " | Total images: " + str(total), end="\r")
            blankcount = 0

        ##if there are 3 empty images in a row, quit
        if blankcount > 30:
            print("\nLooks like that's all the images for the past 24 hours. Quitting...\n")
            break
        if cityCode == 'ABTTX':
            minute = minute + 1
        if cityCode != 'ABTTX':
            minute = minute + 5


cityCodes = ['GTTGB', 'WLWTT', 'GLVSC']
# cityCode = 'GTTGB'

for cityCode in cityCodes:
    #check if directory exists
    curdir = "./" + str(cityCode)
    if os.path.isdir(curdir) == False:
        print("curdir false")
        os.mkdir(curdir)
    else:
        print("curdir true")
    print(cityCode)
    getimgs(cityCode, curdir)
