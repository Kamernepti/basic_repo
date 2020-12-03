from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, "index.html")

# This way works but changes all of the inputs at the same time when the rest were added 
def process_money(request):
    if request.session =="GET":
        return redirect('/')
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['farmcounter'] = random.randint(10, 20)
    request.session['counter'] += request.session['farmcounter']
    return render(request, 'process_money.html')


# This didn't work
# def process_money(request):
#     if request.session == "GET":
#         return redirect("/")
#     if 'counter' not in request.session:
#         request.session['counter'] = 0
#     if request.method =="POST":
#         request.session['farmcounter'] = request.POST['farmhouse']
#         request.session['farmhouse'] = random.randint(10, 20)
#     request.session['counter'] +=request.session['farmhouse']
#     return render(request, 'process_money.html')

def reset (request):
    request.session.flush()
    request.session['counter'] = 0
    return redirect('/')