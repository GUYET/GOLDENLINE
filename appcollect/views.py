from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import RequeteCollecte


@require_GET
def visualisation(request):
    return render(
        request,
        template_name="visualisation.html",
        context={"requete": RequeteCollecte.objects.all()},
    )
