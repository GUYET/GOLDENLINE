--Sélection des colonnes de chaque table
SELECT customers.id_customer, customers.child_number, customers.csp_name_id, purchases.purchase_amount, purchases.purchase_date, purchases.nb_collect_id

--Sélection des tables
FROM customers, purchases

--Jointure des colonnes communes
WHERE purchases.nb_collect_id = customers.nb_collect

--Limiter le nombre de résultat
LIMIT 10 ;
