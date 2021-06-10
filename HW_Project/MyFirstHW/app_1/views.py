from django.shortcuts import render
from django.http import HttpResponse
import datetime


def home(requests):
    return HttpResponse("<h1>WELCOME OUR WEBSITE</h1>")



def greeting(requests):
    return HttpResponse("<strong>HELLO! AND WELCOME TO MY PERSONAL WEBSITE</strong>")


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


