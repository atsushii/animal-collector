from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('sign_up/', views.SignUpView.as_view(), name='sign_up')
]