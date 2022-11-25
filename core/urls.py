from django.urls import path
from .views import index, carrinho, lanches, combos, pasteis, bebidas, tapiocas, produto

urlpatterns = [
    path('', index, name='index'),
    path('carrinho', carrinho, name='carrinho'),
    path('lanches', lanches, name='lanche'),
    path('pasteis', pasteis, name='pastel'),
    path('tapiocas', tapiocas, name='tapioca'),
    path('bebidas', bebidas, name='bebida'),
    path('combos', combos, name='combo'),
    path('produto/<int:pk>', produto, name='produto'),
]