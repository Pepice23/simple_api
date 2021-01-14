from django.urls import path
from .views import ListCharacter, DetailCharacter, ListLogo, DetailLogo

urlpatterns = [
    path('<int:pk>/', DetailCharacter.as_view()),
    path('logo/<str:name>/', DetailLogo.as_view()),
    path('', ListCharacter.as_view()),
    path('logo/', ListLogo.as_view()),

    ]