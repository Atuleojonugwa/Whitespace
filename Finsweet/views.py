from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def blogPost(request):
    return render(request, "blogPost.html")

def Aboutus(request):
    return render(request, "Aboutus.html")

def category(request):
    return render(request, "category.html")

def authors(request):
    return render(request, "authors.html")

def contactus(request):
    return render(request, "contactus.html")

def privacypolicy(request):
    return render(request, "privacypolicy.html")