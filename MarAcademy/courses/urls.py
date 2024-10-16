from django.urls import path
from .views import course_create, course_detail, course_list, module_details, lesson_update, lesson_detail, instructor_course_list, enroll_in_course, course_update, course_delete, module_create, module_update, lesson_create
from django.conf import settings
from django.conf.urls.static import static

app_name = 'courses'  # Add this line to define the namespace

urlpatterns = [
    
    path('detail/<int:pk>/', course_detail, name='course_detail'),  # Added trailing slash
    path('list/', course_list, name='courses'),
    path('module/<int:pk>/', module_details, name='module_details'),
    path('lesson/<int:pk>/', lesson_detail, name='lesson_details'), 
    path('list/<int:pk>/', enroll_in_course, name='enroll_in_course'), 
    path('courses/', instructor_course_list, name='course_list'),
    path('courses/create/', course_create, name='course_create'),
    path('courses/update/<int:pk>/', course_update, name='course_update'),
    path('courses/delete/<int:pk>/', course_delete, name='course_delete'),
    path('modules/create/<int:course_pk>/', module_create, name='module_create'),
    path('modules/update/<int:pk>/', module_update, name='module_update'),
    path('lessons/create/<int:module_pk>/', lesson_create, name='lesson_create'),
    path('lessons/update/<int:pk>/', lesson_update, name='lesson_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
