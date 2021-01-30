from django.urls import path
from .views import CharacterList, CharacterDetail, CreateNewCharacter

urlpatterns = [
    path('karakterek/list/', CharacterList.as_view()),
    path('karakterek/<str:karakter_name>/', CharacterDetail.as_view()),
    path('uj/', CreateNewCharacter.as_view()),
]
