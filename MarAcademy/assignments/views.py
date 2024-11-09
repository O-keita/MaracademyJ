from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Assignment, AssignmentRequirement, Course, AssignmentResources
from .forms import AssignmentForm, AssignmentRequirementForm
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



def assignment(request, assignment_id):


    assignment = get_object_or_404(Assignment, pk=assignment_id )

    requirements = AssignmentRequirement.objects.filter(assignment=assignment)

    resources = AssignmentResources.objects.filter(assignment=assignment)

    return render(request, "assignment.html", {'assignment':assignment, 
                                               'requirements': requirements,
                                                 "resources": resources})


def create_assignments(request, course_id):

    if request.user.is_instructor:
        course = get_object_or_404(Course, pk=course_id, instructor=request.user)
        if request.method == 'POST':

            form = AssignmentForm(request.POST)

            if form.is_valid():
                assignment = form.save(commit=False)
                assignment.course = course
                assignment.save()
                return redirect("assignments", course_id=assignment.course.pk )
        else:
            form  =  AssignmentForm()

            return render(request, 'create.html', {"form":form, 'course':course})
    
    return redirect('assignment')


def requirements(request, assignment_id):
    if request.user.is_instructor:

        assignment = get_object_or_404(Assignment, pk=assignment_id)

        if request.method == 'POST':

            form = AssignmentRequirementForm

            if form.is_valid():

                requirement = form.save(commit=False)
                requirement.assignments = assignment
                requirement.save()
                return redirect("requirements", pk=assignment.pk)
        else:

            form = AssignmentRequirementForm()
            return render(request, 'requirements.html', {'form':form})
            

    return render(request, 'create.html')






    
 