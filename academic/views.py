# academic/views.py
from rest_framework import viewsets
from django.shortcuts import render
from .models import Teacher, Course, Student, StudentCourse
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer, StudentCourseSerializer

# ViewSets para la API REST (DRF)
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer

# --- ViewSets para la API REST (DRF) ---
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer

# --- Vistas para las Interfaces Web ---
def index_view(request):
    return render(request, 'academic/index.html')

def courses_view(request):
    return render(request, 'academic/courses.html')

def students_view(request):
    return render(request, 'academic/students.html')

def teachers_view(request):
    return render(request, 'academic/teachers.html')

def enrollments_view(request):
    return render(request, 'academic/enrollments.html')

# Vista para Error 404 personalizado
def custom_404_view(request, exception=None):
    return render(request, 'academic/404.html', status=404)