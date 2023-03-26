from django.urls import path
from comments.apps import CommentsConfig
from comments.views import CommentDestroyAPIView, CommentCreateAPIView, CommentListAPIView, CommentUpdateAPIView


app_name = CommentsConfig.name


urlpatterns = [
    path('', CommentListAPIView.as_view(), name='comment_list'),
    path('update/<int:pk>/', CommentUpdateAPIView.as_view(), name='comment_update'),
    path('create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('delete/<int:pk>/', CommentDestroyAPIView.as_view(), name='comment_delete'),
              ]