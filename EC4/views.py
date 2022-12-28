from django.shortcuts import render, HttpResponse, redirect
from EC4.models import Course
from EC4.forms import FormArticulo
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def listarCarreras(request):
    return render(request, 'listarcarreras.html')

def crearCarreras(request):
    return render(request, 'crearcarreras.html')

def listarCursos(request):
    cursos = Course.objects.all()
    return render(request, 'listarcursos.html',{
           'cursos':cursos,

    })

def crearCursos(request):
    formulario = FormArticulo(request.POST)
    return render(request, 'crearcursos.html', {'formulario':formulario})

def crearFullCursos(request):
    if request.method == 'POST':
        name = request.POST['name']
        contenido = request.POST['contenido']
        state = request.POST['state']
        course = Course(
            name = name,
            contenido = contenido,
            state = state
        )
        course.save()
        return redirect('listarCursos')
    else:
        return HttpResponse('<h2>No se ha podido registrar el articulo</h2>')

def eliminarCurso(request, id):
    curso = Course.objects.get(pk=id)
    curso.delete()
    return redirect('listarCursos')

