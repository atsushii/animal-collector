from django.urls import path

from animal import views

app_name = 'animal'

urlpatterns = [
    path('register/', views.AnimalView.as_view(), name='animal_register'),
]
