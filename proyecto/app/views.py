from django.shortcuts import render, redirect

from app.models import Sistema, Smartphone
# Create your views here.


def inicio(request):
    smartphones = Smartphone.objects.all()
    sistemas = Sistema.objects.all()

    contexto={'smartphones': smartphones, 'sistemas': sistemas} #con este diccionario se enviar las variables al html
    return render(request, 'inicio.html', contexto)

# Función para agregar objetos a la base de dato.
def agregar(request):
    modelo =request.POST.get('modelo', '') #se obtiene el valor del input con name modelo.
    id_sistema = request.POST.get('sistema', '') #se obtiene el valor de select con name sistema.

    sistema = Sistema.objects.get(id=id_sistema) # obtenemos el objeto con ese id.

    smartphone = Smartphone(modelo = modelo, sistema =sistema)
    smartphone.save()

    return redirect('inicio')

#Función para editar objetos en la base de datos.

def editar(request, id): 
    modelo = request.POST.get('modelo', '')
    id_sistema = request.POST.get('sistema', '')

    sistema = Sistema.objects.get (id=id_sistema) # obtenemos el objeto con dicha id.

    smartphone = Smartphone.objects.get(id = id) 

    smartphone.modelo= modelo # sobre escribimos el valor de modelo
    smartphone.sistema= sistema # sobre escribimos el valor de sistemas

    smartphone.save()

    return redirect('inicio')


def eliminar(request, id):

    smartphone = Smartphone.objects.get(id = id) 
    smartphone.delete() #eliminamos el objeto de la base de datos.
   

    return redirect('inicio')