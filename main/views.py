from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.
def hello(request, string):
    print(string)
    context = {
        'message': string
    }
    return render(request, "hello.html", context)

def user(request, username):
    fruits = ["Apple", "Banana", "Orange"]
    context = {
        "username": username,
        "fruits": fruits
    }
    return render(request, "user.html", context)

@csrf_protect
def profile(request):
    if request.method == 'POST':
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            new_user = User.objects.create(
                first_name=fname, last_name=lname, email=email, username=username,
                is_staff=True, is_superuser=True
            )
            new_user.set_password(password)
            new_user.save()
            return redirect("hello", f"Hello {new_user.username}!")
        except Exception as e:
            return redirect("hello", f"{e}")
    context = {
        "num": 1234567890
    }
    return render(request, "profile.html", context)

"""
User:
    first_name
    last_name
    email
    username
    password
    is_active
    is_staff
    is_superuser
    last_login
    date_joined

Profile:
    user
    phone_number
    age
    gender
"""