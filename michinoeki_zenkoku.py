import json
from pprint import pprint
import pandas as pd
import folium

m = folium.Map(location=[35.6809591, 139.7673068], zoom_start=5)

df = pd.read_json(
    r"C:\Users\113414A009MEH\Documents\dev\intro_michinoeki\P35-18_Roadside_Station.json",
    encoding="utf-8")

df_f = df["features"]

for data in df_f:
    d = data["properties"]
    folium.Marker(
        [d["P35_001"], d["P35_002"]],
        popup=d["P35_006"]).add_to(m)

m.save("michinoekizenkokumap.html")
