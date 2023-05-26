import psycopg2
import os

# Connexion à la base de données
conn = psycopg2.connect(
    database="app_collect",
    user="postgres",
    password="($*lsfLxhBuqLp$",
    host="127.0.0.1",
    port="5432",
)
cursor = conn.cursor()

# Chemin fichier
file_path = os.path.join(os.path.dirname(__file__), "products_categories.txt")

# Ouverture fichier et lecteur
with open(file_path, "r") as file:
    lines = file.readlines()

# Requête d'insertion
insert_query = "INSERT INTO products_categories (product_category_name) VALUES (%s);"

# Convertion des lignes en liste de tuples
values = [(line.strip(),) for line in lines]

# Exécution de la requête d'insertion avec les valeurs
cursor.executemany(insert_query, values)


# Validation des modifications
# Fermeture de la connexion à la base de données
conn.commit()
cursor.close()
conn.close()
