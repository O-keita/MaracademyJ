from django.shortcuts import render,get_object_or_404, redirect

from .models import Course, Module, Lesson

# Create your views here.
def course_list(request):

    courses = Course.objects.all()

    
    return render(request, 'courses/course_list.html', {'courses': courses})


def enroll_in_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.user not in course.enrolled_users.all():
        course.enrolled_users.add(request.user)
        course.save()
    return redirect('courses:course_detail', pk=course.pk)


def course_detail(request, pk):

    course = Course.objects.get(pk=pk)
    course.modules = Module.objects.filter(course=course)
    return render(request, 'courses/course_details.html', {'course': course})

def course_create(request):
    return render(request, 'courses/course_form.html')

def module_details(request, pk): 

    module = get_object_or_404(Module, pk=pk)

    module.lessons = Lesson.objects.filter(module=module)

    return render(request, 'courses/module_details.html', {'module': module})


def lesson_detail(request, pk):

    lesson = get_object_or_404(Lesson, pk=pk)

    return render(request, 'courses/lessons.html', {'lesson': lesson})