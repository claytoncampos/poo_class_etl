import requests
import datetime
import json
import os
import urllib3


class Collector:

    def __init__(self, url, instance_name):
        self.url = url
        self.instance = instance_name

    def get_endpoint(self, **kwargs):
        urllib3.disable_warnings()
        resp = requests.get(self.url, verify=False, params=kwargs)
        return resp

    def save_data(self, data):
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")
        data["ingestion_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # if not ex  os.mkdir(f'{os.path.abspath("")}/{self.instance}')
        filename = f'{os.path.abspath("")}/{self.instance}/{now}.json'
        with open(filename, "w") as open_file:
            json.dump(data, open_file)

    def get_and_save(self, **kwargs):
        resp = self.get_endpoint(**kwargs)
        if resp.status_code == 200:
            data = resp.json()
            self.save_data(data)
            return data
        else:
            return {}

    def auto_exec(self, limit=100):
        offset = 0
        while True:
            data = self.get_and_save(limit=limit, offset=offset)

            if data["next"] == None:
                break

            offset += limit


# url = "https://pokeapi.co/api/v2/pokemon"
# instance_name = "pokemon"
# collector = Collector(url, instance_name)
# collector.auto_exec()
