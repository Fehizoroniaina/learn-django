from django.shortcuts import render

from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"


    template_name = 'home.html'
    sucess_url = 'PostList.html'

class PostListView(ListView):
    model = Post
    template_name = 'PostList.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'


class  PostUpdatedView(UpdateView):
    model = Post
    fields = "__all__"
    sucess_url = "/"
    template_name = 'post_update.html'


class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    sucess_url = reverse_lazy('blog:all')
    template_name = 'post_confirm_delete.html'