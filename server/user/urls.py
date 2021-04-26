from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('log-in/', views.LoginView.as_view(), name='log-in'),
    path('delete/', views.DeleteUserView.as_view(), name='delete'),
    path('animal-list/', views.UserAnimalListView.as_view(), name='list-animals'),
    path('animal-list/<int:pk>', views.UserAnimalRetrieve.as_view(), name='retrieve-animal'),
    path('register/', views.UserAnimalRegister.as_view()),
    path('me/', views.UserManager.as_view()),
]