from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trainner
from .forms import TrainnerForm
from .operations import *

def index(request):
    return render(request, 'index.html')

def register(request):
    formulario = TrainnerForm(request.POST or None)

    if formulario.is_valid():

        nombre = formulario.cleaned_data['nombre']
        sexo = formulario.cleaned_data['sexo']
        edad = formulario.cleaned_data['edad']
        peso = formulario.cleaned_data['peso']
        altura = formulario.cleaned_data['altura']
        cintura = formulario.cleaned_data['cintura']
        cuello = formulario.cleaned_data['cuello']
        cadera = formulario.cleaned_data['cadera']
        actividad = formulario.cleaned_data['actividad']
        
        usuario = Usuario(sexo, edad, peso, altura, cintura, cuello, cadera)
        
        bmr = usuario.calcular_bmr()
        indice_cintura = usuario.calcular_indice_cintura_altura(),
        porcen_graso = usuario.calcular_porcentaje_graso(),
        ##masa_corporal = usuario.masa_corporal_magra(porcen_graso),
        calorias = calcular_calorias(bmr, actividad)
        
        print(f"Bmr: {bmr}")
        print(f"Porcentajede grasa: {porcen_graso}")
        print(f"Indice de cintura: {indice_cintura}")
        #print(f"Masa corporal: {masa_corporal}")
        print(f"Calorias: {calorias}")


     
        datos_trainner = Trainner(
            nombre = nombre,
            sexo = sexo,
            edad = edad,
            peso = peso,
            altura = altura,
            cintura = cintura,
            cuello = cuello,
            cadera = cadera,
            actividad = actividad
        )

        datos_trainner.save()
        return redirect('index')
    else:
        formulario = TrainnerForm()

    return render(request, 'register.html', {'formulario': formulario})

def table(request):
    datos = Trainner.objects.all()
    return render(request, 'table.html', {'datos': datos})

def edit(request, id):

    trainner = Trainner.objects.get(id_persona = id)
    formulario = TrainnerForm(request.POST or None, instance=trainner)

    return render(request, 'edit.html', {'formulario': formulario})

def eliminar(request, id):
    trainner = Trainner.objects.get(id_persona=id)
    trainner.delete()
    return redirect('index')
