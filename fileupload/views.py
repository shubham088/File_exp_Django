# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFormDoc
from .models import UploadFilesModel

# Create your views here.


#def uploadPage(request):
    #return render(request,'fileupload/loadingFiles.html',{})

@login_required
def uploadFiles(request):

    if request.method == 'POST':

        form = UploadFormDoc(request.POST, request.FILES)
        if form.is_valid():

            newdoc = UploadFilesModel(doc = request.FILES['file'])
            newdoc.save()
            return redirect('home-page')
    else:
        form = UploadFormDoc()
    return render(request, 'fileupload/loadingFiles.html', {'form': form})



@login_required
def download_files(request):
    documents = UploadFilesModel.objects.all()
    return render(request, 'fileupload/downloadFiles.html',{'documents': documents})
