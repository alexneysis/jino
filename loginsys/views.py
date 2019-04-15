# -*- coding: utf-8 -*-

from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render, redirect

from django.template.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/auth/login')
            else:
                args['login_error'] = "Пользователь не найден"
                return render(request, 'loginsys/login.html', args)
        except Exception as e:
            print(e)
            return render(request, 'loginsys/error.html')
    else:
        return render(request, 'loginsys/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/auth/login')


def registr(request):
    try:
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('mail')
        user = User.objects.create_user(username, email, password)
        user.last_name = name
        user.save()
    except Exception as e:
        print(e)
        return render(request, 'loginsys/error.html')
    return render(request, 'loginsys/login.html')
