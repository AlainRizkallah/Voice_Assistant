import json
import requests
location="Paris,fra"
apiKey="24126675319c0b0356c039fd10156afc"

response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID="+apiKey+"&q="+location+"&units=metric")
todos = json.loads(response.text)

def printTemp():
    print(todos['list'][0]['main']['temp'])