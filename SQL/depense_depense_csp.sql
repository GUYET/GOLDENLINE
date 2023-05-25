SELECT csp_name_id, SUM(purchase_amount) as depense_csp
FROM depense_detail_csp
GROUP BY csp_name_id