from django.urls import path
from .import views



app_name  = 'blog'
#helps to  organize  URLs  by application and use name when referring to them



urlpatterns = [
    
    #post views
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail, name='post_detail'),
    path('<int:post_id>/share/',views.post_share,name='post_share'),
    #registering a new view  in path
    
]
#adding url patterns for my views