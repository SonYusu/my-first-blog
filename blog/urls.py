from django.urls import path,include
from . import views

appname = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'),
]