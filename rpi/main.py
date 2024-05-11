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
        print(f"Считываю данные с датчика: {sensor}", end='')
        value = read_temp(sensor)
        print(".. ok")
        print("Отправление показаний в BackEnd", end='')
        client.save_value(sensor, value)
        print(".. ok")
    time.sleep(delay)
