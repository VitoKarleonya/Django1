from django.shortcuts import render, get_object_or_404
from .models import Person

def register_person(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        person = Person.objects.create(surname=surname, name=name, email=email, phone=phone)
        return render(request, 'people/registration_success.html', {'person': person})
    else:
        return render(request, 'people/register_person.html')

def registration_success(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    return render(request, 'people/registration_success.html', {'person': person})
