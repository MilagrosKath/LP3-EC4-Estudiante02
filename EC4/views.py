from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def listarCarreras(request):
    return render(request, 'listarcarreras.html')

def crearCarreras(request):
    return render(request, 'crearcarreras.html')

def listarCursos(request):
    return render(request, 'listarcursos.html')

def crearCursos(request):
    return render(request, 'crearcursos.html')