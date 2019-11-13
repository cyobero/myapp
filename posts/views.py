# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from posts.models import Posts

from django.shortcuts import render

# Create your views here.
def post(request, post_id):
    # make sure that post_id is an int
    try:
        post_id = int(post_id)
        post = Posts.objects.get(id=post_id)
    except ValueError:
        raise Http404

    return render(request, 'post.html', {
        'title': post.title,
        'caption': post.caption,
        'author': post.author,
        'body': post.body,
        'timestamp': post.timestamp,
    })