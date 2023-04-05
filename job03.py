import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="msq.575:MRN!", database="laplateforme")
mycursor = conn.cursor()

sql = ("insert into `etage2`(`nom`, `numero`, `superficie`) values(%s, %s, %s)")
sql2 = ("insert into `salles2`(`nom`, `id_etage`, `capacite`) values(%s, %s, %s)")
val1 = ("RDC", 0, 500)
val2 = ("R+1", 1, 500)

new_val1 = ("Lounge", 1, 100)
new_val2 = ("Studio son", 1, 5)
new_val3 = ("Broadcasting", 2, 50)
new_val4 = ("Bocal peda", 2, 4)
new_val5 = ("Coworking", 2, 80)
new_val6 = ("Lounge", 2, 5)


#mycursor.execute(sql, val1)
#mycursor.execute(sql, val2)
mycursor.execute(sql2, new_val1)
mycursor.execute(sql2, new_val2)
mycursor.execute(sql2, new_val3)
mycursor.execute(sql2, new_val4)
mycursor.execute(sql2, new_val5)
mycursor.execute(sql2, new_val6)



conn.commit()

print(mycursor.rowcount, "record inserted.")