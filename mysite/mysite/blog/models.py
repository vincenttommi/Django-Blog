from django.db import models
from django.utils import timezone
# Create your models here.
class  Post(models.Model):
    title  = models.CharField(max_length=250)
    slug  = models.SlugField(max_length=250)
    body  =  models.TextField()
    publish  =  models.DateTimeField(default=timezone)
    #publish: This is a DateTimeField field that translates 
    # into a DATETIME column in the SQL database
    created  =  models.DateTimeField(auto_now_add=True)
    #created: This is a DateTimeField field. We will use it to store the date and time when the post
  #was created. By using auto_now_add, the date will be saved automatically when creating anobject.
    updated =  models.DateTimeField(auto_now=True)
#updated: This is a DateTimeField field. We will use it to store the last date and time when the
 #post was updated. By using auto_now, the date will be updated automatically when saving an object.
    

 

    
    
    
    def  __str__(self):
        return self.title