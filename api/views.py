from rest_framework import viewsets
from .serializer import trabajadorSerializer
from .models import trabajador
from django.shortcuts import render

class trabajadorViewSet(viewsets.ModelViewSet):
    queryset = trabajador.objects.all()
    serializer_class = trabajadorSerializer

def search_results(request):
    workers = trabajador.objects.none()
    if request.method == 'GET':
        id = request.GET.get('id', '')
        if id.isdigit():
            workers = trabajador.objects.filter(id=id)

    return render(request, 'index.html', {'workers': workers})