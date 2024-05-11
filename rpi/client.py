import requests

class Backend:

    def __init__(self, base_url):
        self.base_url = base_url
    
    def save_value(self, sensor, value):
        try:
            requests.post(f'{self.base_url}/save_value/{sensor}/{value}')
        except:
            pass
