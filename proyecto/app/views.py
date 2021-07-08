from django.shortcuts import render, redirect

from app.models import Sistema, Smartphone
# Create your views here.


def inicio(request):
    smartphones = Smartphone.objects.all()
    sistemas = Sistema.objects.all()

    contexto={'smartphones': smartphones, 'sistemas': sistemas} #con este diccionario se enviar las variables al html
    return render(request, 'inicio.html', contexto)


def agregar(request):
    modelo =request.POST.get('modelo', '') #se obtiene el valor del input con name modelo.
    id_sistema = request.POST.get('sistema', '') #se obtiene el valor de select con name sistema.

    sistema = Sistema.objects.get(id=id_sistema) # obtenemos el objeto con ese id.

    smartphone = Smartphone(modelo = modelo, sistema =sistema)
    smartphone.save()

    return redirect('inicio')