# RAPPEL DE LA REQUETE SQL

# --Sélection des colonnes de chaque table
# SELECT customers.id_customer, customers.child_number, customers.csp_name_id, purchases.purchase_amount, purchases.purchase_date, purchases.nb_collect_id

# --Sélection des tables
# FROM customers, purchases

# --Jointure des colonnes communes
# WHERE purchases.nb_collect_id = customers.nb_collect

# --Limiter le nombre de résultat
# LIMIT 10 ;

from pyspark.sql import SparkSession

# Création session Spark
spark = SparkSession.builder.getOrCreate()

# Extraction des données CSV dans des DataFrames
customers_df = spark.read.csv(
    "collect/data_app_interne/customers/extrait _client.csv",
    header=True,
    inferSchema=True,
)
purchases_df = spark.read.csv(
    "collect/data_app_interne/purchases/purchases.csv", header=True, inferSchema=True
)

# Transformation des DataFrames
result_df = (
    customers_df.join(
        purchases_df, customers_df["nb_collect"] == purchases_df["nb_collect_id"]
    )
    .select(
        customers_df["id_customer"],
        customers_df["child_number"],
        customers_df["csp_name_id"],
        purchases_df["purchase_amount"],
        purchases_df["purchase_date"],
        purchases_df["nb_collect_id"],
    )
    .limit(10)
)

# Chargement résultat dans un fichier CSV
result_df.write.csv("collect/Requete_SPARK/result_anonymisees.csv", header=True)

# Arrêt de la session Spark
spark.stop()
