import requests
import folium



res=requests.get('https://ipinfo.io/')
data=res.json()
print(data)
location=data['loc'].split(',')
lat=float(location[1])
log=float(location[0])


fg=folium.FeatureGroup("my map")

fg.add_child(folium.Marker(location=[23.543522,52.570552],popup="Hospital 1"))
fg.add_child(folium.Marker(location=[23.435206,52.812251],popup="Hospital 2"))
fg.add_child(folium.Marker(location=[23.569958,52.343959],popup="Hospital 3"))


map=folium.Map(location=[23.543522,52.570552],zoom_start=7)
map=folium.Map(location=[23.435206,52.812251],zoom_start=7)
map=folium.Map(location=[23.569958,52.343959],zoom_start=7)

map.add_child(fg)
map.save("maps.html")

import webbrowser
webbrowser.open("maps.html")

