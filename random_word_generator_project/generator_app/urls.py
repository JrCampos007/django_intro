from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),                  # root route
    path('random_word', views.random),      # random_word
    path('reset', views.reset),             # reset
]