from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            # Authentification réussie, connectez l'utilisateur
            login(request, user)
            return redirect("")  # Redirigez vers la page d'accueil ou une autre page
        else:
            # Authentification échouée, affichez un message d'erreur
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(
                request, "accounts/login.html", {"error_message": error_message}
            )

    return render(request, "accounts/login.html")


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


@login_required
class DataDepenseCspChartView(TemplateView):
    template_name = "visualisation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["datas"] = DataPanierMoyenCsp.objects.all()
        return context
