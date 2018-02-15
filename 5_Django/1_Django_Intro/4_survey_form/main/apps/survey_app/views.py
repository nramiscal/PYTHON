from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey_app/index.html')


def process(request):

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')




def result(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return render(request, 'survey_app/result.html')
