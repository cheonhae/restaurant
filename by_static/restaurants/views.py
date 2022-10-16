from asyncio import ReadTransport
from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant
#from .forms import RestaurantForm
# Create your views here.

def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, "restaurants/index.html", context)

def detail(request, pk):
    detail = Restaurant.objects.get(pk=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'restaurants/detail.html', context)