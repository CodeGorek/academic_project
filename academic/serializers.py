# academic/serializers.py
from rest_framework import serializers
from .models import Teacher, Course, Student, StudentCourse

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    # Campo de lectura para mostrar el nombre completo del docente en la API
    teacher_name = serializers.ReadOnlyField(source='teacher.__str__')

    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'