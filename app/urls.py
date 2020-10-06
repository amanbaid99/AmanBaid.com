from django.urls import path,include
from . import views




urlpatterns=[
    path('',views.HomePage,name='homepage'),
    path('gallery/',views.gallery,name='gallery'),
    path('skill/',views.skill,name='skill'),
    
]