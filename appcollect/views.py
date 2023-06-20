from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import (
    RequeteAnonymisees,
    RequeteCollecte,
    DataDepenseCsp,
    DataDepenseTotalCsp,
    DataPanierMoyenCsp,
)


# Création des views


@login_required
def visualisation(request):
    requetes_anonymisees = RequeteAnonymisees.objects.all()
    requetes_collecte = RequeteCollecte.objects.all()
    depense_detail_csp = DataDepenseCsp.objects.all()
    depense_total_par_csp = DataDepenseTotalCsp.objects.all()
    depense_moyen_par_csp = DataPanierMoyenCsp.objects.all()

    return render(
        request,
        template_name="visualisation.html",
        context={
            "requetes_anonymisees": requetes_anonymisees,
            "requetes_collecte": requetes_collecte,
            "depense_detail_csp": depense_detail_csp,
            "depense_total_par_csp": depense_total_par_csp,
            "depense_moyen_par_csp": depense_moyen_par_csp,
        },
    )

