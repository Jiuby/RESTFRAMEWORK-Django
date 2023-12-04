from rest_framework import viewsets
from .serializer import trabajadorSerializer
from .models import trabajador

# Create your views here.

class trabajadorViewSet(viewsets.ModelViewSet):
    queryset = trabajador.objects.all()
    serializer_class = trabajadorSerializer