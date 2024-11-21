from django.shortcuts import render

from courses.models import Opportunities

# Create your views here.



def opportunities(request):
    opportunities = Opportunities.objects.all()


    return render(request, 'opportunities.html', {'opportunities': opportunities})