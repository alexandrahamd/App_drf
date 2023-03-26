from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateAPIView, BlogUpdateAPIView, BlogDestroyAPIView, BlogListAPIView


app_name = BlogConfig.name


urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blog_list'),
    path('update/<int:pk>/', BlogUpdateAPIView.as_view(), name='blog_update'),
    path('create/', BlogCreateAPIView.as_view(), name='blog_create'),
    path('delete/<int:pk>/', BlogDestroyAPIView.as_view(), name='blog_delete'),
              ]