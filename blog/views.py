from django.shortcuts import render
from .models import Post
# Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1>Blog home</h1>')

# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')

# posts =[
#     {
#         'author':'Umarjon',
#         'title':'Blog post 1',
#         'content':'Birinchi postning matni',
#         'date_posted':'Dekabr 9, 2021'
#     },
#      {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'Dekabr 11, 2021'
#     }

# ]
def home(request):
    context={'posts':Post.objects.all()}
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})