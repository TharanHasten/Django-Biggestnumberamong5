
from django.urls import path
from . import views

urlpatterns = [
    path('', views.max_of_five, name='max_of_five'),
]
