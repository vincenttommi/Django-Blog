from django.shortcuts import render, get_list_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage,\
 PageNotAnInteger
from  django.views.generic import ListView
# In this view, we retrieve all the posts with 
# the PUBLISHED status using the published manager that we created previously
def post_list(request):
    post_list = Post.published.all()
    
    # Pagination with 3 posts per range
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
 
    # We have added a try and except block to manage 
    # the EmptyPage exception when retrieving a page
    try:
        posts = paginator.page(page_number)
    except  PageNotAnInteger:
        # If page_number is out of range, deliver the last page of results 
        posts = paginator.page(1)
        
    except EmptyPage:   
        # if page_number is out of range deliver  last page  of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post/list.html', {'posts': posts})

# Create a view to return a single post
def post_detail(request, year, month, day, post):
    post = get_list_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    # In the detail view, we now use the get_object_or_404() shortcut to retrieve the desired post
    return render(request, 'blog/post/detail.html', {'post': post})



class  PostListView(ListView):
    """
    
    Alternative post list  view
    """
    queryset  = Post.published.all()
    content_object_name  =  'posts'
    paginate_by = 3
    template_name  = '/post/list.html'
    
# we have implemented a class-based view that inherits from the ListView class    