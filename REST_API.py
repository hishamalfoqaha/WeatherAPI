import requests
import json



response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Dortmund?unitGroup=metric&key=AKBLR5U2LLLMDZZF7YRCWZ2Y5&contentType=json")

print(response.json()['days'])

# We can iterate over it

for data in response.json()['days']:
     print(data['datetime'])
     print(data['tempmin'])
     print()