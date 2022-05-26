from django.urls import path
from .views import *


urlpatterns = [
    path('', add_city, name='main_page'),
    path('<str:name>/delete', DeleteCity.as_view(), name='delete_city_url'),
]