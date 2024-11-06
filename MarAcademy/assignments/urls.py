from .views import assignments, assignment

from django.urls import path


urlpatterns = [

    path("assignments/<int:course_id>/", assignments, name="assignments"),
    path("assignment/", assignment, name="assignment")
]