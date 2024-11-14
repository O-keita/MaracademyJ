from .views import assignments, assignment, create_assignments, submission, submission_list, grade_submission, assignment_list

from django.urls import path


urlpatterns = [

    path("assignments/<int:course_id>/", assignments, name="assignments"),
    path("assignment/<int:assignment_id>/", assignment, name="assignment"),
    path("assignment/create/<int:course_id>",create_assignments, name="create_assignment" ),
    path("submission/<int:assignment_id>", submission,name='submission'  ),
    path('assignment/<int:assignment_id>/submissions/', submission_list, name='submission_list'),
    path('submission/<int:submission_id>/grade/', grade_submission, name='grade_submission'),
    path('instructor/assignments', assignment_list, name='assignment_list')
    
    # path("assignment/grade/<int:assignment_id>", grading, name="grading")
  
]