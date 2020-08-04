from django.shortcuts import render

# Create your views here.

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
     'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
     'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
     'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]


def all_people(request):
    return render(request, 'people.html', context = {"all_people" : people})

def people_id(request, x):
    return render(request, 'people_id.html', context = {"person" : people[x - 1]})
