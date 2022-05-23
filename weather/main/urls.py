from django.urls import path
from .views import *


urlpatterns = [
    path('', add_city),
    # path('<name:str>/delete/', DeleteCity.as_view(), 'delete_city_url')
]