from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import RequeteCollecte, RequeteAnonymisees


@require_GET
def visualisation(request):
    requetes_collecte = RequeteCollecte.objects.all()
    requetes_anonymisees = RequeteAnonymisees.objects.all()
    return render(
        request,
        template_name="visualisation.html",
        context={
            "requetes_collecte": requetes_collecte,
            "requetes_anonymisees": requetes_anonymisees,
        },
    )
