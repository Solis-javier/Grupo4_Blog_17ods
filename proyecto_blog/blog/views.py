from django.shortcuts import render
from django.http import HttpResponse


posts =[
    {
        'autor':'Solis Javier',
        'titulo':'Posteo numero 1',
        'contenido':'EL primer contenido',
        'fecha_post':'11 diciembre 2021',

    },
    {
        'autor':'Pablo Correa',
        'titulo':'Posteo numero 2',
        'contenido':'EL segundo contenido',
        'fecha_post':'12 diciembre 2021',

    }

]


# Create your views here.
def inicio(request):
    contexto = {
        'posts': posts
    }
    return render(request,'blog/inicio.html', contexto)

def acerca_de(request):
    return render(request,'blog/about.html', {'title':'Acerca de'})
