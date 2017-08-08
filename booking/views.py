# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.template import loader
from models import booking_device
from .forms import BookForm

def index(request):
    return render(request, 'index/index.html')

def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/success/')
    else:
        form = UserCreationForm()
    return render(request,'user/create.html',{'form':form})

#def# retreive(request):
 ##"   if request.method == 'POST':
     #   form = BookForm(request.POST)
      #  if form.is_valid():
       #     starting_point = form.cleaned_data['starting point']
        #    arrival_point = form.cleaned_data['arrival point']
         #   form.save()
          #  print("ok")
           # return render(request, 'book/print_reservations.html', {"form":form})
#    else:
 #       form = BookForm()
  #  return render(request, 'book/layout.html', {'form':form})

def my_reservations(request):
    objects = booking_device.objects.all()
    template = loader.get_template('book/print_reservations.html')
    context = {
        "objects": objects,
    }
    return render(request, 'book/print_reservations.html', context)
   
def retreive(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        form.save()
        print form.cleaned_data['starting_point']
        print form.cleaned_data['arrival_point']
    context = {
        "form": form,
    }
    return render(request, "book/layout.html", context)