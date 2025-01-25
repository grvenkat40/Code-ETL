import pandas as pd
import mysql.connector
import requests
responce=requests.get("https://jsonplaceholder.typicode.com/photos")
json=responce.json()
#print(json)
id=[{"albumid":album['albumId'], 'title':album['title']} for album in json]
#new_data=pd.DataFrame(id)
#print(new_data)
data=pd.DataFrame(json)
print(data)
