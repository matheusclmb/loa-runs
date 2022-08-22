from django.http import HttpResponse
from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
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
