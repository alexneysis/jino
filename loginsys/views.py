# -*- coding: utf-8 -*-

import logging

from django.contrib import auth
# Create your views here.
from django.shortcuts import render, redirect
from django.template.context_processors import csrf


def login(request):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(u"Go to method login")
    args = {}
    if request.method == "POST":
        logging.debug(u"Go to if POST")
        try:
            logging.debug(u"Go to try block")
            args.update(csrf(request))
            username = request.POST.get('username')
            password = request.POST.get('password')
            logging.debug(u"Went username and password get with request")
            users = auth.authenticate(username=username, password=password)
            logging.debug(u"Went authenticate and get user " + str(type(users)))
            if users is not None:
                print("if None")
                logging.debug(u"Go to user is not None")
                auth.login(request, users)
                logging.debug(u"Login user")
                return redirect('/clinic')
            else:
                args['login_error'] = "Пользователь не найден"
                return render(request, 'loginsys/login.html', args)
        except Exception as e:
            print(e)
            return render(request, 'loginsys/error.html')
    else:
        return redirect('/clinic')


def auth_rend(request):
    return render(request, 'loginsys/login.html')


def logout(request):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(u"Register debug")
    try:
        logging.debug(u"Before logout")
        auth.logout(request)
        logging.debug(u"After logout")
    except Exception as e:
        print(e)
        return render(request, 'loginsys/error.html')
    logging.debug(u"It is end")
    return redirect('/clinic')
