from django.urls import path
from recipes.views import *


urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
]
