from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import tema, articulo
from django.urls import reverse
from django.db.models import Q

# Create your views here.

def busqueda(request):
    busqueda = request.GET.get("buscar")
    listaTema = tema.objects.all().order_by('id')
    listaArticulo = articulo.objects.all()
    if busqueda:
        listaArticulo = articulo.objects.filter(
            Q(tituloArticulo__icontains = busqueda) |
            Q(contenidoArticulo__icontains = busqueda)
        ).distinct()
        return render(request, 'busqueda.html',{
            'listaTema':listaTema,
            'listaArticulo':listaArticulo
        })
    return render(request,'busqueda.html',{
        'listaTema':listaTema,
        'listaArticulo':listaArticulo
    })
    

def home(request):
    listaTema = tema.objects.all().order_by('id')
    listaArticulo = articulo.objects.all()
    busqueda = request.GET.get("buscar")
    if busqueda:
        listaArticulo = articulo.objects.filter(
            Q(tituloArticulo__icontains = busqueda) |
            Q(contenidoArticulo__icontains = busqueda)
        ).distinct()
        return render(request, 'busqueda.html',{
            'listaTema':listaTema,
            'listaArticulo':listaArticulo
        })
    return render(request,'home.html',{
        'listaTema':listaTema,
        'listaArticulo':listaArticulo
    })

def registroTema(request):
    listaTema = tema.objects.all().order_by('id')
    if request.method == 'POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        objTema = tema.objects.create(
            nombreTema = nombreTema,
            descripcionTema = descripcionTema
        )
        objTema.save()
        return HttpResponseRedirect(reverse('wikiApp:home'))
    busqueda = request.GET.get("buscar")
    if busqueda:
        listaArticulo = articulo.objects.filter(
            Q(tituloArticulo__icontains = busqueda) |
            Q(contenidoArticulo__icontains = busqueda)
        ).distinct()
        return render(request, 'busqueda.html',{
            'listaTema':listaTema,
            'listaArticulo':listaArticulo
        })
    return render(request,'registroTema.html',{
        'listaTema':listaTema
    })

def registroArticulo(request):
    listaTema = tema.objects.all().order_by('id')
    if request.method == 'POST':
        tituloArticulo = request.POST.get('tituloArticulo')
        contenidoArticulo = request.POST.get('contenidoArticulo')
        temaRegistro = request.POST.get('temaSeleccionado')
        temaRelacionado = tema.objects.get(id = temaRegistro )
        objArticulo = articulo.objects.create(
            tituloArticulo = tituloArticulo,
            contenidoArticulo = contenidoArticulo,
            temaRelacionado = temaRelacionado
        )
        objArticulo.save()
        return HttpResponseRedirect(reverse('wikiApp:home'))
    busqueda = request.GET.get("buscar")
    if busqueda:
        listaArticulo = articulo.objects.filter(
            Q(tituloArticulo__icontains = busqueda) |
            Q(contenidoArticulo__icontains = busqueda)
        ).distinct()
        return render(request, 'busqueda.html',{
            'listaTema':listaTema,
            'listaArticulo':listaArticulo
        })
    return render(request,'registroArticulo.html',{
        'listaTema' : listaTema
    })

def vistaTema(request, idTema):
    listaTema = tema.objects.all().order_by('id')
    objTema = tema.objects.get(id = idTema)
    listaArticulo = objTema.articulo_set.all()
    busqueda = request.GET.get("buscar")
    if busqueda:
        listaArticulo = articulo.objects.filter(
            Q(tituloArticulo__icontains = busqueda) |
            Q(contenidoArticulo__icontains = busqueda)
        ).distinct()
        return render(request, 'busqueda.html',{
            'listaTema':listaTema,
            'listaArticulo':listaArticulo
        })
    return render(request, 'vistaTema.html', {
        'listaTema': listaTema,
        'objTema': objTema,
        'listaArticulo': listaArticulo
    })

def vistaArticulo(request, idArticulo):
    listaTema = tema.objects.all().order_by('id')
    objArticulo = articulo.objects.get(id=idArticulo)
    busqueda = request.GET.get("buscar")
    if busqueda:
        listaArticulo = articulo.objects.filter(
            Q(tituloArticulo__icontains = busqueda) |
            Q(contenidoArticulo__icontains = busqueda)
        ).distinct()
        return render(request, 'busqueda.html',{
            'listaTema':listaTema,
            'listaArticulo':listaArticulo
        })
    return render(request,'vistaArticulo.html',{
        'listaTema': listaTema,
        'objArticulo':objArticulo,
    })