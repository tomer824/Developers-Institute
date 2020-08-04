from django.shortcuts import render

# Create your views here.


def animal(request):
    with open('animal_json.json', 'r') as f:
        animal = json.load(f)
        return render(request, )

def family(request):
    with open('family_json.json', 'r') as g:
        family = json.load(g)
        return render(request, )