from django.shortcuts import render, get_object_or_404

from courses.models import Progress, Assignment, Submission

# Create your views here.

def progress(request):

    assignments =  Assignment.objects.all()


    progress = Progress.objects.filter(student=request.user)

    enrolled_courses = set()
    enrolled_assignments = []
    for assignment in assignments:
        if request.user in assignment.course.enrolled_users.all():
            enrolled_courses.add(assignment.course)
            enrolled_assignments.append(assignment)

    

    updated_progress = []

    for result in progress:

        try:
            progress_mark = int(result.assignment_grade)

            result.assignment_grade = progress_mark

            updated_progress.append(result)

        except ValueError:
            result.assignment_grade = 0
            updated_progress.append(result)






    



    return render(request, 'progress.html', {'progress':updated_progress,
                                              'assignments': enrolled_assignments, 
                                              "courses":enrolled_courses,
                                             
                                              
                                              })



