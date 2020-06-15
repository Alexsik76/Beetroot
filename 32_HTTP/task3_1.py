import requests
import sys

# location = "689558"
url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=5dc158e8a8dde73cdcfe9ac5c03d6a23"
r = requests.get(url)
print(r, type(r))
print(r.json())
print(r.text)
print(dir(r))
print(help(r))