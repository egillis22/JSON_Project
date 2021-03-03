import json

infile = open("US_fires_9_1.json", "r")

fires9_1 = json.load(infile)


lats = [
    fires9_1[x]["latitude"]
    for x in range(len(fires9_1))
    if fires9_1[x]["brightness"] > 450
]
lons = [
    fires9_1[x]["longitude"]
    for x in range(len(fires9_1))
    if fires9_1[x]["brightness"] > 450
]
brightness = [
    fires9_1[x]["brightness"]
    for x in range(len(fires9_1))
    if fires9_1[x]["brightness"] > 450
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

my_layout = Layout(title="US Fires 9/1/2020 through 9/13/2020")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="US_fires_9_1.html")
