from django.urls import path
from .views import opportunities



urlpatterns = [
    path('opportunities', opportunities, name='opportunities')
]
