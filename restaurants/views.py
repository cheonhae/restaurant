from asyncio import ReadTransport
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurant
from .forms import RestaurantForm

# Create your views here.

def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, "restaurants/index.html", context)

def detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {
        'restaurant': restaurant,
    }
    return render(request, 'restaurants/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, files=request.FILES)
        if form.is_valid():
            #restaurant = form.save(commit=False)
            #restaurant.user = request.user
            #restaurant.save()
            restaurant = form.save()
            return redirect('restaurants:detail', restaurant.pk)
        pass
    else:
        form = RestaurantForm()
    
    context = {
        'form': form,
    }
    return render(request, 'restaurants/create.html', context)

def update(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurants:detail', restaurant.pk)
    else:
        form = RestaurantForm(instance=restaurant)
        
    context = {
        'form': form,
        'restaurant': restaurant,
    }
    return render(request, 'restaurants/update.html', context)