from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime


def index(request):

    return render(request, 'session_words_app/index.html')

def process(request):
    if not 'font_size' in request.POST:
        font_size = "100%"
    else:
        font_size = "150%"

    date = str(datetime.now().replace(microsecond=0))
    print "date:"
    print date
    context = {
        "word": request.POST['word'],
        "color": request.POST['color'],
        "font_size": font_size,
        "time": date,
    }
    print "context:"
    print context
    if not 'list' in request.session:
        list = []
        list.append(context)
        request.session['list'] = list
    else:
        list = request.session['list']
        list.append(context)
        request.session['list'] = list

    print "session list:"
    print request.session['list']

    return redirect('/')


def clear(request):
    print "now in clear"
    del request.session['list']
    return redirect('/')
