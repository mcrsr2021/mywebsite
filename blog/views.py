from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Post

def index(request):
  return render(request,'blog/index.html',{})

class PostListView(ListView):
  model = Post
  fields = '__all__'

class PostCreateView(CreateView):
  model = Post
  fields = '__all__'

class PostDetailView(DetailView):
  model = Post

class PostUpdateView(UpdateView):
  model = Post
  fields = '__all__'

class PostDeleteView(DeleteView):
  model = Post
  success_url = '/'