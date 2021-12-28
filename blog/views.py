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
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
def home(request):
    context={'posts':Post.objects.all()}
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model=Post
    template_name ='blog/home.html'
    context_object_name ='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return  False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return  False

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
