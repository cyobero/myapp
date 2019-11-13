# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from post.models import Post
from django.shortcuts import get_object_or_404

from django.shortcuts import render

# Create your views here.
def post(request, post_id):
    # make sure that post_id is an int
    try:
        post_id = int(post_id)
    except ValueError:
        raise Http404

    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post.html', {'post': post})

