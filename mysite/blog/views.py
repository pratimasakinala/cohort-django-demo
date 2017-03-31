from django.shortcuts import render, redirect
from django.views import generic

from .models import Post, Comment
from .forms import CommentForm

class PostMixin(object):
    queryset = Post.objects.filter(status='P')

class PostList(PostMixin, generic.ListView):
    template_name = 'blog/post_list.html'

class PostDetail(PostMixin, generic.DetailView):
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class CreateComment(PostMixin, generic.View):
    def post(self, request, post_id):
        post = self.queryset.get(pk=post_id)
        form = CommentForm(request.POST)
        if form_is_valid():
            # comment = Comment.objects.create(
            #     post = post,
            #     name = form.cleaned_data['name'],
            #     comment = form.cleaned_data['comment'],
            # )
            # comment.save()

            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect(post.get_absolute_url())
        return redirect(post.get_absolute_url() + '?error=1')


# def post_list(request):
#     post_list = Post.objects.filter(status='P')
#     return render(request, 'blog/post_list.html', context={
#     'post_list': post_list,
#     })
