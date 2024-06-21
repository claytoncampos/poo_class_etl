from class_etl import Collector

url = "https://pokeapi.co/api/v2/pokemon"
instance_name = "pokemon"
collector = Collector(url, instance_name)
collector.auto_exec()
