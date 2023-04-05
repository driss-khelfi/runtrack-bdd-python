import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="msq.575:MRN!", database="laplateforme")
cursor = conn.cursor()


cursor.execute("select sum(superficie) from etage2")
result = cursor.fetchone()
my_result = result[0]

print("La superficie de la Plateforme est de", my_result, "m²")

conn.close()