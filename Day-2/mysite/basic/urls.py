from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.home,name = "home"),
    path('review', views.form, name="form"),
]