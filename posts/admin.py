# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from posts.models import Posts

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posts, PostsAdmin)