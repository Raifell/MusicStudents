from django.shortcuts import render
from .models import *


def main_page(request):
    data = Student.objects.all()
    return render(request, 'students/index_main.html', {'title': 'Main', 'data': data})


def students_page(request, student_slug):
    update, valid = False, True
    data = Student.objects.get(slug=student_slug)
    if request.method == 'POST':
        update_data = request.POST

        Student.objects.filter(slug=student_slug).update(name=update_data['name'],
                                                         surname=update_data['surname'],
                                                         age=update_data['age'],
                                                         course=update_data['course'],
                                                         instrument=update_data['instrument'],
                                                         grade=update_data['grade'],
                                                         payment=True if 'payment' in update_data else False)
        update = True
    return render(request, 'students/index_students.html', {'title': 'Students Edit', 'data': data, 'update': update})


def add_page(request):
    add = False
    if request.method == 'POST':
        add_data = request.POST

        Student.objects.create(name=add_data['name'],
                               surname=add_data['surname'],
                               age=add_data['age'],
                               course=add_data['course'],
                               instrument=add_data['instrument'],
                               grade=add_data['grade'],
                               payment=True if 'payment' in add_data else False)
        add = True
    return render(request, 'students/index_add.html', {'title': 'Add', 'add': add})
