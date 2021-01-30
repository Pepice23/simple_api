from rest_framework import generics
from .models import Character
from .serializers import CharacterListSerializer, CharacterDetailSerializer, NewCharacterSerializer


class CharacterList(generics.ListAPIView):
    def get_queryset(self):
        return Character.objects.all()

    serializer_class = CharacterListSerializer


class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Character.objects.all()

    lookup_field = "karakter_name"

    serializer_class = CharacterDetailSerializer


class CreateNewCharacter(generics.CreateAPIView):
    def get_queryset(self):
        return Character.objects.all()

    serializer_class = NewCharacterSerializer
