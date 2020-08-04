from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.all_people, name = 'people'),
    path('people/<int:x>/', views.people_id, name = 'people_id'),
]