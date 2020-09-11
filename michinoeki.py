import json
from pprint import pprint
import pandas as pd
import folium

m = folium.Map(location=[43.06417, 141.34694], zoom_start=6)

df = pd.read_json(
    r"C:\Users\113414A009MEH\Documents\dev\intro_michinoeki\Roadside_Stationhokkaido.json",
    encoding="utf-8")

df_f = df["features"]

for data in df_f:
    d = data["properties"]
    folium.Marker(
        [d["P35_001"], d["P35_002"]],
        popup=folium.Popup(d["P35_006"], max_width=200)).add_to(m)

m.save("michinoekimap.html")
