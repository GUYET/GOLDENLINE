import matplotlib.pyplot as plt

# Données factices pour l'exemple
categories = ["Catégorie A", "Catégorie B", "Catégorie C"]
depenses_par_categorie = [1000, 1500, 800]
depense_panier_moyen = [50, 60, 45]

# Tracer le graphique des dépenses par catégorie
plt.figure(figsize=(8, 4))
plt.bar(categories, depenses_par_categorie)
plt.xlabel("Catégorie socioprofessionnelle")
plt.ylabel("Dépenses")
plt.title("Dépenses par catégorie socioprofessionnelle")
plt.show()

# Tracer le graphique de la dépense du panier moyen
plt.figure(figsize=(8, 4))
plt.bar(categories, depense_panier_moyen)
plt.xlabel("Catégorie socioprofessionnelle")
plt.ylabel("Dépense du panier moyen")
plt.title("Dépense du panier moyen par catégorie socioprofessionnelle")
plt.show()

return render(
    request,
    template_name="visualisation.html",
    context={
        "graph_file": graph_file,
    },
)
