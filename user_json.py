import pandas as pd
import requests
import mysql.connector
import json
pull=requests.get("https://jsonplaceholder.typicode.com/users")
json_data=pull.json()
#dataa=pd.json_normalize(json_data)
#details=[{'name': user['name'],'email': user['email']} for user in json_data]
#for id in details:
#    print(id)
#new=pd.DataFrame(details)
#print(new)
#file=new.to_csv("employees.csv")
#print(json_data)
bs=[{'name':user['name'],'Business':user['company']['bs']} for user in json_data]
bs_data=pd.DataFrame(bs)
#print(bs_data)
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='2040',
    database='data'
)
cursor=conn.cursor()
create_table="CREATE TABLE IF NOT EXISTS data.business(name varchar(100),Business varchar(100))"
cursor.execute(create_table)
insert_query="INSERT INTO data.business(name,Business) VALUES (%s,%s)"
for _,line in bs_data.iterrows():
    insert_data=cursor.execute(insert_query,(line['name'],line['Business']))
conn.commit()
cursor.close()
conn.close()
print("data is loaded into database correctly")
#data=pd.DataFrame(json_data)
#print(data)
#print(data.info())
#print(data.isnull().sum())