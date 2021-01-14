from rest_framework import serializers
from .models import Character, Logo


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'race', 'cls',)


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ('image', 'name')