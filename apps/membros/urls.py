from django.urls import path
from apps.membros.views import index

urlpatterns = [
    path('', index, name='index'),
    #path('cadastro', cadastro, name='cadastro'),
]