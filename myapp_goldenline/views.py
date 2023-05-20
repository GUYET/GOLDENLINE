from django.http import HttpRequest, HttpResponse
from django.http.response import JsonResponse


def health(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"statut": "ok"})
