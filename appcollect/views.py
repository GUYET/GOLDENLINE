from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import (
    RequeteCollecte,
    RequeteAnonymisees,
    DataDepenseCsp,
    DataPanierMoyenCsp,
)

#Crétion des views
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
class DataDepenseCspChartView(TemplateView):
    template_name = "visualisation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["datas"] = DataDepenseCsp.objects.all()
        return context

@login_required
class DataPanierMoyenCspChartView(TemplateView):
    template_name = "visualisation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["datas"] = DataPanierMoyenCsp.objects.all()
        return context
    
    
