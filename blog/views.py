from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.


'''

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/post_list.html',
        {
            'posts': posts,
        }
    )
'''


class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/post_list.html'


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'author']


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image']

    template_name = 'blog/post_update_form.html'


'''

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request,
                  'blog/post_detail.html',
                  {
                    'post': post
                  }
                )

'''
