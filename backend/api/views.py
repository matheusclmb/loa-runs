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
