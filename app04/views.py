from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Game
from .serializers import GameSerializer
from .permissions import IsOwnOrReanOnly

# Create your views here.
class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnOrReanOnly]