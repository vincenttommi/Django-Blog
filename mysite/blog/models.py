from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
#importing user
# Create your models here.



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
#This manager retrieves all the  objects from database






class  Post(models.Model):
    
    class Status(models.TextChoices):
        #adding status field   to our model that will allow us to manage  status of blog posts
        DRAFT = 'DF','Draft'
        PUBLISHED  = 'PB','Published'
      
    title  = models.CharField(max_length=250)
    slug  = models.SlugField(max_length=250)
    author  = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    #We have imported the User model from the django.contrib.auth.models module and we have added
  #an author field to the Post model. This field defines a many-to-one relationship, meaning that each
  #post is written by a user, and a user can write any number of posts.
    
    body  =  models.TextField()
    publish  =  models.DateTimeField(default=timezone.now)
    #publish: This is a DateTimeField field that translates 
    # into a DATETIME column in the SQL database
    created  =  models.DateTimeField(auto_now_add=True)
    #created: This is a DateTimeField field. We will use it to store the date and time when the post
  #was created. By using auto_now_add, the date will be saved automatically when creating anobject.
    updated =  models.DateTimeField(auto_now=True)
#updated: This is a DateTimeField field. We will use it to store the last date and time when the
 #post was updated. By using auto_now, the date will be updated automatically when saving an object.
     
#Defining  a defualt sort order that arrranges post in a chronolgical order
    status  = models.CharField(max_length=2,choices=Status.choices, default=Status.DRAFT)
    objects  = models.Manager()  #The default manager
    published =  PublishedManager() #my custom manager

    class Meta:
        ordering  = ['-publish']
        
        indexes = [
            models.Index(fields=['-publish'])
        ]
        #databse index  - improves performance for  queries filtering or ordering results
    def  __str__(self):
        return self.title