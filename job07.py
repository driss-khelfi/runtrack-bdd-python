import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="msq.575:MRN!", database="laplateforme")
mycursor = conn.cursor()


mycursor.execute( "create table test_employes (id integer auto_increment primary key, nom varchar(255), prenom varchar(255), salaire float, id_service int)")
exe2 = ("insert into `test_employes`(`nom`, `prenom`, `salaire`, `id_service`) values(%s, %s, %s, %s)")

val = [("Martin", "Julie", 1800, 1),
       ("Blanc", "Romain", 2200, 2),
       ("Duval", "Zoe", 2600, 3),
       ("Laplace", "Noah", 3000, 4),
       ("Queen", "Elisabeth", 4000, 5)]




exe3 = "select * from test_employes where salaire > 3000"
exe4 = mycursor.executemany(exe2, val)
#my_result = result = mycursor.fetchall()
#my_result = result

#print(my_result)

exe4 = "create table test_service(id integer auto_increment primary key, nom varchar(255))"
exe5 = ("insert into `test_service`(`nom`) values(%s)")

new_val = [("communication"),
           ("clients"),
           ("comptabilite"),
           ("informatique"),
           ("direction")]
exe6 = mycursor.executemany(exe5, new_val)

mycursor.executemany(exe1, exe2, exe3,exe4, exe5, exe6 )


conn.commit()


print(mycursor.rowcount, "record inserted.")