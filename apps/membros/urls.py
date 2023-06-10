from django.urls import path
from apps.membros.views import index, cadastro, consulta, editar, excluir

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('consulta/', consulta, name='consulta'),
    path('editar/<int:id>/', editar, name='editar'),
    path('excluir/<int:id>/', excluir, name='excluir'),
]