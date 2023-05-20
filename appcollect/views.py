from django.shortcuts import render


def visualisation(request):
    return render(request, template_name="visualisation.html")
