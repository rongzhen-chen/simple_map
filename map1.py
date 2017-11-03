import folium as fl
import pandas as pd

def genColor(v):
    if v <= 1000:
        return "green"
    elif 1000 < v <= 3000:
        return "orange"
    else:
        return "red"

data=pd.read_csv('Volcanoes_USA.txt')

lat = list(data["LAT"])
lon = list(data["LON"])

elv = list(data["ELEV"])


map1 = fl.Map(location=(48.7767982,-121.8109970),zoom_start=10, tiles="OpenStreetMap")

fgv = fl.FeatureGroup(name = "Volcanoes_USA")
for lt, ln, el in zip(lat, lon, elv):
    fgv.add_child(fl.Marker(location = (lt,ln), popup = str(el)+" meters", icon = fl.Icon(color = genColor(el))))
    #fg.add_child(fl.Circle(location = (lt,ln), radius = 10000, popup = str(el), fill_opacity = 1, color = genColor(el), fill = True, fill_color = genColor(el)))

fgp = fl.FeatureGroup(name = "Population")
fgp.add_child(fl.GeoJson(data=open("world.json",'r',encoding='UTF-8-sig').read(),
 style_function=lambda x: {'fillColor':"green" if x['properties']['POP2005']<1E7
 else "orange" if 1E7 < x['properties']['POP2005'] < 2E7 else "red"}))

map1.add_child(fgv)
map1.add_child(fgp)

map1.add_child(fl.LayerControl())

map1.save("map1.html")
