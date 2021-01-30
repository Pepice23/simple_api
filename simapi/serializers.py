from rest_framework import serializers
from .models import Character


class CharacterListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("karakter_name",)
        model = Character


class CharacterDetailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("karakter_name", "race", "cls")
        model = Character


class NewCharacterSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("karakter_name", )
        model = Character
