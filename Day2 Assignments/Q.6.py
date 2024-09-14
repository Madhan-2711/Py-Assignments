import requests
import pandas as pd
import json
import time

url = "http://api.open-notify.org/iss-now.json"

header= {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
}

loc = []
i=1
while(i<100):
    
 try:
    data = requests.get(url,headers = header)
    
    js = json.loads(data.text)
    
    latitude = js['iss_position']['latitude']
    longitude = js['iss_position']['longitude']
    timestamp = js['timestamp']
    
    loc.append({ "latitude" : latitude, "longitude": longitude, "timestamp": timestamp})
    i=i+1
    print("Record collected Successfully")
 except Exception as e:
     print(e)
     
 
 time.sleep(1) 


dat = pd.DataFrame(loc)
dat.to_csv("location.csv", index = False)
print("All Records updated into csv file")


