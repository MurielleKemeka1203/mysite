from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Band
# Create your views here.

def bonjour(request):
    return HttpResponse('<h1> Bonjour et bienvenu!</h1>')

def about(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")