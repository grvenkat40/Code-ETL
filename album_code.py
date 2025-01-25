import pandas as pd
import requests
import openpyxl
url="https://jsonplaceholder.typicode.com/albums"
response=requests.get(url)
data=response.json()
#for user in data:
#    print(user['userId'])
df=pd.DataFrame(data) #df=pd.json_normalize(data)
#print(df)
#print(data[0]['userId'])
#titles=[a['title'] for a in data]
#for title in titles:
#    print(title)
try:
    df.to_csv("albums.csv",index=True)
    print("csv File saved successfully!")
    df.to_excel('albums.xlsx',engine='openpyxl')
    print("excel File saved successfully!")
except Exception as e:
    print("Error:", e)

