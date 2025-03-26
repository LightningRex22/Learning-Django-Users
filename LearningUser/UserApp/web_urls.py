from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('faculty-form/', views.faculty_form, name='faculty_form'),
]