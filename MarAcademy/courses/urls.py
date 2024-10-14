from django.urls import path
from .views import course_create, course_detail, course_list, module_details, lesson_detail, enroll_in_course
from django.conf import settings
from django.conf.urls.static import static

app_name = 'courses'  # Add this line to define the namespace

urlpatterns = [
    path('create/', course_create, name='course_create'),
    path('detail/<int:pk>/', course_detail, name='course_detail'),  # Added trailing slash
    path('list/', course_list, name='courses'),
    path('module/<int:pk>/', module_details, name='module_details'),
    path('lesson/<int:pk>/', lesson_detail, name='lesson_details'), 
    path('list/<int:pk>/', enroll_in_course, name='enroll_in_course'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
