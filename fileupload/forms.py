from django import forms



class UploadFormDoc(forms.Form):

    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=50)
    file = forms.FileField()
