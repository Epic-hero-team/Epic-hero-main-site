from django.urls import path
 
from .views import BlogListView, BlogDetailView # новое изменение
 
urlpatterns = [
    path('news/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # новое изменение
    path('news/', BlogListView.as_view(), name='news'),
]