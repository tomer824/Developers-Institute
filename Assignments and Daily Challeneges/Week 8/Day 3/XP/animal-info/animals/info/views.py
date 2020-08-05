from django.shortcuts import render
from info.models import Animals, Family

# Create your views here.

selected_animals = Animals.objects.all()

def family(request, id):
    return render(request, 'family.html', context = {'animals' : selected_animals, 'id':id})

def animal(request, id):
    return render(request, 'animal.html', context = {'animals' : selected_animals, 'id':id})

def animals(request):
    return render(request, 'animals.html', context = {'animals' : selected_animals})


# /animals/ - should show a list of all the animals. 
# When you click on any of the animals in the list, you should be taken to /animal/X (see above).