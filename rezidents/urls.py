from django.urls import path
from . import views

urlpatterns = [
    path('', views.rezidents_list, name='rezidents_list'),
]