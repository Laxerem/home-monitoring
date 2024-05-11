import time
from temp import read_temp
from util import read_config
from client import Backend

config = read_config()
sensors = config["sensors"]
backend_url = config["backend_url"]
delay = config["delay"]

client = Backend(backend_url)

while True:
    for sensor in sensors:
        value = read_temp(sensor)
        client.save_value(sensor, value)
    time.sleep(delay)
