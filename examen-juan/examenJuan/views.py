from django.shortcuts import render  
from django.db.models import Q  
from .models import Coche, Marca, Fabrica, ITV, Revision  

# ------------------------ 
def error_400(request, exception=None):  
    return render(request, 'errores/400.html', None, None, 400)  

def error_402(request, exception=None):  
    return render(request, 'errores/402.html', None, None, 402)  

def error_403(request, exception=None):  
    return render(request, 'errores/403.html', None, None, 403)  

def error_404(request, exception=None):  
    return render(request, 'errores/404.html', None, None, 404)  

def error_500(request, exception=None):  
    return render(request, 'errores/500.html', None, None, 500)  

# ------------------------ 

def index(request):  
    return render(request, 'examenJuan/index.html')  


def modelo_ciudad(request, marca_modelo, fabrica_ciudad):
    coche = Coche.objects.select_related('marca', 'fabrica')
    coche = coche.filter(marca__modelo__contains=marca_modelo).filter(fabrica__ciudad__contains=fabrica_ciudad)
    return render(request, 'examenJuan/buscar.html', {'modelo_ciudad':coche})