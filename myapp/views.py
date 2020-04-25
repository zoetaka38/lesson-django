from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Post

class MyFirstView(ListView):
    template_name = "myapp/index.html"

    def get(self, request, **kwargs):
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request, self.template_name, context)