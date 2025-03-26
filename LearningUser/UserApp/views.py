from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def main(request):
    faculty = Faculty.objects.all()
    return render(request, 'main.html', {'faculty': faculty})

def faculty_form(request):
    return render(request, 'faculty_registration.html')