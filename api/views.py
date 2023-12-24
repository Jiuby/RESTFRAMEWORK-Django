from rest_framework import viewsets
from .serializer import trabajadorSerializer
from .models import trabajador
from django.shortcuts import render

class trabajadorViewSet(viewsets.ModelViewSet):
    queryset = trabajador.objects.all()
    serializer_class = trabajadorSerializer

def search_results(request):
    workers = trabajador.objects.none()  # Empty QuerySet
    if request.method == 'GET':
        edad = request.GET.get('edad', '')
        cargo = request.GET.get('cargo', '')
        salario = request.GET.get('salario', '').replace(',', '').replace('.', '')
        activo = request.GET.get('activo', '') == 'true'

        if edad.isdigit():
            workers = trabajador.objects.filter(edad__lte=int(edad))

        if cargo:
            workers = trabajador.objects.filter(cargo__icontains=cargo)

        if salario.isdigit():
            workers = [worker for worker in workers if int(worker.salario.replace(',', '').replace('.', '')) <= int(salario)]

        if activo:
            workers = trabajador.objects.filter(activo=activo)

    return render(request, 'index.html', {'workers': workers})