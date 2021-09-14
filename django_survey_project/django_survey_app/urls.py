from django.http.response import HttpResponseRedirect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('result', views.result),
]