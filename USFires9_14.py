import json

infile = open("US_fires_9_14.json", "r")

fires9_14 = json.load(infile)

lats, lons, brightness = [], [], []

lats = [
    fires9_14[x]["latitude"]
    for x in range(len(fires9_14))
    if fires9_14[x]["brightness"] > 450
]
lons = [
    fires9_14[x]["longitude"]
    for x in range(len(fires9_14))
    if fires9_14[x]["brightness"] > 450
]
brightness = [
    fires9_14[x]["brightness"]
    for x in range(len(fires9_14))
    if fires9_14[x]["brightness"] > 450
]

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": brightness,
        "marker": {
            "size": 10,
            "color": brightness,
            "colorscale": "viridis",
            "reversescale": True,
            "colorbar": {"title": "brightness"},
        },
    }
]

my_layout = Layout(title="US Fires 9/14/2020 through 9/120/2020")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="US_fires_9_14.html")
