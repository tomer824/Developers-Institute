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
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')
        author_id = request.POST.get('authors_dropdown')
        author = Author.objects.get(id = author_id)
        Book(title = title, year = year, author = author).save()
    return render(request, 'new_book.html', {'authors' : Author.objects.all()})

def new_customer(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Customer(first_name = first_name, last_name = last_name).save()
    return render(request, 'new_customer.html')