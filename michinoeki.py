import json
from pprint import pprint
import pandas as pd


df = pd.read_json(
    r"C:\Users\113414A009MEH\Documents\dev\intro_michinoeki\Roadside_Stationhokkaido.json",
    encoding="utf-8")

df_f = df["features"]

for d in df_f:
    print(f'{d["properties"]["P35_006"]} : {d["geometry"]["coordinates"]}')
