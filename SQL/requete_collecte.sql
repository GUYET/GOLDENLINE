--Sélection des colonnes de chaque table
SELECT purchases.nb_collect_id, purchases.purchase_amount, purchases.product_category_name_id

--Sélection des tables
FROM purchases

--Liste ordonnée
ORDER BY nb_collect_id

--Limiter le résultat
LIMIT 10 ;