# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UploadFilesModel(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    doc = models.FileField(upload_to = 'uploads', validators=[FileExtensionValidator(['pdf','mp4','doc'])])

    def __str__(self):
        return self.doc
