import os, json
def getHeartRate():
	mapping = {}
	heartRateFiles = [i for i in os.listdir('KamranChoudhry/user-site-export/HR/') if i.endswith("json")]
	for file in heartRateFiles:
		dateArr = [] ; bpmArr = []
		fileName = str(file)
		date = fileName[11:-5]
		pathToFile = 'KamranChoudhry/user-site-export/HR/' + fileName
		with open(pathToFile) as jsonFile:
			data = json.load(jsonFile)
			for entry in data:
				dateArr.append(entry['dateTime'])
				bpmArr.append(entry['value']['bpm'])
			mapping[date] = [dateArr, bpmArr]

	return mapping

mapping = getHeartRate()							# returns hr for all files
print(mapping)