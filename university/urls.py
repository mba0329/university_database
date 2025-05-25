from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('professors/', views.professor_list, name='professor_list'),
    path('professors/<int:pk>/', views.professor_detail, name='professor_detail'),

    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),

    path('phdstudents/', views.phdstudent_list, name='phdstudent_list'),
    path('phdstudents/<int:pk>/', views.phdstudent_detail, name='phdstudent_detail'),

    path('researchgroups/', views.researchgroup_list, name='researchgroup_list'),
    path('researchgroups/<int:pk>/', views.researchgroup_detail, name='researchgroup_detail'),
]