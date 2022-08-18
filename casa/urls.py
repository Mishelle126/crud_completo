from django.urls import path
from .views import list_casa, create_casa, delete_casa, editar_casa

urlpatterns = [
    path('', list_casa),
    path('new/', create_casa, name='create_casa'),
    path('delete_casa/<int:casa_id>/', delete_casa, name='delete_casa'),
    path('editar_casa/<int:casa_id>/', editar_casa, name='editar_casa'),
]
