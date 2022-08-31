from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIRequestFactory

from .views import *


# Create your tests here.
class EndpointTest(TestCase):
    def test_index_view(self):
        url = reverse("home")
        self.assertEqual(url, "/api/v1/")

    # ABYSS RAIDS
    def test_abyssraids_view(self):
        url = reverse("abyssraids")
        self.assertEqual(url, "/api/v1/abyssraids/")

    def test_argos_view(self):
        url = reverse("argosruns")
        self.assertEqual(url, "/api/v1/abyssraids/argos/")

    # LEGION RAIDS
    def test_legionraids_view(self):
        url = reverse("legionraids")
        self.assertEqual(url, "/api/v1/legionraids/")

    def test_valtan_normal_view(self):
        url = reverse("valtan_normal")
        self.assertEqual(url, "/api/v1/legionraids/valtan/normal/")

    def test_valtan_hard_view(self):
        url = reverse("valtan_hard")
        self.assertEqual(url, "/api/v1/legionraids/valtan/hard/")

    def test_valtan_inferno_view(self):
        url = reverse("valtan_inferno")
        self.assertEqual(url, "/api/v1/legionraids/valtan/inferno/")

    def test_vykas_normal_view(self):
        url = reverse("vykas_normal")
        self.assertEqual(url, "/api/v1/legionraids/vykas/normal/")

    def test_vykas_hard_view(self):
        url = reverse("vykas_hard")
        self.assertEqual(url, "/api/v1/legionraids/vykas/hard/")

    def test_runs_view(self):
        url = reverse("runs")
        self.assertEqual(url, "/api/v1/runs/")

    def test_create_view(self):
        url = reverse("create")
        self.assertEqual(url, "/api/v1/createrun/")

    def test_blog_view(self):
        url = reverse("blog")
        self.assertEqual(url, "/api/v1/blog/")


factory = APIRequestFactory()


class APITest(TestCase):
    def test_abyssraid_endpoint(self):
        request = factory.get("/api/v1/abyssraids/")
        response = abyssraids.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_argos_endpoint(self):
        request = factory.get("/api/v1/abyssraids/argos/")
        response = ArgosRuns.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_legionraid_endpoint(self):
        request = factory.get("/api/v1/legionraids/")
        response = legionraids.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_valtan_normal_endpoint(self):
        request = factory.get("/api/v1/legionraids/valtan/normal/")
        response = ValtanRunsNormal.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_valtan_hard_endpoint(self):
        request = factory.get("/api/v1/legionraids/valtan/hard/")
        response = ValtanRunsHard.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_valtan_inferno_endpoint(self):
        request = factory.get("/api/v1/legionraids/valtan/inferno/")
        response = ValtanRunsInferno.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_vykas_normal_endpoint(self):
        request = factory.get("/api/v1/legionraids/vykas/normal/")
        response = VykasRunsNormal.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_vykas_hard_endpoint(self):
        request = factory.get("/api/v1/legionraids/vykas/hard/")
        response = VykasRunsHard.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_blog_endpoint(self):
        request = factory.get("/api/v1/blog/")
        response = blog.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_runs_endpoint(self):
        request = factory.get("/api/v1/runs/")
        response = runs.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_createrun_endpoint(self):
        request = factory.post(
            "/api/v1/createrun/",
            {
                "youtube": "https://www.django-rest-framework.org/api-guide/testing/",
                "screenshot": "",
                "raid_type": "Abyss Raid",
                "raid_name": "Argos",
                "difficulty": "Normal",
                "time": "23:42",
                "deathless": False,
                "discord": "user#0011",
                "playerOne": "player one",
                "playerTwo": "player two",
                "playerThree": "player three",
                "playerFour": "player four",
                "playerFive": "",
                "playerSix": "",
                "playerSeven": "",
                "playerEight": "",
                "playerOneLVL": 1480,
                "playerTwoLVL": 1456,
                "playerThreeLVL": 1505,
                "playerFourLVL": 1478,
                "playerFiveLVL": "",
                "playerSixLVL": "",
                "playerSevenLVL": "",
                "playerEightLVL": "",
                "averageIlvl": "",
            },
        )
        response = CreateRun.as_view()(request)
        self.assertEqual(response.status_code, 201)
