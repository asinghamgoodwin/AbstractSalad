# our pure python file for manipulating data

perfectSaladRatios = {"Greens": 0.3,"Veggies":0.3,"Protein":0.2,"Dressing":0.1,"Other":0.1}

def calculateRatios(category_dict):
	ourSaladRatios = {}
	for category in category_dict.keys():
		ourSaladRatios[category]=len(category_dict[category])
	total = sum(ourSaladRatios.values())
	for category in category_dict.keys():
		ourSaladRatios[category] = ourSaladRatios[category]/float(total)
	return ourSaladRatios


def warnAboutRatios(perfectDict, ourDict):
	warnings = []
	for category in perfectDict.keys():
		if ourDict[category] < perfectDict[category]/2:
			warnings.append(category)
	return warnings