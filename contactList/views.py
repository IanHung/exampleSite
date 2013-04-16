# Create your views here.
from django.shortcuts import render
from contactList.models import Location, Email

def index(request):
    locations_list = Location.objects.order_by('priority')
    emails_list = Email.objects.order_by('name')
    return render(request, 'contactList/contact.html', {'locations_list': locations_list, 'emails_list': emails_list})