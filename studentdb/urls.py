from django.contrib import admin
from django.urls import path
from . import views

app_name = 'studentdb'

urlpatterns = [
    path('students/', views.home, name='home'),
]
