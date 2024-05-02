from django.shortcuts import render
from django.views import  generic
from django.urls import  reverse_lazy

from .models import Post
from .forms import PostForm
# Create your views here.



class HomeView(generic.ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']


class ArticleDetailView(generic.DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields=('title', 'body')


class DeletePostView(generic.DeleteView):
    model=Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('home')
