# Create your views here.
from django.shortcuts import render
from people.models import Person

def index(request):
    people_list = Person.objects.order_by('-experience', 'lastName', 'firstName')
    return render(request, 'people/people.html', {'people_list': people_list})