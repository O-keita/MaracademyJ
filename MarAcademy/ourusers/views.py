from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser
from courses.models import Submission

from courses.models import Course

# Create your views here.

def home(request):

    Users = CustomUser.objects.count()
    Courses = Course.objects.count()
    
 
        

    return render(request, 'ourusers/home.html' , {'Users': Users, 'Courses': Courses})



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'ourusers/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)


        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_instructor:
                    return redirect('courses:course_list')
                else:   
                    return redirect('dashboard')
            
    else:
        form = AuthenticationForm()
    return render(request, 'ourusers/login.html', {'form': form})



@login_required
def dashboard(request):



    user = request.user

    courses = user.enrolled_courses.prefetch_related('assignments')

    assignments = sum(course.assignments.count() for course in courses)




    submissions = Submission.objects.filter(student=user)

    

    pending = assignments - submissions.count()



    context =  {'user': user,
                 'enrolled_courses': courses.count(),
                 'submissions': submissions.count(),
                 'pending': pending,
                 'submitted': submissions
                
                 
                 
                 }



    
    return render(request, 'ourusers/dashboard.html', context)



@login_required
def logout_view(request):   
    logout(request)
    return redirect('home')