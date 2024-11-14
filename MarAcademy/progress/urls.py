from django.urls import path
from .views import progress


urlpatterns = [
    path("progress/", progress, name='progress')
]