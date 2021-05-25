from django.contrib import messages
from django.shortcuts import redirect, render
from contacts.models import ContactInfo
from django.contrib.auth.models import auth


def login(request):

    contactInfo = ContactInfo.objects.first()

    return render(request, 'login/login.html', {'contactInfo': contactInfo})


def signin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('/home')
    else:
        messages.info(request, 'Invalid Credentials')
        return redirect('/login')
    return redirect('/login')
