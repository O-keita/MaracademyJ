# forms.py
from django import forms
from .models import Course, Module, Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'image']

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'description', 'image', 'course']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['module', 'title', 'content', 'description', 'video_url', 'video_file', 'image']
