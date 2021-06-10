from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('greeting/', views.greeting),
    path('introduction/', views.introduction),
    path('datetime/', views.cur_datetime),
    path('dict/', views.dict_values),
]