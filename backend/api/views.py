from django.http import HttpResponse
from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class blog(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        result = blogs.order_by('-id')
        serializer = BlogSerializer(result, many=True)
        return Response(serializer.data)

class abyssraids(APIView):
    def get(self, request):
        abyssraid = AbyssRaids.objects.all()
        serializer = AbyssRaidsSerializer(abyssraid, many=True)
        return Response(serializer.data)


class legionraids(APIView):
    def get(self, request):
        legionraid = LegionRaids.objects.all()
        serializer = LegionRaidsSerializer(legionraid, many=True)
        return Response(serializer.data)


class runs(APIView):
    def get(self, request):
        run = Runs.objects.all()
        serializer = RunsSerializer(run, many=True)
        return Response(serializer.data)


class CreateRun(generics.CreateAPIView):
    queryset = Runs.objects.all()
    serializer_class = RunsSerializer


# RAIDS SPECIFICS
class ArgosRuns(APIView):
    def get(self, request):
        argos = Runs.objects.filter(raid_name="Argos")
        serializer = RunsSerializer(argos, many=True)
        return Response(serializer.data)


class ValtanRunsNormal(APIView):
    def get(self, request):
        valtan = Runs.objects.filter(raid_name="Valtan").filter(difficulty="Normal")
        serializer = RunsSerializer(valtan, many=True)
        return Response(serializer.data)


class ValtanRunsHard(APIView):
    def get(self, request):
        valtan = Runs.objects.filter(raid_name="Valtan").filter(difficulty="Hard")
        serializer = RunsSerializer(valtan, many=True)
        return Response(serializer.data)


class ValtanRunsInferno(APIView):
    def get(self, request):
        valtan = Runs.objects.filter(raid_name="Valtan").filter(difficulty="Inferno")
        serializer = RunsSerializer(valtan, many=True)
        return Response(serializer.data)


class VykasRunsNormal(APIView):
    def get(self, request):
        vykas = Runs.objects.filter(raid_name="Vykas").filter(difficulty="Normal")
        serializer = AbyssRaidsSerializer(vykas, many=True)
        return Response(serializer.data)


class VykasRunsHard(APIView):
    def get(self, request):
        vykas = Runs.objects.filter(raid_name="Vykas").filter(difficulty="Hard")
        serializer = RunsSerializer(vykas, many=True)
        return Response(serializer.data)


class VykasRunsInferno(APIView):
    def get(self, request):
        vykas = Runs.objects.filter(raid_name="Vykas").filter(difficulty="Inferno")
        serializer = RunsSerializer(vykas, many=True)
        return Response(serializer.data)
