from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('log_in/', views.LoginView.as_view(), name='log_in'),
    path('delete/', views.DeleteUserView.as_view(), name='delete'),
    path('animal_list/', views.UserAnimalListView.as_view(), name='list_user_animal'),
    path('animal_list/<int:pk>', views.UserAnimalRetrieve.as_view(), name='retrieve_user_animal'),
    path('register/', views.UserAnimalRegister.as_view()),
    path('me/', views.UserManager.as_view()),
]