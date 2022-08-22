from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("abyssraids/", abyssraids.as_view(), name="abyssraids"),
]
