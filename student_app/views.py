from django.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentInfo, StudentAcademics
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    FormView, 
    DetailView,
    CreateView,
    DeleteView,
    UpdateView)

@login_required
def home(request):
    context = {
        'studentsinfo': StudentInfo.objects.all(),
        'studentsacademics': StudentAcademics.objects.all()
    }
    return render(request, 'student_app/home.html', context)

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        student_searched = StudentInfo.objects.filter(name__contains = searched)
        parallel_searched = StudentAcademics.objects.filter(roll_no = student_searched.first().roll_no).all()
        for student in parallel_searched:
            print(student)
        context = {
            'searched':searched,
            'parallel_searched':parallel_searched,
            'student_searched':student_searched,
        }
        return render(request, 'student_app/search.html', context)
    else:
        context = {}
        return render(request, 'student_app/search.html', context)

class StudentInfoListView(ListView):
    model = StudentInfo
    template_name = 'student_app/home.html'
    context_object_name = 'studentsinfo' 

class StudentAcademicListView(ListView):
    model = StudentAcademics
    template_name = 'student_app/studentdetails.html'
    context_object_name = 'studentacademics'


class StudentAcademicDetailView(DetailView):
    model = StudentAcademics

class StudentInfoCreateView(LoginRequiredMixin, CreateView):
    model = StudentInfo
    fields = '__all__'

class StudentAcademicCreateView(LoginRequiredMixin, CreateView):
    model = StudentAcademics
    fields = '__all__'

class StudentInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = StudentInfo
    fields = '__all__'

class StudentAcademicUpdateView(LoginRequiredMixin, UpdateView):
    model = StudentAcademics
    fields = '__all__'

class StudentInfoDeleteView(LoginRequiredMixin, DeleteView):
    model = StudentInfo
    success_url = '/student/'

class StudentAcademicDeleteView(LoginRequiredMixin, DeleteView):
    model = StudentAcademics
    success_url = '/details/'

