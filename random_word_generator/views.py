from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def generate_word(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    request.session['word']= get_random_string(length=14)
    request.session['counter'] +=1
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/')