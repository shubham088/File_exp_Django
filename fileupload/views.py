# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadFormDoc

# Create your views here.

@login_required
def uploadPage(request):
    return render(request,'fileupload/loadingFiles.html',{})


def uploadFiles(request):
    if request.method == 'POST':
        form = UploadFormDoc(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('home-page')
    else:
        form = UploadFormDoc()
    return render(request, 'fileupload/loadingFiles.html', {'form': form})
