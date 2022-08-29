from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("abyssraids/argos", ArgosRuns.as_view(), name="argosruns"),
    path("abyssraids/", abyssraids.as_view(), name="abyssraids"),
    path(
        "legionraids/valtan/normal/", ValtanRunsNormal.as_view(), name="valtan_normal"
    ),
    path("legionraids/valtan/hard/", ValtanRunsHard.as_view(), name="valtan_hard"),
    path(
        "legionraids/valtan/inferno/",
        ValtanRunsInferno.as_view(),
        name="valtan_inferno",
    ),
    path("legionraids/vykas/normal/", VykasRunsNormal.as_view(), name="vykas_normal"),
    path("legionraids/vykas/hard/", VykasRunsHard.as_view(), name="vykas_hard"),
    path("legionraids/vykas/inferno/", VykasRunsInferno.as_view(), name="vykas_hard"),
    path("legionraids/", legionraids.as_view(), name="legionraids"),
    path("runs/", runs.as_view(), name="runs"),
    path("createrun/", CreateRun.as_view(), name="create"),
    path("blog/", blog.as_view(), name="blog"),
]
