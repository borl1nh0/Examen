from django.db import models  

class Marca(models.Model):   
    modelo = models.CharField(max_length=100)  

class Fabrica(models.Model):   
    ciudad = models.CharField(max_length=100)  
    

class ITV(models.Model):  
    ciudad = models.CharField(max_length=100)  
    
class Coche(models.Model):  
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)  
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)    
    precio_base = models.FloatField(null=True)  
    anyo_lanzamiento = models.PositiveIntegerField()
    itv = models.ManyToManyField("ITV", through="Revision") 

 
class Revision(models.Model):  
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE)  
    itv = models.ForeignKey(ITV, on_delete= models.CASCADE, null=True)   
    kilometraje = models.PositiveIntegerField()  
      

   