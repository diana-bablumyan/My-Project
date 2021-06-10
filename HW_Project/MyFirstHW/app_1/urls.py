from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='name'),
    path('greeting/', views.greeting, name='greeting'),
    path('introduction/', views.introduction, name='introduction'),
    path('datetime/', views.cur_datetime, name='datetime'),
    path('dict/', views.dict_values, name='dict'),
    path('json_web/', views.json_web, name='json'),

]