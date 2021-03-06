import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data["features"]
mags, lons, lats = [], [], []
hovertext = []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    mags.append(mag)
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    lons.append(lon)
    lats.append(lat)
    hovertext = eq["properties"]["place"]
print(mags[:10])
print(lons[:10])
print(lats[:10])
print(hovertext[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hovertext,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "viridis",
            "reversescale": True,
            "colorbar": {"title": "magnitude"},
        },
    }
]

my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
