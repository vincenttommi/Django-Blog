from django.shortcuts import render, get_list_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage,\
 PageNotAnInteger
# from  django.views.generic import ListView
from .forms  import  EmailPostForm
#importing class of the form to our function
from django.core.mail  import  send_mail
#importing mail from django.core.mail









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
    return render(request, 'post/detail.html', {'post': post})



# class  PostListView(ListView):
#     """
    
#     Alternative post list  view
#     """
#     queryset  = Post.published.all()
#     content_object_name  =  'posts'
#     paginate_by = 3
#     template_name  = '/post/list.html'
    
# we have implemented a class-based view that inherits from the ListView class    



def  post_share(request, post_id):
    #Retrieving  post by id
    
    post  = get_list_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
# We have defined the post_share view that takes the request object and the post_id variable as pa-
 #  rameters. We use the get_object_or_404() shortcut to retrieve a published post by its id.
    if request.method == 'POST':
        #Form  was submitted 
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #Form fields passed  validation
            cd = form.cleaned_data
            
            #send email
            post_url  = request.build_absolute_uri(post.get_absolute_url())
            #this code generates an absolute URL for a specific Post within context of webrequest
            
            subject  = f"{cd['name']} recommends you read" \
                f"{post.title}"
            
            message =  f"Read{post.title} at {post_url}\n\n"\
                f"{cd['name']}\'s comments:{cd['comments']}"
             
            send_mail(subject, message, 'vincenttommi@gmail.com',
            [cd['to']])        
                
                
            sent  = True
            
            
    else:
        form = EmailPostForm()
        
        #when  page is loaded for the first time,the view is receives a GET request
        #in this case a  new EmailPostForm is created and stored in form variable
        return render(request, 'post/share.html',{'post':post,'form':'form', 'sent':sent})
    
    

    
