from django import forms

from fileupload.models import UploadFilesModel

class UploadFormDoc(forms.Form):
    file = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
