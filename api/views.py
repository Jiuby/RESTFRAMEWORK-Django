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
        salario = request.GET.get('salario', '')
        salario = salario.replace(',', '').replace('.', '')
        if salario.isdigit():
            salario = int(salario)
            workers = trabajador.objects.all()
            workers = [worker for worker in workers if int(worker.salario.replace(',', '').replace('.', '')) < salario]

    return render(request, 'index.html', {'workers': workers})