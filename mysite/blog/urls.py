from django.urls import path
from .import views



app_name  = 'blog'
#helps to  organize  URLs  by application and use name when referring to them



urlpatterns = [
    
    #post views
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    
]
#adding url patterns for my views