from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    context = {
        'word' : get_random_string(length=14)
    }

    return render(request, 'word_app/index.html', context)

def reset(request):
    print "in reset function"
    request.session.clear()
    return redirect('/')
