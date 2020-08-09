from django.urls import path
from . import views

urlpatterns = [
    path('new_author', views.new_author, name = 'new_author')
]