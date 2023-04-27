from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Course, Unit, Student
from django.contrib.auth.decorators import login_required

@login_required
def student_portal(request):
    if not request.user.is_authenticated:
        return redirect('login')
    student = request.user.student
    courses = Course.objects.all()
    units = Unit.objects.filter(course=student.course)
    context = {'courses': courses, 'units': units}
    return render(request, 'home_portal.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_portal')
        else:
            error_message = 'Invalid login credentials'
            context = {'error_message': error_message}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        reg_number = request.POST['reg_number']
        course_id = request.POST['course']
        course = Course.objects.get(id=course_id)
        user = User.objects.create_user(username, email, password)
        student = Student(user=user, reg_number=reg_number, course=course)
        student.save()
        return redirect('login')
    else:
        courses = Course.objects.all()
        context = {'courses': courses}
        return render(request, 'register.html', context)
 
