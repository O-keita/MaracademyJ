from .views import assignments, assignment, create_assignments, requirements

from django.urls import path


urlpatterns = [

    path("assignments/<int:course_id>/", assignments, name="assignments"),
    path("assignment/<int:assignment_id>/", assignment, name="assignment"),
    path("assignment/create/<int:course_id>",create_assignments, name="create_assignment" ),
    path("assignment/requirements/<int:assignment_id>", requirements, name='requirements' )
 
    
]