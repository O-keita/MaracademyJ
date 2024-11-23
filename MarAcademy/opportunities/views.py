from django.shortcuts import render, redirect, get_object_or_404

from courses.models import Opportunities

from .forms import opportunityForm

# Create your views here.



def opportunities(request):
    opportunities = Opportunities.objects.all()

    return render(request, 'opportunities.html', {'opportunities': opportunities}) 


def opportunity_list(request):

    if request.user.is_instructor:

        opportunities = Opportunities.objects.filter(created_by=request.user)

        return render(request, 'opportunity_list.html', {"opportunities":opportunities})

    return redirect('dashboard')

def create_opportunity(request):

    if request.user.is_instructor:

        if request.method == 'POST':

            form = opportunityForm(request.POST, None)


            if form.is_valid():

                opportunities = form.save(commit=False)

                opportunities.created_by = request.user

                opportunities.save()

                return redirect('opportunity_list')
            
        else:
            form = opportunityForm()


        


        return render(request, 'create_opportunity.html', {'form': form})
    

    return redirect('dashboard')



def update_opportunity(request, opportunity_id):



    if request.user.is_instructor:

        opportunity = get_object_or_404(Opportunities, pk=opportunity_id)

        if request.method == 'POST':

            form = opportunityForm(request.POST, instance=opportunity)

            if form.is_valid():

                opportunity = form.save(commit=False)
                opportunity.created_by = request.user
                opportunity.save()
                return redirect('opportunity_list')

        else:

            form = opportunityForm(instance=opportunity)
        return render(request, 'update_opportunity.html', {'form': form, "opportunity": opportunity})
    
    return redirect('dashboard')

