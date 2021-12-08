from django.shortcuts import render, get_object_or_404

import blog
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/all_blogs.html', context=context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', context={'blog': blog})
