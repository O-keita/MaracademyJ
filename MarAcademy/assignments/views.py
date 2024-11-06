from django.shortcuts import render, get_object_or_404
from courses.models import Assignment, AssignmentRequirement, Course
# Create your views here.


def  assignments(request, course_id):


    


    course = get_object_or_404(Course, id=course_id)
    
    # Ensure user is enrolled in the course
    if request.user in course.enrolled_users.all():
        assignments = Assignment.objects.filter(course=course)
    else:
        assignments = None  # Or redirect with an error message

    context = {
        'course': course,
        'assignments': assignments,
    }
    return render(request, 'assignments.html', context)



def assignment(request):
    return render(request, "assignment.html")