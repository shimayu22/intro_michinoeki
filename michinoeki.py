import json
from pprint import pprint
import pandas as pd


with open(r"C:\Users\113414A009MEH\Documents\dev\intro_michinoeki\Roadside_Stationhokkaido.json", encoding="utf-8") as f:
    s = f.read()

jsondata = json.loads(s)

for data in jsondata["features"]:
    print(data["properties"]["P35_006"])

print(len(jsondata["features"]))
