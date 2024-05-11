devices_dir = "/sys/bus/w1/devices"

def read_temp(device_id):
    file = open(f'{devices_dir}/{device_id}/temperature')
    value = int(file.readline().strip())
    value /= 1000
    file.close()
    return value

