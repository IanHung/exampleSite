# Create your views here.
from django.shortcuts import render
from price.models import SimplePrice, PackagePrice

def index(request):
    basic_list = SimplePrice.objects.order_by('title')
    package_list = PackagePrice.objects.order_by('title')
    return render(request, 'price/price.html', {'basic_list': basic_list, 'package_list' : package_list})