#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

from subprocess import call
import urllib
import json
import calendar
import time


#device = "wlan0"
#temp = "wifistat.out"

def saveWifiStat(device, outputFileName):
    #retcode = call("date > {0}".format(outputfilename), shell=True)
    retcode = call("iwconfig {0} > {1}".format(device, outputFileName), shell=True)

def printWifiStat(outputFileName):
    fileWifiStat = open(outputFileName, "r")
    print(fileWifiStat.read())

def getWifiStat(outputFileName):
    fileWifiStat = open(outputFileName, "r")
    return fileWifiStat.read()

def firebaseSendData(outputFileName):
    url = 'https://mycooltemperatureapp.firebaseio.com/readings.json'
    postdata = {
        'date': str(calendar.timegm(time.gmtime())),
        'wifistat': str(getWifiStat(outputFileName))
    }
    print(postdata)

if __name__ == '__main__':
    saveWifiStat("wlan0", "wifistat.out")
    #printWifiStat(outputfilename)




