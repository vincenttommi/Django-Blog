from django.db import models
from  django.utils import timezone

# Create your models here.
class  Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT  = 'DF','Draft'
        
        PUBLISHED ='PB', 'Published'
        
    
    
    
    title  = models.CharField(max_length=250)
    slug  = models.SlugField(max_length=250)
    body =  models.TimeField()
    publish  = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    #sadding status field
    status  =  models.CharField(max_length=2, choices=Status.choices,default=Status.DRAFT)
    
    
    
    
    #defining a default sort order
    class  Meta:
        ordering  = ['-publish']
        
        
        #adding database index that helps  in improving performance  for queries filtering or 
        # ordering results by field
        
        indexes  = [
            models.Index(fields=['-publish']),
        ]
    
    def __str__(self):
        return self.title
    
    
