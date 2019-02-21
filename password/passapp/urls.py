from django.urls import path
from passapp import views

app_name = 'passapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login')
]
