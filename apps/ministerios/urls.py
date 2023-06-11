from django.urls import path
from apps.ministerios.views import ministerio_consult, ministerio_update, ministerio_create, ministerio_delete

urlpatterns = [
    path('ministerio_consult/', ministerio_consult, name='ministerio_consult'),
    path('ministerio_create/', ministerio_create, name='ministerio_create'),
    path('ministerio_update/<int:pk>/', ministerio_update, name='ministerio_update'),
    path('ministerio_delete/<int:pk>/', ministerio_delete, name='ministerio_delete'),
]
