from django.shortcuts import render, get_object_or_404
from .models import Professor, Course, PhDStudent, ResearchGroup

def home(request):
    return render(request, 'university/home.html')

# List Views
def professor_list(request):
    view_mode = request.GET.get('view', 'block')
    professors = Professor.objects.all()
    return render(request, 'university/professors_list.html', {
        'professors': professors,
        'view_mode': view_mode,
    })

def course_list(request):
    view_mode = request.GET.get('view', 'block')
    courses = Course.objects.all()
    return render(request, 'university/courses_list.html', {
        'courses': courses,
        'view_mode': view_mode,
    })

def phdstudent_list(request):
    view_mode = request.GET.get('view', 'block')
    students = PhDStudent.objects.all()
    return render(request, 'university/phd_students_list.html', {
        'students': students,
        'view_mode': view_mode,
    })

def researchgroup_list(request):
    view_mode = request.GET.get('view', 'block')
    groups = ResearchGroup.objects.all()
    return render(request, 'university/research_groups_list.html', {
        'groups': groups,
        'view_mode': view_mode,
    })

# Detail Views remain unchanged...

# Detail Views
def professor_detail(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, 'university/professor_detail.html', {'professor': professor})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'university/course_detail.html', {'course': course})

def phdstudent_detail(request, pk):
    student = get_object_or_404(PhDStudent, pk=pk)
    return render(request, 'university/phd_student_detail.html', {'student': student})

def researchgroup_detail(request, pk):
    group = get_object_or_404(ResearchGroup, pk=pk)
    return render(request, 'university/research_group_detail.html', {'group': group})