from rest_framework import generics
from .models import Character, Logo
from .serializers import CharacterSerializer, LogoSerializer


class ListCharacter(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class DetailCharacter(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class ListLogo(generics.ListAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer


class DetailLogo(generics.RetrieveAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    lookup_field = 'name'
