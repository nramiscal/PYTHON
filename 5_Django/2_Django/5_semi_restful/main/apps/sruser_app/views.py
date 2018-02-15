from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from models import *


# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^users$', views.index),
#     url(r'^users/new$', views.new),
#     url(r'^users/<id>$', views.show),
#     url(r'^users/create$', views.create), POST
#     url(r'^users/<id>/edit$', views.edit),
#     url(r'^users/<id>/destroy$', views.destroy),
#     url(r'^users/<id>$', views.update), POST
# ]

def index(request):
    context = {
        "users" : User.objects.all()
    }

    return render(request, 'sruser_app/index.html', context)

def new(request):
    return render(request, 'sruser_app/new.html')

def create(request):
    print request.POST
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    return redirect('/')

def show(request, id):
    context = {
        "user" : User.objects.get(id=id)
    }

    return render(request, 'sruser_app/show.html', context)

def edit(request, id):
    context = {
        "user" : User.objects.get(id=id)
    }
    return render(request, 'sruser_app/edit.html', context)

def update(request, id):
    print request.POST
    context = {
        "id": id
    }
    b = User.objects.get(id=id)
    b.first_name = request.POST['first_name']
    b.last_name = request.POST['last_name']
    b.email = request.POST['email']
    b.save()
    # return render(request, 'sruser_app/{}/show.html'.format(id))
    return redirect('/users/{}'.format(id))

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/')
