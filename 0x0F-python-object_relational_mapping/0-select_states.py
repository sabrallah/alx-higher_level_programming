#!/usr/bin/python3
"""
Script qui liste tous les états de la base de données hbtn_0e_0_usa
"""

import sys
import MySQLdb

if name == 'main':


# Connexion à la base de données
connection = MySQLdb.connect(
           user=sys.argv[1], 
           password=sys.argv[2],
           database=sys.argv[3],
           port=3306,
           host='localhost'
)

# Récupération du curseur
cursor = connection.cursor()

# Requête de sélection
cursor.execute('SELECT * FROM states ORDER BY id ASC;')

# Récupération des données
states = cursor.fetchall() 

# Parcours et affichage des états
for state in states:

    print(state)

# Fermeture de la connexion
connection.close()
