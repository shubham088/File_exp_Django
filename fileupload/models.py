# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UploadFilesModel(models.Model):
    doc = models.FileField(upload_to = 'uploads/')
