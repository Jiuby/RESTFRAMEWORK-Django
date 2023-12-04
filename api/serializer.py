from rest_framework import serializers
from .models import trabajador

class trabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = trabajador
        fields = "__all__"