from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests
import json


def home(requests):
    a = {}
    if requests.method == 'POST':
        print(requests.POST)
        a = requests.POST
        dict_= {}

        dict_['name'] = a.get('fname')
        dict_['surname'] = a.get('sname')
        dict_['age'] = a.get('age')

        with open('user.json', 'w') as file:
             json.dump(dict_, file, indent=4)
        print('aaa')
    return render(requests, 'app_1/image.html')


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


def json_web(requests):
    with open("band_json.json", "r") as file:
        data = json.load(file)
        dict_ = {}
        key = 1
        for data in data['bands']:
            dict_[f'key{key}'] = data
            key += 1
        # str_data = str(data)
        return render(requests, 'app_1/json_data.html', dict_)

