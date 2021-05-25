from django.contrib import messages
from django.shortcuts import redirect, render
from contacts.models import ContactInfo
from django.contrib.auth.models import User, auth


def signup(request):

    contactInfo = ContactInfo.objects.first()

    return render(request, 'signup/signup.html', {'contactInfo': contactInfo})


def register(request):

    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    phoneNo = request.POST['phone']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username not available!')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'This Email Already Have an Account!')
            return redirect('/signup')
        else:
            user = User.objects.create_user(
                username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
            user.save()
            user = auth.login(request, user)
            return redirect('/home')
    else:
        messages.info(request, 'Password not matching...')
        return redirect('/signup')

    return redirect('/signup')
