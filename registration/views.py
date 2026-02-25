from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration
from django.contrib.auth.hashers import make_password

def list_user(request):
    user_input="<script>alert(`you are hacked. stealing cookies. ${document.cookie}`)</script>"
    users=Registration.objects.all()
    return render(request, 'registration/index.html', {
        'users': users, 
        "user_input":user_input
        }) 

def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            hasspass=make_password(data['password'])
            registration=Registration(
                name=data['name'],
                email=data['email'],
                password=hasspass
            )
            registration.save()
            print("success")
            return render(request, 'registration/form.html', {
                'form': RegistrationForm(),
                'success': "Successfully Registered!"
                })
    else:
        form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})