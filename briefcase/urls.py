from django.urls import path
from . import views

urlpatterns = [
    path('briefcase/', views.briefcase, name='briefcase'),
]