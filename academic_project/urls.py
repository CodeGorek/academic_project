"""
URL configuration for academic_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# academic_project/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from academic.views import (
    TeacherViewSet, CourseViewSet, StudentViewSet, StudentCourseViewSet,
    index_view, courses_view, students_view, teachers_view, enrollments_view, custom_404_view
)

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'student-courses', StudentCourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', index_view, name='index'),
    path('courses/', courses_view, name='courses'),
    path('students/', students_view, name='students'),
    path('teachers/', teachers_view, name='teachers'),
    path('enrollments/', enrollments_view, name='enrollments'),
    re_path(r'^.*$', custom_404_view),
]