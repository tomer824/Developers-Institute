from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("hello word, youre at polls index")

# def index(request):
#     return render(request, 'index.html')


#below is from course notes - copy / paste

def index(request):
    parties = [
        {"name": "Likud", "votes": 62},
        {"name" : "blue and white", "votes" : 58}
    ]

    return render(request, 'index.html', context = {'parties_var' : parties})

def home(request):
    return render(request, "homepage.html")