from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('add/', add_page, name='add_page'),
    path('students/<slug:student_slug>/', students_page, name='students_page'),
]
