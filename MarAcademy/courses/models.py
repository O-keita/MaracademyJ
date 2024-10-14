from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100, blank=True, null=True) 
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', max_length=500, blank=True, null=True)
    enrolled_users = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Module(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', max_length=500, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.TextField(null=True, blank=True)
    video_url = models.URLField(blank=True, null=True, max_length=3000)
    video_file = models.FileField(upload_to='lesson_videos/', blank=True, null=True)
    image = models.ImageField(upload_to='lesson_images/', blank=True, null=True)

    def __str__(self):
        return self.title   

