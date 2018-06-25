from django.conf.urls import include, re_path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('styleguide/', views.styleguide, name='styleguide'),

    path('authors/', views.AuthorListView.as_view(), name='authors'),
    
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),

    #path('hashtags/', views.HashtagListView.as_view(), name='hashtags'),
    
    re_path(r'^hashtag/(?P<pk>\d+)/$', views.HashtagDetailView.as_view(), name='hashtag-detail'),

    path('posts/', views.PostListView.as_view(), name='posts'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post-detail'),
]

