import json

with open("config.json") as config_data:
	data = json.load(config_data)

def config(paramName):
	return data[paramName];