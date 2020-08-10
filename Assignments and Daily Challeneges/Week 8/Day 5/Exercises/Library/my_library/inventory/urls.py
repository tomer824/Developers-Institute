from django.urls import path
from . import views

urlpatterns = [
    path('new_author', views.new_author, name = 'new_author'),
    path('new_book', views.new_book, name = 'new_book'),
    path('new_customer', views.new_customer, name = 'new_customer'),
]