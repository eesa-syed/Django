from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('formpage/',views.formName, name='formpage'),
]