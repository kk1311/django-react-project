from django.shortcuts import render
from rest_framework import genereics
from .serializers import RoomSerializers
from .models import Room

# Create your views here.

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer