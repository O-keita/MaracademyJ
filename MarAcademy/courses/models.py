from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
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
    course = models.ForeignKey(Course,  related_name='modules', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    module = models.ForeignKey(Module,related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.TextField(null=True, blank=True)
    video_url = models.URLField(blank=True, null=True, max_length=3000)
    video_file = models.FileField(upload_to='lesson_videos/', blank=True, null=True)
    image = models.ImageField(upload_to='lesson_images/', blank=True, null=True)

    def __str__(self):
        return self.title   

class Assignment(models.Model):

    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    points = models.CharField(max_length=300, null=True, default="Not graded")
    submission = models.CharField(max_length=3000, null=True, default='Url Link')
    description = models.CharField(max_length=50000)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.course.title}"
    


class AssignmentRequirement(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='requirements', on_delete=models.CASCADE)
    requirement_text = models.CharField(max_length=1000, null=True)  # each requirement as a text field

    def __str__(self):
        return f"{self.requirement_text}"
    

class AssignmentResources(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='resources', on_delete=models.CASCADE )
    text = models.CharField(max_length=1000, null=True)
    resource_url = models.URLField(blank=True, null=True, max_length=3000)

    def __str__(self):
        return  self.text



class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='submissions', on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='submissions/', blank=True, null=True)
    submission_link = models.URLField(blank=True, null=False, default='not submited')  #
    submission_date = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=30, null=True, blank=True, default="Not Yet Graded")
    feedback = models.TextField(blank=True, null=True)  # Optional feedback from instructor

    def __str__(self):
        return f"Submission by {self.student} for {self.assignment}"
    


class Progress(models.Model):
    student = models.ForeignKey(User, related_name="progress_records", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="progress_records", on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, related_name="progress_records", on_delete=models.CASCADE, blank=True, null=True)
    assignment_grade = models.CharField(max_length=30, null=True, blank=True)
    class Meta:
        unique_together = ('student', 'course', 'assignment')  # Ensure uniqueness per assignment and quiz per course per student

    def __str__(self):
        return f"{self.student.username} - {self.course.title} - {self.assignment or self.quiz}"
    

class Opportunities(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=3000, null=False)
    link = models.URLField(null=False, blank=False)
    dateline = models.DateField()



    def __str__(self):
        return  f"{self.title}"
