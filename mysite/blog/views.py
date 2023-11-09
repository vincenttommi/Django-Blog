from django.shortcuts import render
from .models import Post
from djang.http import Http404


#In this view, we retrieve all the posts with 
# the PUBLISHED status using the published manager that we created previously

def  post_list(request):
    posts   =  Post.published.all()
    return render(request,'blog/post/list.html',{'posts':posts})


#create a view to  return a single post

def post_detail(request,id):
    try:
        post =  Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    
    return render(request, 'blog/post/detail.html',{'post':post})    
        
        
