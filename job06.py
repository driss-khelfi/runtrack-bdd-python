import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="msq.575:MRN!", database="laplateforme")
cursor = conn.cursor()


cursor.execute("select sum(capacite) from salles2")
result = cursor.fetchone()
my_result = result[0]

print("La capacité de toutes les salles est de:", my_result)

conn.close()