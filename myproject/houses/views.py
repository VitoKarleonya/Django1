from django.shortcuts import render, get_object_or_404, redirect
from .models import House
from .forms import HouseForm

def register_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save()
            return redirect('houses:registration_success', house_id=house.id)
    else:
        form = HouseForm()
    return render(request, 'houses/register_house.html', {'form': form})

def registration_success(request, house_id):
    house = get_object_or_404(House, id=house_id)
    return render(request, 'houses/registration_success.html', {'house': house})
