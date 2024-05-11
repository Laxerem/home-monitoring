import json

def read_config():
    file = open("config.json")
    dictionary = json.load(file)
    file.close()
    return dictionary