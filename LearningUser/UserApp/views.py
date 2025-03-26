from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def main(request):
    faculty = Faculty.objects.all()
    return render(request, 'main.html', {'faculty': faculty})

def register(request):
    return render(request, 'register.html')

def faculty_create_view(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # You can create a success page or redirect to any other view
    else:
        form = FacultyForm()
    return render(request, 'faculty_form.html', {'form': form})