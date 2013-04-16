# Create your views here.
from django.shortcuts import render
from service.models import Service

def index(request):
    service_list = Service.objects.order_by('title')
    
    return render(request, 'service/service.html', {'service_list': service_list})