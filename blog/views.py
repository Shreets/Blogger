from django.shortcuts import render, get_object_or_404
from .filters import BlogFilter
from blog.models import *


def blogdisplay(request):
    blog = Blog.objects.all().order_by('-date_created')
    myFilter = BlogFilter(request.GET, queryset=blog)
    blog = myFilter.qs
    context = {'blogs': blog, 'filter':myFilter}
    return render(request, 'blog/blogs.html', context)


def details(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    context = {'blogs': blog}
    return render(request, 'blog/details.html', context)