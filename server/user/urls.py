from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('log_in/', views.LoginView.as_view(), name='log_in'),
    path('get/<int:pk>', views.UserAnimalRetrieveView.as_view(), name='retrieve_user_animal'),
    path('register/', views.UserAnimalRegister.as_view()),
    path('me/', views.UserManager.as_view()),
]