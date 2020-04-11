from django.urls import path

from . import views

urlpatterns = [
    # path '/', root path
    # method you want to connect to in view
    # name as ref to easily access this path
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]
