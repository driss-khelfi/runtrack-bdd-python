import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="msq.575:MRN!", database="laplateforme")
mycursor = conn.cursor()

mycursor.execute("select * from salles2")
my_result = result = mycursor.fetchall()
my_result = result

print(my_result)