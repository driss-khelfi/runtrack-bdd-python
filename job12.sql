insert into etudiants2(prenom, nom, age, email)
    -> value('Martin', 'Dupuis', 18, 'martin.dupuis@laplateforme.io')

SELECT * FROM etudiants2 WHERE nom='dupuis';