from django.shortcuts import render, redirect
from .models import *

def index(request):
    context= {
        "dojos": Dojos.objects.all(),
        "ninjas":Ninjas.objects.all()
    }
    return render(request, 'index.html', context)

def dojo_table(request):
    Dojos.objects.create(
        name=request.POST["name"],
        city=request.POST["city"],
        state=request.POST["state"],
    )
    return redirect('/')

def ninja_table(request):
    Ninjas.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        dojo=request.POST["dojo"],
    )
    return redirect('/')