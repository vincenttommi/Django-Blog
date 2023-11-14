from django.shortcuts import render,get_list_or_404
from .models import Post
from django.http import Http404


#In this view, we retrieve all the posts with 
# the PUBLISHED status using the published manager that we created previously

def  post_list(request):
    posts   =  Post.published.all()
    return render(request,'post/list.html',{'posts':posts})


#create a view to  return a single post

def post_detail(request, year, month, day, post):
    
        post =  get_list_or_404(Post,status=Post.Status.PUBLISHED,slug=post,publish__year=year,publish__month=month,publish__day=day)
       #In the detail view, we now use the get_object_or_404() shortcut to retrieve the desired post
        return render(request, 'blog/post/detail.html',{'post':post})  
    
    
    

    
      
        
        
