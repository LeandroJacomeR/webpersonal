from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about, name='about'),
    path('briefcase/', views.briefcase, name='briefcase'),
    path('contact/', views.contact, name='contact'),
]