"""
URL configuration for RESTAPIwithDJANGO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from api import views

urlpatterns = [
    path('', RedirectView.as_view(url='/search_results/', permanent=True)),  # Redirige la ruta raíz a /search_results/
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('search_results/', views.search_results, name='search_results'),
]


