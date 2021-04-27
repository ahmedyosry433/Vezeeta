from django.urls import path
from . import views
app_name='blog'



urlpatterns = [
    path('blogs/',views.blog_list , name='blog_list'),
    path('addpost/',views.add_post , name='add_post'),
    path('^(?P<id>\d+)/edit$',views.edit_post , name='edit_post'),
    path('^(?P<id>\d+)/delete$',views.delete_post , name='delete_post'),
    path('<slug:slug>/like/',views.LikePost.as_view(), name= 'like_post'),
    

    path('<slug:slug>/',views.blog_detail , name='blog_detail')
    
]
