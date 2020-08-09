from django.shortcuts import render
from . models import (Author, Book, Customer)

# Create your views here.

def new_author(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Author(first_name = first_name, last_name = last_name).save()

    return render(request, 'new_author.html')

def new_book(request):
    pass
    return render(request)

def new_customer(request):
    pass
    return render(request)