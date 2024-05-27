from django.urls import path
from . import views

app_name = 'houses'

urlpatterns = [
    path('register/', views.register_house, name='register_house'),
    path('registration-success/<int:house_id>/', views.registration_success, name='registration_success'),
]
