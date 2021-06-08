from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def greeting(requests):
    return HttpResponse("HELLO! AND WELCOME TO MY PERSONAL WEBSITE")


def introduction(requests):
    return HttpResponse("""Hi my friend.My name is Diana.I'm sorry for this simple look, I'm just learning
     to program. Although this is how Google started, maybe that's a good sign )""")


def cur_datetime(requests):
    return HttpResponse(datetime.datetime.now())


def dict_values(requests):
    dict_ = {}
    for i in range(1, 16):
        dict_[i] = i ** 2
    dict_str = str(dict_)
    return HttpResponse(dict_str)


