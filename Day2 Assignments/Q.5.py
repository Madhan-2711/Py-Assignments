import requests
import json


url = "http://api.open-notify.org/iss-now.json"

header= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}


data = requests.get(url,headers= header)

js = json.loads(data.text)

print( "latitude:" ,js["iss_position"]["latitude"])
print("Longitude:" , js["iss_position"]["longitude"])
print("TimeStamp:", js["timestamp"])