# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from users.forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home-page')
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form})
