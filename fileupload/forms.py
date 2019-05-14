from django import forms

from fileupload.models import UploadFilesModel

class UploadFormDoc(forms.Form):
    file = forms.FileField()
