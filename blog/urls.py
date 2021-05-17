from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('item-photo/', views.item_photo, name='item_photo'),
    path('item-video/', views.item_video, name='item_video'),
    path('item-review/', views.item_review, name='item_review'),
]
