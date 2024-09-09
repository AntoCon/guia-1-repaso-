from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html="""
    <h1>Inicio app1</h1>
    <h2>hola joaquito</h2> <h1> te amo mucho </h1>
    """
    return HttpResponse(html)

# Create your views here.

def funcion(request):
    html="""
    <h2>Hello</h2>
    """
    return HttpResponse(html)
