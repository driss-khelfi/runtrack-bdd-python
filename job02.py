import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="msq.575:MRN!", database="laplateforme")
mycursor = conn.cursor()

mycursor.execute("create table etage2 (id integer auto_increment primary key, nom varchar(255), numero int, superficie int)")
mycursor.execute("create table salles2 (id integer auto_increment primary key, nom varchar(255), id_etage int, capacite int)")

conn.commit()

