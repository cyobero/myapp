# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=140)
    body = models.TextField()
    author = models.OneToOneField(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to='images')

    def __unicode__(self):
        return "%s-%s" % (self.title, str(self.id))

    class Meta:
        ordering = ['-timestamp', ]

