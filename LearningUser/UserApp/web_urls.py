from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('create-faculty/', views.faculty_create_view, name='create_faculty'),
]