from django.urls import path
from . import views

urlpatterns = [
    # News
    path('', views.news_list, name='news_list'),
    path('<int:pk>/', views.news_detail, name='news_detail'),

    # Gallery
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/<int:pk>/', views.gallery_detail, name='gallery_detail'),

    # Documents
    path('documents/', views.document_list, name='document_list'),
]
