from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Assignment, AssignmentRequirement, Course, AssignmentResources, Submission, Progress
from .forms import AssignmentForm, AssignmentRequirementForm, SubmissionForm, GradeSubmissionForm, AssignmentResourseForm
# Create your views here.


def is_instructor(user):
    return user.groups.filter(name='Instructors').exists()  
@login_required
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

@login_required
def create_assignments(request, course_id):

    if request.user.is_instructor:
        course = get_object_or_404(Course, pk=course_id, instructor=request.user)
        if request.method == 'POST':

            form = AssignmentForm(request.POST)

            if form.is_valid():
                assignment = form.save(commit=False)
                assignment.course = course
                assignment.save()
                return redirect("courses:course_update", pk=course.pk )
        else:
            form  =  AssignmentForm()

            return render(request, 'create.html', {"form":form, 'course':course})
    
    return redirect('assignment', course_id=course.pk)



@login_required
def update_assignment(request, course_id, assignment_id):

    if request.user.is_instructor:

        course = get_object_or_404(Course, pk=course_id, instructor=request.user)
        assignment = get_object_or_404(Assignment, pk=assignment_id, course=course)
        requirements = AssignmentRequirement.objects.filter(assignment=assignment)
        resourse = AssignmentResources.objects.filter(assignment=assignment)

        assignment_form = AssignmentForm(request.POST, None, instance=assignment)
        requirement_form = AssignmentRequirementForm(request.POST, None)
        resource_form = AssignmentResourseForm(request.POST, None)


        if request.method == 'POST':


            if 'save_assignment' in request.POST and assignment_form.is_valid():

                assignment_form.save()

                return redirect("courses:course_update", pk=course.pk)
            
            if 'add_requirement' in request.POST and requirement_form.is_valid():
                requirement = requirement_form.save(commit=False)
                requirement.assignment = assignment
                requirement.save()
                return redirect(request.path)
            

            if 'add_resource' in request.POST and resource_form.is_valid():

                resourse = resource_form.save(commit=False)
                resourse.assignment = assignment
                resourse.save()
                return redirect(request.path)


            

        else:
            assignment_form  = AssignmentForm(instance=assignment)


        context = {
            "assignment_form": assignment_form,
            "requirement_form": requirement_form,
            "resource_form": resource_form,
            "requirements": requirements,
            "assignment": assignment,
            "resources": resourse
        }

        

        return render(request, 'create.html', context)
    
    return redirect('assignments')

@login_required
def delete_assignment(request, course_id, assignment_id):

    if request.user.is_instructor:

        course = get_object_or_404(Course, pk=course_id)

        assignment = get_object_or_404(Assignment, pk=assignment_id, course=course )


        assignment.delete()
        return redirect('courses:course_update', pk=course_id)
    
    return redirect('courses:course_list')


@login_required
def submission(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)

    if request.method == 'POST':

        form = SubmissionForm(request.POST)
      
        if form.is_valid():

            submission = form.save(commit=False)

            submission.assignment = assignment
            submission.student = request.user

            submission.save()


            Progress.objects.update_or_create(
            student=submission.student,
            course=submission.assignment.course,
            assignment=submission.assignment,
            defaults={'assignment_grade':submission.grade}
    )

        return redirect('assignment', assignment_id=assignment.pk)

    else:
        form = SubmissionForm()
    return render(request, 'submit_assignment.html', {'assignment': assignment, 'form': form})






# def grading(request, submission_id):

#     submission = get_object_or_404(Submission, id=submission_id)
#     if request.method == 'POST':
#         form = GradeForm(request.POST)
#         if form.is_valid():
#             submission.grade = form.cleaned_data['grade']
#             submission.feedback = form.cleaned_data['feedback']
#             submission.save()
#             return redirect('assignment_detail', assignment_id=submission.assignment.id)
#     else:
#         form = GradeForm(initial={'grade': submission.grade, 'feedback': submission.feedback})
#     return render(request, 'grade_submission.html', {'submission': submission, 'form': form})

def assignment_list(request):

    courses = Course.objects.filter(instructor=request.user)
    assignments = Assignment.objects.filter(course__in=courses)

    return render(request, 'assignment_list.html', {'courses': courses, 'assignments': assignments})




def submission_list(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    submissions = Submission.objects.filter(assignment=assignment)
    return render(request, 'submission_list.html', {'assignment': assignment, 'submissions': submissions})

@login_required
def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)

    if request.method == 'POST':
        form = GradeSubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()

            # Update Progress model if you want to reflect the grade there too
            Progress.objects.update_or_create(
                student=submission.student,
                course=submission.assignment.course,
                assignment=submission.assignment,
                defaults={'assignment_grade': submission.grade}
            )

            return redirect('submission_list', assignment_id=submission.assignment.id)
    else:
        form = GradeSubmissionForm(instance=submission)

    return render(request, 'grade_submission.html', {'submission': submission, 'form': form})
