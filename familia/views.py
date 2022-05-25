from django.shortcuts import redirect, render
from .models import Familia
from .forms import FamiliaForm
# Create your views here.

#Vista Inicio
def inicio(request):
    return render(request, 'paginas/inicio.html')

#Vistas Familia
def familia(request):
    familia = Familia.objects.all()
    #print(familia)
    return render(request, 'familia/familia.html', {'familia': familia})

def crear_familiar(request):
    formulario = FamiliaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('familia')
    
    return render(request, 'familia/crear_familiar.html', {'formulario': formulario})

def editar_familiar(request, id):
    familia = Familia.objects.get(id=id)
    formulario = FamiliaForm(request.POST or None, request.FILES or None, instance=familia)
    if formulario.is_valid() and request.POST: #PUEDE SER TAMBIÉN request.method == 'POST'
        formulario.save()
        return redirect('familia')
    
    return render(request, 'familia/editar_familiar.html', {'formulario':formulario})

def borrar_familiar(request, id):
    familia = Familia.objects.get(id = id)
    familia.delete()
    return redirect('familia')