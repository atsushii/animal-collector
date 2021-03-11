from django.urls import path

from animal import views

app_name = 'animal'

urlpatterns = [
    path('register/', views.AnimalRegisterView.as_view(), name='animal_register'),
    path('detail/<int:pk>', views.AnimalDetail.as_view(), name='animal_detail'),
]
