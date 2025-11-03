from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.index, name='index'),  
    path('Marca/<str:marca_modelo>/Fabrica/<str:fabrica_ciudad>', views.modelo_ciudad, name='modelo_ciudad'),  
   
]  