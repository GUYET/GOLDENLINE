SELECT csp_name_id, SUM(purchase_amount) AS panier_moyen
FROM depense_categorie_csp
GROUP BY csp_name_id