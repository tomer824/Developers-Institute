from django.shortcuts import render
from . models import Person
from . forms import Contact_Form

# Create your views here.


def new_contact(request):
    new_person = Person(name, email, phone_number, address)
    new_person.save()
    # return render(request)
    pass

def all_contacts(request):
    #return render(request)
    pass
