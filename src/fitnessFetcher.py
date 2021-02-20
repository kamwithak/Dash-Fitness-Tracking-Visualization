import os, json
from datetime import datetime

def collectHeartRateInformation():
	masterDict = {} ; dateOptions = []
	src = 'data/user-site-export/HR/'
	for file in os.listdir(src):
		dateArr = [] ; bpmArr = []
		date = file[11:21]
		with open(src + file) as jsonFile:
			data = json.load(jsonFile)
			for entry in data:
				dateArr.append(entry['dateTime'])
				bpmArr.append(int(entry['value']['bpm']))
		masterDict[date] = dateArr, bpmArr
	for key in sorted(masterDict):
		dateOptions.append({'label': key, 'value': key})
	return masterDict, dateOptions

def collectCaloricInformation():
	masterDict = {}
	src = 'data/user-site-export/CALORIES/'
	for file in os.listdir(src):
		with open(src + file) as jsonFile:
			data = json.load(jsonFile)
			for entry in data:
				dateTimeObj = datetime.strptime(entry['dateTime'][:8], "%m/%d/%y")
				curDate = dateTimeObj.strftime("%Y-%m-%d")
				dailyCalories = float(entry['value'])
				if (curDate not in masterDict):
					masterDict[curDate] = [dailyCalories]
				else:
					masterDict[curDate].append(dailyCalories)
	for key in masterDict:
		i = 0 ; tmp = 0
		while (i < len(masterDict[key])):
			tmp += float(masterDict[key][i])
			masterDict[key][i] = tmp
			i += 1
	for curDate in masterDict:
		masterDict[curDate] = max(masterDict[curDate])
	return masterDict

def collectDistanceInformation():
	masterDict = {}
	src = 'data/user-site-export/DISTANCE/'
	for file in os.listdir(src):
		with open(src + file) as jsonFile:
			data = json.load(jsonFile)
			for entry in data:
				dateTimeObj = datetime.strptime(entry['dateTime'][:8], "%m/%d/%y")
				curDate = dateTimeObj.strftime("%Y-%m-%d")
				dailyDistance = float(entry['value'])
				if (curDate not in masterDict):
					masterDict[curDate] = [dailyDistance]
				else:
					masterDict[curDate].append(dailyDistance)
	for key in masterDict:
		i = 0 ; tmp = 0
		while (i < len(masterDict[key])):
			tmp += float(masterDict[key][i])
			masterDict[key][i] = tmp
			i += 1
	for curDate in masterDict:
		masterDict[curDate] = max(masterDict[curDate])
	return masterDict

#x,y = collectHeartRateInformation()
#print(y)