from django.shortcuts import render

def listnews(request):
    return render(request, 'blog/blog.html')

def singleblog(request):
    return render(request, 'blog/blog-details.html')
