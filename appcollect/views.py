from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required

from .models import (
    RequeteCollecte,
    RequeteAnonymisees,
    DataDepenseCsp,
    DataPanierMoyenCsp,
)


@login_required
def visualisation(request):
    requetes_collecte = RequeteCollecte.objects.all()
    requetes_anonymisees = RequeteAnonymisees.objects.all()
    depense_categorie_csp = DataDepenseCsp.objects.all()
    depense_panier_moyen_csp = DataPanierMoyenCsp.objects.all()

    return render(
        request,
        template_name="visualisation.html",
        context={
            "requetes_collecte": requetes_collecte,
            "requetes_anonymisees": requetes_anonymisees,
            "depense_categorie_csp": depense_categorie_csp,
            "depense_panier_moyen_csp": depense_panier_moyen_csp,
        },
    )


@login_required
def graphiques(request):
    depenses = DataDepenseCsp.objects.all().values()
    df = pd.DataFrame(depenses)
    df1 = df.purchase_amount.tolist()
    df = ["csp_name_id"].tolist()
    mydict = {"df": df, "df1": df1}

    return render(request, template_name="visualisation.html", context=mydict)
