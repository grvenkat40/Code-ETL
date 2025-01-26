import pandas as pd
import numpy as np
import requests
import mysql.connector
data = pd.read_csv(r"C:\Users\ADMIN\Downloads\AI in Retail Dataset.csv", encoding="latin1")
#print(data.head())

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='2040',
    database='data'
)
cursor=conn.cursor()
table_query="""CREATE TABLE AI_Retail_Data (
    Country VARCHAR(50),
    Online_Consumer VARCHAR(3),
    Age VARCHAR(10),
    Annual_Salary VARCHAR(50),
    Gender VARCHAR(10),
    Education VARCHAR(100),
    Payment_Method_Credit_Debit VARCHAR(3),
    Living_Region VARCHAR(50),
    Online_Service_Preference VARCHAR(3),
    AI_Endorsement VARCHAR(3),
    AI_Privacy_No_Trust VARCHAR(3),
    AI_Enhance_Experience VARCHAR(3),
    AI_Satisfaction VARCHAR(3),
    AI_Tools_Used_Chatbots VARCHAR(3),
    AI_Tools_Used_Virtual_Assistant VARCHAR(3),
    AI_Tools_Used_Voice_Photo_Search VARCHAR(3),
    Payment_Method_COD VARCHAR(3),
    Payment_Method_Ewallet VARCHAR(3),
    Product_Category_Appliances VARCHAR(3),
    Product_Category_Electronics VARCHAR(3),
    Product_Category_Groceries VARCHAR(3),
    Product_Category_Personal_Care VARCHAR(3),
    Product_Category_Clothing VARCHAR(3))"""
#table_create=cursor.execute(table_query)
insert_query=""" INSERT INTO data.AI_Retail_Data (
    Country,
    Online_Consumer,
    Age,
    Annual_Salary,
    Gender,
    Education,
    Payment_Method_Credit_Debit,
    Living_Region,
    Online_Service_Preference,
    AI_Endorsement,
    AI_Privacy_No_Trust,
    AI_Enhance_Experience,
    AI_Satisfaction,
    AI_Tools_Used_Chatbots,
    AI_Tools_Used_Virtual_Assistant,
    AI_Tools_Used_Voice_Photo_Search,
    Payment_Method_COD,
    Payment_Method_Ewallet,
    Product_Category_Appliances,
    Product_Category_Electronics,
    Product_Category_Groceries,
    Product_Category_Personal_Care,
    Product_Category_Clothing
)
VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
for _,row in data.iterrows():
    #insert_data=cursor.execute(insert_query,(
    row['Country'],
    row['Online_Consumer'],
    row['Age'],
    row['Annual_Salary'],
    row['Gender'],
    row['Education'],
    row['Payment_Method_Credit/Debit'],
    row['Living_Region'],
    row['Online_Service_Preference'],
    row['AI_Endorsement'],
    row['AI_Privacy_No_Trust '],
    row['AI_Enhance_Experience'],
    row['AI_Satisfication'],
    row['AI_Tools_Used _Chatbots'],
    row['AI_Tools_Used_Virtual_Assistant'],
    row['AI_Tools_Used_Voice&Photo_Search'],
    row['Payment_Method_COD'],
    row['Payment_Method_Ewallet'],
    row['Product_Category_Appliances'],
    row['Product_Category_Electronics'],
    row['Product_Category_Groceries'],
    row['Product_Category_Personal_Care'],
    row['Product_Category_Clothing']
    ))
    
conn.commit()
cursor.close()
conn.close()
print("Data is successfully loaded into your server")