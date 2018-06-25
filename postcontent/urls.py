from django.conf.urls import include, re_path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('styleguide/', views.styleguide, name='styleguide'),

    path('authors/', views.AuthorListView.as_view(), name='authors'),
    
    path('posts/', views.PostListView.as_view(), name='posts'),
    
    re_path(r'^author/(?P<slug>[\w-]+)/$', views.AuthorDetailView.as_view(), name='author-detail'),
    
    re_path(r'^hashtag/(?P<slug>[\w-]+)/$', views.HashtagDetailView.as_view(), name='hashtag-detail'),

    re_path(r'^post/(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name='post-detail'),
]

