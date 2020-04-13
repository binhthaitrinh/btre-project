from django.urls import path

from . import views

urlpatterns = [
    # path '/', root path
    # method you want to connect to in view
    # name as ref to easily access this path
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
