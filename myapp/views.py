from django.shortcuts import render
from post.models import Post
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    # Fetch posts and only display first five posts.
    # We'll use pagination to scroll through posts.
    post_list = get_list_or_404(Post)
    paginator = Paginator(post_list, 5)  # paginator object that contains latest five posts
    page = request.GET.get('page')  # what this do?
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # retrieves first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range then deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')
