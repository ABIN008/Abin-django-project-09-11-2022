from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('questions/',views.question_list,name='questions'),
     path('choices/<int:id>/',views.choose,name='choices')
    
]