# RAPPEL DE LA REQUETE SQL

# --Sélection des colonnes de chaque table
# SELECT purchases.nb_collect_id, purchases.purchase_amount, purchases.product_category_name_id

# --Sélection des tables
# FROM purchases

# --Liste ordonnée
# ORDER BY nb_collect_id

# --Limiter le résultat
# LIMIT 10 ;

from pyspark.sql import SparkSession

# Création session Spark
spark = SparkSession.builder.getOrCreate()

# Extraction des données CSV dans des DataFrames
purchases_df = spark.read.csv(
    "collect/data_app_interne/purchases/purchases.csv", header=True, inferSchema=True
)

# Transformation des DataFrames
result_df = (
    purchases_df.select("nb_collect_id", "purchase_amount", "product_category_name_id")
    .orderBy("nb_collect_id")
    .limit(10)
)

# Chargement résultat dans un fichier CSV
result_df.write.csv("collect/Requete_SPARK/result_collecte.csv", header=True)

# Arrêt de la session Spark
spark.stop()
