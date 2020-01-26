# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Section(models.Model):
    href = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    background_img = models.ImageField()


class ProjectIMG(models.Model):
    img = models.ImageField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class Project(models.Model):
    href = models.CharField(max_length=255)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    background_color = models.CharField(max_length=255)
