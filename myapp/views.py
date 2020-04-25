from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


class MyFirstView(ListView):
    template_name = "myapp/index.html"

    def get(self, request, **kwargs):
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request, self.template_name, context)


class PostCreateView(CreateView):
   """
   ビュー：登録画面
   """
   model = Post
   form_class = PostForm
   success_url = reverse_lazy('index')

   def form_valid(self, form):
       """
       登録処理
       """
       post = form.save(commit=False)
       post.save()

       return HttpResponseRedirect(self.success_url)


class PostDetailView(DetailView):
   """
   ビュー：詳細画面
   """
   model = Post

   def get_context_data(self, **kwargs):
       """
       表示データの設定
       """
       # 表示データの追加はここで 例：
       # kwargs['sample'] = 'sample'
       return super().get_context_data(**kwargs)


class PostUpdateView(UpdateView):
   """
   ビュー：詳細画面
   """
   model = Post
   form_class = PostForm
   success_url = reverse_lazy('index')

   def form_valid(self, form):
      """
      登録処理
      """
      post = form.save(commit=False)
      post.save()
 
      return HttpResponseRedirect(self.success_url)