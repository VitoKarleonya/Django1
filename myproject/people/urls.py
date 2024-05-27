from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('people/', views.register_person, name='register_person'),
    path('registration-success/<int:person_id>/', views.registration_success, name='registration_success'),
]
