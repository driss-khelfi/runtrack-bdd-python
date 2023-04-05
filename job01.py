# coding: utf-8

import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="msq.575:MRN!", database="laplateforme")
cursor = conn.cursor()
cursor.execute("select * from etudiants2")
print(cursor.fetchall())
conn.close()