import pandas 
import requests
url='https://github.com/Ovi/DummyJSON/blob/master/database/posts.json'
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print(data)
else:
    print('failed')