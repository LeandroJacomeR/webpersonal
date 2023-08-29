from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def briefcase(request):
    return render(request, 'core/briefcase.html')

def contact(request):
    return render(request, 'core/contact.html')