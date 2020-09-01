from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomRegistrationForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        # registration_forms = UserCreationForm(request.POST)
        registration_forms = CustomRegistrationForm(request.POST)
        if registration_forms.is_valid():
            registration_forms.save()
            messages.success(request, 'CREATED ACCOUNT Successfully!!')
            return redirect('user_app:register')
    # return  HttpResponse("<h1> Registration </h1>")
    else:
        # registration_forms = UserCreationForm()
        registration_forms = CustomRegistrationForm()
    return render(request, 'register.html', {'registration_forms': registration_forms})
