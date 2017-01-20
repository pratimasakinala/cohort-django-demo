from django.shortcuts import render

from .models import Post


def post_list(request):
    post_list = Post.objects.filter(status='P')
    return render(request, 'blog/post_list.html', context={
        'post_list': post_list,
    })
