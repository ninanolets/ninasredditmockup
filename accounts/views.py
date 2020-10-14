from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from contacts.models import Contact

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists(): 
                    messages.error(request, 'Email already registered')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')
        else: 
            messages.error(request, 'Passwords must match')
            return redirect('signup')
    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index') # MAKE IT TO DASHBOARD LATER
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out') 
        return redirect('index')


@login_required(login_url='/accounts/login')
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    
    context = {
        'contacts': user_contacts,
    }
    return render(request, 'accounts/dashboard.html', context)
