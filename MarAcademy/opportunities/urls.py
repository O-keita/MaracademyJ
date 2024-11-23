from django.urls import path
from .views import opportunities, create_opportunity, update_opportunity, opportunity_list



urlpatterns = [
    path('opportunities', opportunities, name='opportunities'), 
    path('instructor/opportunity_list', opportunity_list, name='opportunity_list' ),
    path('instructor/opportunity/create/', create_opportunity, name='create_opportunity'),
    path('instructor/opportunity/<int:opportunity_id>/update', update_opportunity, name='update_opportunity')
]
