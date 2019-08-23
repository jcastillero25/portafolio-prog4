import requests
import time
import urllib
import webbrowser

resp = requests.get("http://api.open-notify.org/iss-now.json")
print(resp.status_code)
data = resp.json()
lat = (data['iss_position']['latitude'])
print(lat)
long = (data['iss_position']['longitude'])
print(long)
#print(data['iss_position']['latitude'], data['iss_position']['longitude'])

resp = requests.get("https://api.wheretheiss.at/v1/coordinates/" +str.format(lat) + ","+str.format(long))
print(resp.status_code)
data = resp.json()
print(data)
GMP = (data['map_url'])
webbrowser.open(GMP)
import requests
import time
import urllib
import webbrowser

resp = requests.get("http://api.open-notify.org/iss-now.json")
print(resp.status_code)
data = resp.json()
lat = (data['iss_position']['latitude'])
print(lat)
long = (data['iss_position']['longitude'])
print(long)
#print(data['iss_position']['latitude'], data['iss_position']['longitude'])

resp = requests.get("https://api.wheretheiss.at/v1/coordinates/" +str.format(lat) + ","+str.format(long))
print(resp.status_code)
data = resp.json()
print(data)
GMP = (data['map_url'])
webbrowser.open(GMP)
