from django.urls import path
from .views import ListCharacter, DetailCharacter

urlpatterns = [
    path('<int:pk>/', DetailCharacter.as_view()),
    path('', ListCharacter.as_view()),
    ]