from django.shortcuts import render, HttpResponse, redirect
from time import strftime
from datetime import datetime

def index(request):
  context = {
  # "time": strftime("%Y-%m-%d %H:%M %p"())
    # "time": datetime.now().strftime("%Y-%m-%d %H:%M %p")
    "time": datetime.now()
  }
  return render(request,'time_display/index.html', context)
