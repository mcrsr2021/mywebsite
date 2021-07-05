from django.urls import path
from . import views
from .views import PostListView,PostCreateView,PostDetailView, PostUpdateView,PostDeleteView

urlpatterns = [
  path('',PostListView.as_view(),name='posts'),
  path('post_create',PostCreateView.as_view(),name='post_create'),
  path('post_detail/<int:pk>',PostDetailView.as_view(),name='post_detail'),
  path('post_update/<int:pk>',PostUpdateView.as_view(),name='post_update'),
  path('post_delete/<int:pk>',PostDeleteView.as_view(),name='post_delete'),
]