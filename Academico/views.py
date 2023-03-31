from django.shortcuts import render, redirect
from .models import Curso

# Create your views here.

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    cursosListados = Curso.objects.all()
    return render(request, "gestioncurso.html", {'cursos': cursosListados})


def registrarcurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')


def eliminarcurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')


def editarcurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    return redirect('/')


def edicioncurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "editarcurso.html", {"curso": curso})
