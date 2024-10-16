from django.shortcuts import render,get_object_or_404, redirect

from .models import Course, Module, Lesson
from .forms import CourseForm, ModuleForm, LessonForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def course_list(request):

    courses = Course.objects.all()

    
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def enroll_in_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.user not in course.enrolled_users.all():
        course.enrolled_users.add(request.user)
        course.save()
    return redirect('courses:course_detail', pk=course.pk)
@login_required
def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/course_details.html', {'course': course})

@login_required
def module_details(request, pk): 

    module = get_object_or_404(Module, pk=pk)

    lessons = Lesson.objects.filter(module=module) 

    return render(request, 'courses/module_details.html', {'module': module, 'lessons': lessons})

@login_required
def lesson_detail(request, pk):

    lesson = get_object_or_404(Lesson, pk=pk)
    lesson_list = Lesson.objects.all()  

    return render(request, 'courses/lessons.html',
                   {'lesson': lesson,
                     'lesson_list': lesson_list})








@login_required
def instructor_course_list(request):
    if request.user.is_instructor:
        courses = Course.objects.filter(instructor=request.user)
        return render(request, 'instructors/course_list.html', {'courses': courses})
    else:
        return redirect('courses:course_list')

@login_required
def course_create(request):
    if request.user.is_instructor:

        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES)  # Include FILES for image uploads
            if form.is_valid():
                course = form.save(commit=False)
                course.instructor = request.user  # Set the logged-in user as the instructor
                course.save()
                return redirect('courses:course_list')
        else:
            form = CourseForm()
        return render(request, 'instructors/course_form.html', {'form': form})
    else:
        return redirect('courses:course_list')

@login_required
def course_update(request, pk):

    if request.user.is_instructor:
  
        course = get_object_or_404(Course, pk=pk, instructor=request.user)

        modules = course.modules.all() 

        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                form.save()
                return redirect('courses:course_list')
        else:
            form = CourseForm(instance=course)
        return render(request, 'instructors/course_form.html', {'form': form, 'modules': modules})

    else:
        return redirect('courses:course_list')

@login_required
def course_delete(request, pk):
    if request.user.is_instructor:

        course = get_object_or_404(Course, pk=pk, instructor=request.user)
        if request.method == 'POST':
            course.delete()
            return redirect('courses:course_list')
        return render(request, 'instructors/course_confirm_delete.html', {'course': course})
    else:
        return redirect('courses:course_list')

# Module views@login_required
def module_create(request, course_pk):
    if request.user.is_instructor:
        course = get_object_or_404(Course, pk=course_pk, instructor=request.user)
        if request.method == 'POST':
            form = ModuleForm(request.POST, request.FILES)
            if form.is_valid():
                module = form.save(commit=False)
                module.course = course
                module.save()
                # Redirect to the update page for the newly created module
                return redirect('courses:course_update', pk=module.course.pk)
        else:
            form = ModuleForm()
        # Render form with course information
        return render(request, 'instructors/module_form.html', {'form': form, 'course': course})
    else:
        # Redirect non-instructors to the course list
        return redirect('courses:course_list')

    
@login_required
def module_update(request, pk):
    if request.user.is_instructor:
        module = get_object_or_404(Module, pk=pk)
        course = module.course
        lessons = module.lessons.all() 
        if request.method == 'POST':
            form = ModuleForm(request.POST, request.FILES, instance=module)
            if form.is_valid():
                form.save()
                return redirect('courses:course_update', pk=module.course.pk)
        else:
            form = ModuleForm(instance=module)
        return render(request, 'instructors/module_form.html', {'form': form, 'course': course, 'lessons': lessons, 'module': module})
    else:
        return redirect('courses:course_list')
@login_required
def lesson_create(request, module_pk):
    if request.user.is_instructor:
        module = get_object_or_404(Module, pk=module_pk)
        if request.method == 'POST':
            form = LessonForm(request.POST, request.FILES)
            if form.is_valid():
                lesson = form.save(commit=False)
                lesson.module = module
                lesson.save()
                return redirect('courses:module_update', pk=module.pk)
        else:
            form = LessonForm()
        return render(request, 'instructors/lesson_form.html', {'form': form, 'module': module})
    else:
        return redirect('courses:course_list')
    

@login_required
def lesson_update(request, pk):
    if request.user.is_instructor:
        lesson = get_object_or_404(Lesson, pk=pk)
        module = lesson.module
        if request.method == 'POST':
            form = LessonForm(request.POST, request.FILES, instance=lesson)
            if form.is_valid():
                form.save()
                return redirect('courses:module_update', pk=module.pk)

        else:
            form = LessonForm(instance=lesson)
        return render(request, 'instructors/lesson_form.html', {'form': form, 'module': module})

    else:
        return redirect('courses:course_list')