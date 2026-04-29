from django.shortcuts import render, get_object_or_404
from .models import Subject

def index(request):
    subjects = Subject.objects.all()
    return render(request, 'index.html', {'subjects': subjects})

def generate_pdf(request, id):
    subject = get_object_or_404(Subject, id=id)
    return render(request, 'pdf_template.html', {'subject': subject})

