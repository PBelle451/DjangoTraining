from django.urls import path 
from .views import HomePageView, PostDetailView, AddPostView

app_path = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('post/', AddPostView.as_view, name='post'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
]
