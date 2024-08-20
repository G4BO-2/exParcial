from django.urls import path, include
from . import views

app_name = 'wikiApp'

urlpatterns = [
    path('', views.home, name="home"),
    path('registroTema', views.registroTema, name="registroTema"),
    path('registroArticulo', views.registroArticulo, name="registroArticulo"),
    path('vistaTema/<str:idTema>', views.vistaTema, name="vistaTema"),
    path('vistaArticulo/<str:idArticulo>', views.vistaArticulo, name='vistaArticulo'),
    path('busqueda', views.busqueda, name="busqueda")

]