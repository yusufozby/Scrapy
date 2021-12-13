import json
import mysql.connector

con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1453",
  database="Alanlar" 
 


)

mycursor = con.cursor()

#mycursor.execute("CREATE DATABASE Alanlar")
mycursor.execute("CREATE TABLE Department(bolum VARCHAR(255),departmentId int(12) AUTO_INCREMENT, PRIMARY KEY (departmentId))")




with open('konular.json') as f:
  veriler = json.load(f)
print(veriler)
for veri in veriler:
  print(veri['Alan'])
  mycursor.execute("INSERT INTO Department (bolum) VALUES  ('{}')".format(veri['Alan']))
con.commit()
  