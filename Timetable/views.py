from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout

def home(request):
    return render(request, 'Timetable/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'Timetable/signupuser.html', {'form':UserCreationForm()})
    else: #Create a New User
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('personalTimetable')
            except IntegrityError:
               return render(request, 'Timetable/signupuser.html', {'form':UserCreationForm(), 'error':'This username has already been taken. Please choose a new username'})
        else:
            return render(request, 'Timetable/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})
            #Tells the user that the repeated passwords are different


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')




def personalTimetable(request):
    return render(request, 'Timetable/personalTimetable.html')
