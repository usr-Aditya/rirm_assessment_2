from django.urls import path
from . import views
from .views import (
    StudentInfoListView, 
    StudentAcademicListView, 
    StudentAcademicDetailView, 
    StudentAcademicCreateView, 
    StudentAcademicUpdateView, 
    StudentInfoCreateView, 
    StudentInfoUpdateView,
    StudentInfoDeleteView,
    StudentAcademicDeleteView,
    )

urlpatterns = [
    path('', StudentInfoListView.as_view(), name="student-home"),
    path('details/', StudentAcademicListView.as_view(), name="student-details"),
    path('details/<pk>/', StudentAcademicDetailView.as_view(), name="student-detail"),
    path('newstudent/', StudentInfoCreateView.as_view(), name="student-create"),
    path('academics/', StudentAcademicCreateView.as_view(), name="academics-create"),
    path('info/<pk>/update/', StudentInfoUpdateView.as_view(), name="student-update"),
    path('details/<pk>/update/', StudentAcademicUpdateView.as_view(), name="academics-update"),
    path('info/<pk>/delete/', StudentInfoDeleteView.as_view(), name="student-delete"),
    path('details/<pk>/delete/', StudentAcademicDeleteView.as_view(), name="academics-delete"),
    path('search/', views.search, name="student-search"),
]
