from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_category/', views.create_category, name='create_category'),
]