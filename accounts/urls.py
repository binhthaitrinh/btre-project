from django.urls import path

from . import views

urlpatterns = [
    # path '/', root path
    # method you want to connect to in view
    # name as ref to easily access this path
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
