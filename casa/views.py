from pdb import post_mortem
from django.shortcuts import render, redirect
from .models import Casa

# Create your views here.
def list_casa(request):
    casa = Casa.objects.all()
    return render(request, 'casa.html', {"casa": casa})

def create_casa(request):
    casa = Casa(cuarto=request.POST['cuarto'], metro=request.POST['metro'], baño=request.POST['baño'], descripcion=request.POST['descripcion'])
    casa.save()
    return redirect('/casa/')

def delete_casa(request, casa_id):
    casa = Casa.objects.get(id=casa_id)
    casa.delete()
    return redirect('/casa/')

def editar_casa(request, casa_id):
    casa = Casa.objects.get(id=casa_id)
    if request.method == "POST":
        casa.cuarto = request.POST['cuarto']
        casa.metro  = request.POST['metro']
        casa.baño   = request.POST['baño']
        casa.descripcion = request.POST['descripcion']
        casa.save()
        
        return redirect('/casa/')
    return render (request, 'house.html', {"casa": casa})
        
        

