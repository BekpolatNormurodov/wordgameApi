from django.urls import path
from .views import *

urlpatterns = [
    path('hangman/', HangmanAPIView.as_view()),
]