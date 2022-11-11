from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
)


class Home(View):
    def get(self, request):
        # <view logic>
        return render(request,'home/home.html')

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog.html'
    ordering = ['-date_posted']
    paginate_by = 4

class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'slug'  # Should match the value after ':' from url <slug:slug>
    slug_field = 'slug'  # Should match the name of the slug field on the model



