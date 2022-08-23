from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("abyssraids/", abyssraids.as_view(), name="abyssraids"),
    path("legionraids/", legionraids.as_view(), name="legionraids"),
    path("runs/", runs.as_view(), name="runs"),
    path("createrun/", CreateRun.as_view(), name="create"),
]
