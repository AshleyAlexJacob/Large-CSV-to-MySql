import mysql.connector # pip install mysql-connector-python == 8.0.29
import pandas as pd

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password='',
  database="testDb"
)
data  = pd.read_csv('data.csv',encoding = "ISO-8859-1")
# print(data.count())
print(data.the_key.unique() )
if db.is_connected:
  cursor = db.cursor()
  cursor.execute("select database();")
  record = cursor.fetchone()
  print("You're connected to database: ", record)
  for i,row in data.iterrows():
            #here %S means string values 
            sql = ("INSERT INTO testDb.location_data"
            "(the_key,cvr_nr,cvr_navn,p_nr,p_navn,p_ansatte,p_ansatte_interval,p_ansatte_date,p_adresseid,p_vejkode,p_vejnavn,p_husnr,p_bogstav,p_etage,p_door,p_postnr,p_postnrnavn,p_kommunenavn,p_kommunekode,p_region,p_sammensatStatus,p_last_update)"
            "VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            cursor.execute(sql, tuple(row))
            print("Record inserted")
#           db.commit()

db.close()