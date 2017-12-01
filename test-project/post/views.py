from django.contrib.auth import get_user_model
from django.core.paginator import EmptyPage
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic, View
from django.utils.translation import ugettext as _

from post.models import Post, Like, Comment


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.new()
    paginate_by = 5
    context_object_name = 'post_list'

    def paginate_queryset(self, queryset, page_size):
        """
        Overrides `MultipleObjectMixin.paginate_queryset`
        to solve EmptyPage problem
        """
        paginator = self.get_paginator(queryset, page_size)
        page_kwarg = self.page_kwarg
        page = (self.kwargs.get(page_kwarg) or
                self.request.GET.get(page_kwarg) or 1)
        try:
            page_number = int(page)
        except ValueError:
            raise Http404(_("Page can not be converted to an int."))
        try:
            page = paginator.page(page_number)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        finally:
            return paginator, page, page.object_list, page.has_other_pages()


class PostDetail(generic.DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context.get('post')
        context['comment_list'] = post.comment_set.all()
        context['like'] = post.like_from_user(self.request.user)
        return context


class CreatePost(generic.CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post/create.html'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user_model = get_user_model()
        self.object.author = user_model.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


class CreateComment(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        text = request.POST.get('comment_text')
        Comment.objects.create(text=text, post=post, author=request.user)
        return HttpResponseRedirect(
            reverse('post:post', kwargs={'pk': post.id})
        )


class LikeState(View):

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        author = request.user
        like, created = Like.objects.get_or_create(author=author, post=post)
        if not created:
            like.change_state()
        return HttpResponseRedirect(
            reverse('post:post', kwargs={'pk': post.id})
        )
