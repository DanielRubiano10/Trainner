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

        formulario.save()
        return redirect('index')
    else:
        formulario = TrainnerForm()

    return render(request, 'register.html', {'formulario': formulario})

def table(request):
    return render(request, 'table.html')

def edit(request):
    return render(request, 'edit.html')

def results(request):
    return render(request, 'results.html')
